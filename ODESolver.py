import numpy as np
import scipy.linalg as la

class FVBoundary:
    def __init__(self):
        pass

class FVTransverse(FVBoundary):
    def __init__(self):
        FVBoundary.__init__(self)
    
    def apply(self,Q):
        Q[0] = Q[1]
        Q[-1] = Q[-2]
        return Q
       
    
    def preapply(self,A,y):
        """
        Convert to tridiagonal form with TV boundary applied as:
        A = 
        | c1  c2  c3  c4 |       | 0       c1  c2    c3    |
        | b1  b2  b3  b4 |  -->  |(a1+b1)  b2  b3  (b4+c4) |
        | a1  a2  a3  a4 |       |a2       a3  a4    0     |
        
        y remains unchanged in TV boundary
        """
        A[1,0] = A[1,0] + A[2,0]
        A[1,-1] = A[1,-1] + A[0,-1]
        
        A[0,1:] = A[0,0:-1]
        A[0,0] = 0 #not needed
        
        A[2,0:-1] = A[2,1:]
        A[2,-1] = 0 #not needed
        
        return [A,y]

#FV ODE Solver techniques
class FVODESOlver:
    #__metaclass__ = abc.ABCMeta
    def __init__(self,name,bry_strategy):
        self.brytype = bry_strategy()
        self.src_functor = None
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_src(self,src_functor):
        self.src_functor = src_functor
        
    def apply_boundary(self,Q):
        return self.brytype.apply(Q)
    
    def preapply_boundary(self,A,y):
        return self.brytype.preapply(A,y)
    
    def apply_src(self,eqid,delta_t,delta_x,j):
        S = self.src_functor.calculate_source(eqid,delta_t,delta_x,j)
        return S
    
    def get_abc(self,eqid,delta_t,delta_x,j):
        S = self.src_functor.calculate_abc(eqid,delta_t,delta_x,j)
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
    
    def solve_user_defined_without_outerloop(self,numj,delta_t,delta_x):
        print("Not implemented: solve_user_defined_without_outerloop")
        raise NotImplementedError()

#This is explicit Euler, with upwinding
class ODEExplicit(FVODESOlver):
    def __init__(self,params):
        FVODESOlver.__init__(self,params.name,params.fv_boundary_strategy)
    
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
            for j in range(1,numj-1):
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
        FVODESOlver.__init__(self,params.name,params.fv_boundary_strategy)
        self.alpha = params.alpha
    
    def solve_conservative_without_outerloop(self,delta_t,delta_x,Q,V,eqid,cc=False):
        numj  = len(Q)
        Q_new = np.zeros_like(Q)
        mu = delta_t*delta_x
        
        #Solve tridiagonal matrix equation Ax=y
        
        #The three diagonals are stored in matrix A starting from upper diag        
        A = np.zeros((3,numj-2))
        y = np.zeros(numj-2)
        
               
        #Unavoidable loop to create matrix A and vector y
        if cc == True: #Cell centered FV
            for j in range(1,numj-1): 
                if V[j] > 0:
                    c = 0
                    b = (delta_x+self.alpha*V[j+1]*delta_t)/mu
                    a = (-self.alpha*V[j])/delta_x
                else:
                    c = (self.alpha*V[j+1])/delta_x
                    b = (delta_x-self.alpha*V[j]*delta_t)/mu
                    a = 0
                
                A[0,j-1] = c
                A[1,j-1] = b
                A[2,j-1] = a
                y[j-1] = self.apply_src(eqid, delta_t, delta_x, j)             
        else: #Vertex centered FV
            for j in range(1,numj-1):
                Vi_avg = (V[j]+V[j-1])/2
                Vj_avg = (V[j]+V[j+1])/2        
                if Vj_avg > 0:
                    c = 0
                    b = (delta_x+self.alpha*Vj_avg*delta_t)/mu
                    a = (-self.alpha*Vi_avg)/delta_x
                    
                else:
                    c = (self.alpha*Vj_avg)/delta_x
                    b = (delta_x-self.alpha*Vi_avg*delta_t)/mu
                    a = 0
                
                A[0,j-1] = c
                A[1,j-1] = b
                A[2,j-1] = a                    
                y[j-1] = self.apply_src(eqid, delta_t, delta_x, j)
                     
        [A,y] = self.preapply_boundary(A,y)
        
        #Solve tridiagonal system of equations        
        Q_new[1:numj-1] = la.solve_banded ((1,1),A,y)
        
        Q_new = self.apply_boundary(Q_new)           
        
        return Q_new
    
    def solve_non_conservative_without_outerloop(self,delta_t,delta_x,Q,V,eqid,cc=False):
        return self.solve_conservative_without_outerloop(delta_t,delta_x,Q,V,eqid,cc)
        
        
    def solve_user_defined_without_outerloop(self,numj,delta_t,delta_x,eqid,cc=False):
        Q_new = np.zeros(numj)
        
        #Solve tridiagonal matrix equation Ax=y
        
        #The three diagonals are stored in matrix A starting from upper diag        
        A = np.zeros((3,numj-2))
        y = np.zeros(numj-2)        
               
        #Unavoidable loop to create matrix A and vector y
        if cc == True: #Cell centered FV
            for j in range(1,numj-1): 
                [a,b,c] = self.get_abc(eqid,delta_t,delta_x,j)                
                A[0,j-1] = c
                A[1,j-1] = b
                A[2,j-1] = a
                y[j-1] = self.apply_src(eqid, delta_t, delta_x, j)             
        else: #Vertex centered FV
            print("Unexpected argument: Not implemented")
            return None
                     
        [A,y] = self.preapply_boundary(A,y)
        
        #Solve tridiagonal system of equations        
        Q_new[1:numj-1] = la.solve_banded ((1,1),A,y)
        
        Q_new = self.apply_boundary(Q_new)           
        
        return Q_new