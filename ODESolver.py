import numpy as np
import scipy.linalg as la

class FVBoundary:
    def __init__(self):
        pass

class FVTransverse(FVBoundary):
    def __init__(self,solver):
        FVBoundary.__init__(self)
        self.solver = solver
    
    def apply(self,Q):
        if self.solver == 'explicit':
            Q[0] = Q[1]
            Q[-1] = Q[-2]            
        elif self.solver == 'implicit':
            Q[0] = Q[1]
            Q[-1] = Q[-2]
        else:
            print('error in applying boundary - no solver given')
        return Q

#FV ODE Solver techniques
class FVODESOlver:
    #__metaclass__ = abc.ABCMeta
    def __init__(self,bry_strategy,solver):
        self.brytype = bry_strategy(solver)
        self.src_functor = {}
    
    def set_src(self,eqid,src_functor):
        self.src_functor[eqid] = src_functor
        
    def apply_boundary(self,Q):
        return self.brytype.apply(Q)
    
    def apply_src(self,eqid,delta_t,delta_x,j):
        S = self.src_functor[eqid](delta_t,delta_x,j)
        return S
    
    def solve_conservative_without_outerloop(self,eqid,delta_t,delta_x,Q,V,cc):
        print("Base class function solve_conservative_without_outerloop should not have been called")
        raise NotImplementedError()
    
    def solve_non_conservative_without_outerloop(self,eqid,delta_t,delta_x,Q,V,cc):
        print("Base class function solve_non_conservative_without_outerloop should not have been called")
        raise NotImplementedError()
    
    def solve_conservative_with_outerloop(self,delta_t,delta_x,Q,V):
        print("Not implemented: solve_conservative_with_outerloop")
        raise NotImplementedError() 
    
    def solve_non_conservative_with_outerloop(self,delta_t,delta_x,Q,V):
        print("Not implemented: solve_non_conservative_with_outerloop")
        raise NotImplementedError()

#This is explicit Euler, with upwinding
class ODEExplicit(FVODESOlver):
    def __init__(self,params):
        FVODESOlver.__init__(self,params.fv_boundary_strategy,'explicit')
    
    def solve_conservative_without_outerloop(self,delta_t,delta_x,Q,V,eqid=0,cc=False):
        numj  = len(Q)
        Q_new = np.zeros_like(Q)
        mu = delta_t/delta_x
        
        if cc == True: #Cell centered FV
            for j in range(1,numj-1): 
                if V[j] > 0:
                    Q_new[j] = Q[j] - mu*(Q[j]*V[j+1] - Q[j-1]*V[j])
                else:
                    Q_new[j] = Q[j] - mu*(Q[j+1]*V[j+1] - Q[j]*V[j])
        else: #Vertex centered FV
            for j in range(1,numj-2):
                Vi_avg = (V[j]+V[j-1])/2
                Vj_avg = (V[j]+V[j+1])/2        
                if Vj_avg > 0:
                    Q_new[j] = Q[j] - mu*(Q[j]*Vj_avg - Q[j-1]*Vi_avg)
                else:
                    Q_new[j] = Q[j] - mu*(Q[j+1]*Vj_avg - Q[j]*Vi_avg)
                
        Q_new = self.apply_boundary(Q_new)
        return Q_new
    
    def solve_non_conservative_without_outerloop(self,delta_t,delta_x,Q,V,eqid,cc=False):
        numj  = len(Q)
        Q_new = np.zeros_like(Q)
        mu = delta_t/delta_x
        
        if cc == True: #Cell centered FV
            for j in range(1,numj-1): 
                if V[j] > 0:
                    Q_new[j] = Q[j] - mu*(Q[j]*V[j+1] - Q[j-1]*V[j]) + self.apply_src(eqid,delta_t,delta_x,j)
                else:
                    Q_new[j] = Q[j] - mu*(Q[j+1]*V[j+1] - Q[j]*V[j]) + self.apply_src(eqid,delta_t,delta_x,j)
        else: #Vertex centered FV
            for j in range(1,numj-2):
                Vi_avg = (V[j]+V[j-1])/2
                Vj_avg = (V[j]+V[j+1])/2        
                if Vj_avg > 0:
                    Q_new[j] = Q[j] - mu*(Q[j]*Vj_avg - Q[j-1]*Vi_avg) + self.apply_src(eqid,delta_t,delta_x,j)
                else:
                    Q_new[j] = Q[j] - mu*(Q[j+1]*Vj_avg - Q[j]*Vi_avg) + self.apply_src(eqid,delta_t,delta_x,j)
                
        Q_new = self.apply_boundary(Q_new)
        return Q_new


#This is implicit Euler with upwinding
class ODEImplicit(FVODESOlver):
    def __init__(self,params):
        FVODESOlver.__init__(self,params.fv_boundary_strategy,'implicit')
        self.alpha = params.alpha
    
    def solve_conservative_without_outerloop(self,delta_t,delta_x,Q,V,eqid,cc=False):
        numj  = len(Q)
        Q_new = np.zeros_like(Q)
        mu = delta_t*delta_x
        
        #Solve tridiagonal matrix equation Ax=y
        
        #The three diagonals are stored in matrix A starting from upper diag        
        A = np.zeros((3,numj-2))
        y = np.zeros(numj-2)
        
        A_test = np.zeros((numj-2,numj-2))
        
        #Unavoidable loop to create matrix A and vector y
        if cc == True: #Cell centered FV
            for j in range(1,numj-1): 
                if V[j] > 0:
                    #A[0,j-1] = 0 #c
                    #A[1,j-1] = (delta_x+self.alpha*V[j+1]*delta_t)/mu  #b
                    #A[2,j-1] = (-self.alpha*V[j])/delta_x #a
                    
                    if j > 1:
                        A_test[j-1,j-2] = (-self.alpha*V[j])/delta_x #a
                    A_test[j-1,j-1] = (delta_x+self.alpha*V[j+1]*delta_t)/mu #b
                    if (j+1) < (numj-2):
                        A_test[j-1,j+1] = 0  #c
                    
                        
                else:
                    #A[0,j-1] = (self.alpha*V[j+1])/delta_x #c
                    #A[1,j-1] = (delta_x-self.alpha*V[j]*delta_t)/mu  #b
                    #A[2,j-1] = 0 #a
                    
                    if j > 1:
                        A_test[j-1,j-2] = 0 #a
                    A_test[j-1,j-1] = (delta_x-self.alpha*V[j]*delta_t)/mu #b
                    if (j+1) < (numj-2):
                        A_test[j-1,j+1] = (self.alpha*V[j+1])/delta_x  #c
                        
                y[j-1] = self.apply_src(eqid, delta_t, delta_x, j)             
        else: #Vertex centered FV
            for j in range(1,numj-1):
                Vi_avg = (V[j]+V[j-1])/2
                Vj_avg = (V[j]+V[j+1])/2        
                if Vj_avg > 0:
                    #A[0,j-1] = 0 #c
                    #A[1,j-1] = (delta_x+self.alpha*Vj_avg*delta_t)/mu  #b
                    #A[2,j-1] = (-self.alpha*Vi_avg)/delta_x #a
                    
                    if j > 1:
                        A_test[j-1,j-2] = (-self.alpha*Vi_avg)/delta_x #a
                    A_test[j-1,j-1] = (delta_x+self.alpha*Vj_avg*delta_t)/mu #b
                    if (j+1) < (numj-2):
                        A_test[j-1,j+1] = 0  #c
                else:
                    #A[0,j-1] = (self.alpha*Vj_avg)/delta_x #c
                    #A[1,j-1] = (delta_x-self.alpha*Vi_avg*delta_t)/mu  #b
                    #A[2,j-1] = 0 #a
                    
                    if j > 1:
                        A_test[j-1,j-2] = 0 #a
                    A_test[j-1,j-1] = (delta_x-self.alpha*Vi_avg*delta_t)/mu #b
                    if (j+1) < (numj-2):
                        A_test[j-1,j+1] = (self.alpha*Vj_avg)/delta_x  #c
                        
                y[j-1] = self.apply_src(eqid, delta_t, delta_x, j)
                        
        #Apply boundary - TBD refactor
        if V[0] > 0:
            a0 = (-self.alpha*V[0])/delta_x
        else:
            a0 = 0
        A[1,0] = A[1,0] + a0
        
        if V[numj-2] > 0:
            cend = 0
        else:
            cend = (self.alpha*V[numj-1])/delta_x
        A[1,-1] = A[1,-1] + cend
        
        #Solve tridiagonal system of equations        
        #Q_new[1:numj-1] = la.solve_banded ((1,1),A,y)
        
        Q_new[1:numj-1] = np.linalg.solve(A_test, y) 
        
        Q_new = self.apply_boundary(Q_new)           
        
        return Q_new
    
    def solve_non_conservative_without_outerloop(self,delta_t,delta_x,Q,V,eqid,cc=False):
        return self.solve_conservative_without_outerloop(delta_t,delta_x,Q,V,eqid,cc)
        
    