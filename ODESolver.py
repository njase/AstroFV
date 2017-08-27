#import abc
import numpy as np

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

#FV ODE Solver techniques
class FVODESOlver:
    #__metaclass__ = abc.ABCMeta
    def __init__(self,bry_strategy):
        self.brytype = bry_strategy()
        self.src_functor = {}
    
    def set_src(self,eqid,src_functor):
        self.src_functor[eqid] = src_functor
        
    def apply_boundary(self,Q):
        return self.brytype.apply(Q)
    
    def apply_src(self,eqid,delta_t,delta_x,j):
        S = self.src_functor[eqid](delta_t,delta_x,j)
        return S
    
    def solve_conservative_without_outerloop(self,delta_t,delta_x,Q,V,cc):
        print("Base class function solve_conservative_without_outerloop should not have been called")
    
    def solve_non_conservative_without_outerloop(self,delta_t,delta_x,Q,V,src_functor,cc):
        print("Base class function solve_non_conservative_without_outerloop should not have been called")
        
    def solve_conservative_with_outerloop(self,delta_t,delta_x,Q,V,cc):
        raise NotImplementedError() 
    
    def solve_non_conservative_with_outerloop(self,delta_t,delta_x,Q,V,cc):
        raise NotImplementedError()

#This is explicit Euler, with upwinding
class ODEExplicit(FVODESOlver):
    def __init__(self,bry_strategy=FVTransverse):
        FVODESOlver.__init__(self,bry_strategy)
    
    def solve_conservative_without_outerloop(self,delta_t,delta_x,Q,V,cc=False):
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
    
    def solve_non_conservative_without_outerloop(self,eqid,delta_t,delta_x,Q,V,cc=False):
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
    def __init__(self,bry_strategy=FVTransverse):
        FVODESOlver.__init__(self,bry_strategy)