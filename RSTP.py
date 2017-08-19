from __future__ import division
from TestRoot import AbstractTest, Params
from IVBV_Root import InitialValues, BoundaryValues
import numpy as np


class RSTPParams(Params):
    def __init__(self):
        Params.__init__(self) 
        self.gamma = 0
        self.cfl = 0.25
        self.ncells = 10


class RSTPIV(InitialValues):
    def __init__(self,Vx,Mx,D,Rho):
        self.Vx = Vx
        self.Mx = Mx
        self.D = D
        self.Rho = Rho

    def distribute_init(self,N,var):
        mid = N//2
        a = np.full((mid),var[0],float)
        b = np.full((N-mid),var[1],float)
        return np.concatenate((a,b))
        
    def get_init_Vx(self,N):
        return self.distribute_init(N,self.Vx)

    def get_init_Mx(self,N):
        return self.distribute_init(N,self.Mx)

    def get_init_D(self,N):
        return self.distribute_init(N,self.D)

    def get_init_Rho(self,N):
        return self.distribute_init(N,self.Rho)

    #P_init = Rho_init
    def get_init_P(self,N):
        return self.distribute_init(N,self.Rho)

    def get_init_Ed(self,N):
        return np.zeros(N)

class RSTPBV(BoundaryValues):
    def __init__(self):
        pass    

    def distribute_bry(self,N,var):
        pass


class RSTPTest(AbstractTest):
    '''
      ode_strategy = implicit/explicit
    '''
    def __init__(self,params,initval,bryval,ode_strategy=None):
        self.params = params
        #self.odesolver = ode_strategy
        self.initval = initval
        self.bryval = bryval

    def solve(self):
        delta_x = (self.params.xmax - self.params.xmin)/self.params.ncells
        numj = self.params.ncells + 1
        delta_t = self.params.cfl*delta_x
        nsteps = int((self.params.tmax-self.params.tmin)//delta_t) #Time steps

        Vxn = self.initval.get_init_Vx(numj)
        Mxn = self.initval.get_init_Mx(numj)
        Dn = self.initval.get_init_D(self.params.ncells)
        Rhon = self.initval.get_init_Rho(numj)
        Pn = self.initval.get_init_P(numj)
        Edn = self.initval.get_init_Ed(numj)

        identity_vec = np.ones(numj)

        #for breaking simulation - when shock wave is 90% close to end boundary
        xbreak = int(0.9*numj)-1
        #break_sim = False

        print("Simulation started for " + str(self.params.gamma))
 
        for n in range(0,nsteps):
            print(n)
            Dn_1 = self.solve_density_eqn(Dn,Vxn,delta_t,delta_x)
            Mxn_1 = self.solve_momentum_eqn(Mxn,Vxn,Pn,delta_t,delta_x)
            Edn_1 = Edn
            
            ### Update phase        
            Dh = self.calculate_Dh(self.params.gamma,Dn_1,Edn_1)
            Mt = self.calculate_Mt(Dh,Mxn_1)

            #update Ut
            Utn_1 = self.update_Ut(Dh,Mt)

            #Update Vx    
            Vxn_1 = self.update_Vx(Mxn_1,Mt)

            #Update density
            Rhon_1 = self.update_rho(Dn_1,Utn_1)

            #Update pressure
            Pn_1 = self.update_pressure(self.params.gamma,Rhon_1,Edn_1,Utn_1)

            Dn = Dn_1
            Mxn = Mxn_1
            Rhon = Rhon_1
            Vxn = Vxn_1
            Utn = Utn_1
            Pn = Pn_1
            Edn = Edn_1

            # If shock wave is close to the boundary, stop!
            if abs(Utn[xbreak]-min(Utn)) > 0.1:
                #break_sim = True
                break

        print("Simulation stopped")
        
    def solve_density_eqn(self,Dn,Vx,delta_t,delta_x):
        print(Dn)
        numj  = len(Dn)
        D = np.zeros_like(Dn)
        mu = delta_t/delta_x
        #take care of boundary for stability reasons in upwind
        for j in range(1,numj-1): 
            if Vx[j] > 0:
                D[j] = Dn[j] - mu*(Dn[j]*Vx[j+1] - Dn[j-1]*Vx[j])
            else:
                D[j] = Dn[j] - mu*(Dn[j+1]*Vx[j+1] - Dn[j]*Vx[j])
        #Transverse boundary
        D[0] = D[1];
        D[-1] = D[-2]
        return D

    def solve_momentum_eqn(self,Mxn,Vx,P,delta_t,delta_x):
        numj  = len(Mxn)
        M = np.zeros_like(Mxn)
        mu = delta_t/delta_x
        for j in range(1,numj-2):
            Vxi_avg = (Vx[j]+Vx[j-1])/2
            Vxj_avg = (Vx[j]+Vx[j+1])/2        
            if Vxj_avg > 0:
                M[j] = Mxn[j] - mu*(Mxn[j]*Vxj_avg - Mxn[j-1]*Vxi_avg) - mu*(P[j]-P[j-1])
            else:
                M[j] = Mxn[j] - mu*(Mxn[j+1]*Vxj_avg - Mxn[j]*Vxi_avg) - mu*(P[j]-P[j-1])
        #Transverse boundary
        M[0] = M[1]
        M[-1] = M[-2]
        return M


    def calculate_Dh(self,gamma,D,Ed):
        if gamma == 0:
            Dh = D
        else:
            ncells = len(D)
            #Dh = D + gamma*Ed(1:ncells)
        return Dh
    
    def calculate_Mt(self,Dh,Mx):    
        ncells = len(Dh)
        Mt = np.zeros_like(Mx)
        Mt[0:ncells] = np.sqrt(np.square(Dh) + np.square(Mx[0:ncells]))
        Mt[-1] = Mt[-2]
        return Mt

    def update_Ut(self,Dh,Mt):
        ncells = len(Dh)
        Ut = np.zeros_like(Mt)
        Ut[0:ncells] = np.divide(Mt[0:ncells],Dh)
        Ut[-1] = Ut[-2]  #we will not allow the simulation to reach the end of boundary, so its safe
        return Ut


    def update_Vx(self,Mx,Mt):
        Vx = np.divide(Mx,Mt)
        Vx[Vx==np.inf] = 0 #Take care of inf = division by zero
        return Vx


    def update_rho(self,D,Ut):
        ncells = len(D)
        rho = np.zeros_like(Ut)
        rho[0:ncells] = np.divide(D,Ut[0:ncells])
        rho[rho==np.inf] = 0 #Take care of inf = division by zero
        rho[-1] = rho[-2]
        return rho


    def update_pressure(self,gamma,rho,Ed,Ut):
        if gamma == 0: #isothermal case
            P = rho
        else:        
            P = (gamma-1)*np.divide(Ed/Ut)
            P[P==np.inf] = 0 #Take care of inf = division by zero
        return P