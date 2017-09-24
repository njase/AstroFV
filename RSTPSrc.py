from ODESolver import ODEExplicit, ODEImplicit
from TestRoot import AbstractSrc

class RSTPSrc(AbstractSrc):
    def __init__(self):        
        self.P = None
        self.P_star = None
        self.D = None
        self.V = None
        self.V_star = None
        self.M = None
        self.E = None
        self.U = None
        self.U_new = None
        
        self.D_eqid = 1
        self.M_eqid = 2
        self.E_eqid = 3 
    
    def factory(solver):
        solvers = {ODEExplicit:RSTPODEExplicitSrc, ODEImplicit:RSTPODEImplicitSrc}
        return solvers[solver]
    factory = staticmethod(factory)
    
    def calculate_source(self,eqid,delta_t,delta_x,j):
        if eqid == self.D_eqid:
            return self.calculate_density_source(delta_t, delta_x, j)
        elif eqid == self.M_eqid:
            return self.calculate_momentum_source(delta_t, delta_x, j)
        elif eqid == self.E_eqid:
            return self.calculate_energy_source(delta_t,delta_x,j)
        else:
            return 0
    
    def calculate_abc(self,eqid,delta_t,delta_x,j):
        if eqid == self.E_eqid:
            return self.calculate_energy_abc(delta_t,delta_x,j)
        else:
            return []
            
    def calculate_momentum_source(self,delta_t,delta_x,j):
        pass
    
    def calculate_density_source(self,delta_t,delta_x,j):
        pass
    
    def calculate_energy_source(self,delta_t,delta_x,j):
        pass
    
    def calculate_energy_abc(self,delta_t,delta_x,j):
        pass

class RSTPODEExplicitSrc(RSTPSrc):
    def __init__(self,params):
        RSTPSrc.__init__(self)
        self.gamma = params.gamma
    
    def calculate_momentum_source(self,delta_t,delta_x,j):
        mu = delta_t/delta_x
        S =  - mu*(self.P[j] - self.P[j-1])
        
        return S
    
    def calculate_energy_source(self,delta_t,delta_x,j):
        mu = delta_t/delta_x
        if self.U[j] != 0: #Take care of division by zero
            S = -(self.gamma-1) * (self.E[j]/self.U[j]) * (self.U_new[j]-self.U[j] + mu*(self.V[j+1]-self.V[j]))
        else:
            S = 0
        
        return S
    

class RSTPODEImplicitSrc(RSTPSrc):
    def __init__(self,params):
        RSTPSrc.__init__(self)
        self.alpha = params.alpha
        self.gamma = params.gamma        
    
    def calculate_density_source(self,delta_t,delta_x,j):
        if self.V[j] > 0:
            S = self.D[j]/delta_t - (1-self.alpha)*((self.D[j]*self.V[j+1]-self.D[j-1]*self.V[j])/delta_x)
        else:
            S = self.D[j]/delta_t - (1-self.alpha)*((self.D[j+1]*self.V[j+1]-self.D[j]*self.V[j])/delta_x)
        
        return S
    
    def calculate_momentum_source(self,delta_t,delta_x,j):
        Vi_avg = (self.V[j]+self.V[j-1])/2
        Vj_avg = (self.V[j]+self.V[j+1])/2 
                
        if Vj_avg > 0:
            S = self.M[j]/delta_t - (1-self.alpha)*((self.M[j]*Vj_avg-self.M[j-1]*Vi_avg)/delta_x) - self.alpha*((self.P_star[j]-self.P_star[j-1])/delta_x) - (1-self.alpha)*((self.P[j]-self.P[j-1])/delta_x)
        else:
            S = self.M[j]/delta_t - (1-self.alpha)*((self.M[j+1]*Vj_avg-self.M[j]*Vi_avg)/delta_x) - self.alpha*((self.P_star[j]-self.P_star[j-1])/delta_x) - (1-self.alpha)*((self.P[j]-self.P[j-1])/delta_x)
        
        return S
    
    def calculate_energy_source(self,delta_t,delta_x,j):
        if self.V[j] > 0:
            S = self.E[j]/delta_t - (1-self.alpha)*((self.E[j]*self.V[j+1]-self.E[j-1]*self.V[j])/delta_x)
        else:
            S = self.E[j]/delta_t - (1-self.alpha)*((self.E[j+1]*self.V[j+1]-self.E[j]*self.V[j])/delta_x) 
        
        return S
    
    
    def calculate_energy_abc(self,delta_t,delta_x,j):
        mu = delta_t*delta_x
        if self.V[j] > 0:
            c = 0
            b1 = (delta_x+self.alpha*self.V_star[j+1]*delta_t)/mu
            a = (-self.alpha*self.V_star[j])/delta_x
        else:
            c = (self.alpha*self.V_star[j+1])/delta_x
            b1 = (delta_x-self.alpha*self.V_star[j]*delta_t)/mu
            a = 0
        
        if self.U_new[j] != 0:
            b2 =  -(self.gamma-1)* (delta_x*(self.U_new[j]-self.U[j]) + delta_t*(self.V_star[j+1]-self.V_star[j])) / (self.U_new[j]*mu)
        else:
            b2 = 0
             
        b = b1+b2
        
        return [a,b,c]