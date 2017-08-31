from __future__ import division
from TestRoot import AbstractTest, Params
from IVBV_Root import InitialValues, BoundaryValues
from RSTPSrc import RSTPSrc
import numpy as np
import matplotlib.pyplot as plt


class RSTPExplicitParams(Params):
    def __init__(self,ncells,gamma=0,cfl=1.0):
        Params.__init__(self) 
        self.gamma = gamma
        self.cfl = cfl
        self.ncells = ncells
        self.fv_boundary_strategy = None
        #self.alpha is not defined

class RSTPImplicitParams(Params):
    def __init__(self,ncells,alpha,gamma=0):
        Params.__init__(self) 
        self.gamma = gamma
        self.ncells = ncells
        self.alpha = alpha
        self.fv_boundary_strategy = None        
        self.cfl = 0.40 #This parameter is not user defined
        
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
    def __init__(self,test_id,params,initval,bryval,ode_strategy=None):
        self.test_id = test_id
        self.params = params
        if ode_strategy:
            self.odesolver = ode_strategy(params)
        self.initval = initval
        self.bryval = bryval
        self.D_eqid = 1
        self.M_eqid = 2
        self.E_eqid = 3
        self.src = RSTPSrc.factory(ode_strategy)(self.params)

    def init_figures(self):
        self.fh_d = 1
        self.ax_d = plt.figure(self.fh_d).add_subplot(111)
        self.fh_v = 2
        self.ax_v = plt.figure(self.fh_v).add_subplot(111)
        self.fh_t = 3
        self.ax_t = plt.figure(self.fh_t).add_subplot(111)
        self.fh_u = 4
        self.ax_u = plt.figure(self.fh_u).add_subplot(111)
        self.fh_p = 5
        self.ax_p = plt.figure(self.fh_p).add_subplot(111)
                
    def plot_figures(self,t,D,V,U,P):
        self.ax_d.plot(D,label=str(t))
        self.ax_v.plot(V,label=str(t)) 
        #tau = 1./sqrt(identity_vec - (Vxn.^2))
        #ax_t.plot(tau)
        self.ax_u.plot(U,label=str(t))
        self.ax_p.plot(P,label=str(t))

    def save_figures(self):
        plt.figure(self.fh_d)
        self.ax_d.set_xlabel('x')
        self.ax_d.set_ylabel('D(x,t)')
        self.ax_d.set_title('Relativistic Density')
        plt.legend(loc=1)
        fpath = self.params.fpath + str(self.test_id) + '_D_img.png'
        plt.savefig(fpath)        
        plt.close(self.fh_d)
        
        plt.figure(self.fh_v)
        self.ax_v.set_xlabel('x')
        self.ax_v.set_ylabel('Vx(x,t)')
        self.ax_v.set_title('Velocity Vx')
        plt.legend(loc=1)
        fpath = self.params.fpath + str(self.test_id) + '_V_img.png'
        plt.savefig(fpath)
        plt.close(self.fh_v)
        
        #self.ax_t.set_xlabel('x')
        #self.ax_t.set_ylabel('Tau(x,t)')
        #plt.close(3)
        
        plt.figure(self.fh_u)
        self.ax_u.set_xlabel('x')
        self.ax_u.set_ylabel('Ut(x,t)')
        self.ax_u.set_title('Velocity Ut')
        plt.legend(loc=1)
        fpath = self.params.fpath + str(self.test_id) + '_U_img.png'
        plt.savefig(fpath)
        plt.close(self.fh_u)
        
        plt.figure(self.fh_p)
        self.ax_p.set_xlabel('x')
        self.ax_p.set_ylabel('P(x,t)')
        self.ax_p.set_title('Pressure')
        plt.legend(loc=1)
        fpath = self.params.fpath + str(self.test_id) + '_P_img.png'
        plt.savefig(fpath)
        plt.close(self.fh_p)
            
    def noStop(self):
        return False
    
    def solve(self,stopFunc=None,collect_cnt=10):    
        if stopFunc is None:
            stopFunc = self.noStop
            
        #Define grid
        delta_x = (self.params.xmax - self.params.xmin)/self.params.ncells
        numj = self.params.ncells + 1
        delta_t = self.params.cfl*delta_x
        nsteps = int((self.params.tmax-self.params.tmin)//delta_t) #Time steps
        
        #Set initial and boundary values
        Vxn = self.initval.get_init_Vx(numj)
        Mxn = self.initval.get_init_Mx(numj)
        Dn = self.initval.get_init_D(self.params.ncells)
        Rhon = self.initval.get_init_Rho(self.params.ncells)
        Pn = self.initval.get_init_P(self.params.ncells)
        Edn = self.initval.get_init_Ed(numj)

        #Stop condition - when shock wave is 90% close to end boundary
        xbreak = int(0.9*numj)-1
        break_sim = False
        
        #Figure and stat collection
        stats_counter = np.linspace(0,nsteps,collect_cnt,True,dtype=int)
        print("Stats collect at location" + str(stats_counter))
        col_index = 1 #Dont plot Initial condition (t=0)
        self.init_figures()
                        
        #Define source terms for the non-conservative equations
        #The equations are numbered as D = 1, M = 2, Ed = 3
        self.odesolver.set_src(self.D_eqid,self.src.calculate_density_source)
        self.odesolver.set_src(self.M_eqid,self.src.calculate_momentum_source)
        
        #Setup outer loop for time
        # Use Explicit solver to solve the 3 equations without loop
        # Do all the stuff
        for n in range(0,nsteps):
            if n%100 == 0:
                print('Simulation ongoing at n = ' + str(n))
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
                break_sim = True

            if (n == stats_counter[col_index] or break_sim) : 
                print("collecting stats for n = " + str(n))          
                t=n*delta_t
                self.plot_figures(t,Dn,Vxn,Utn,Pn)                
                col_index = col_index + 1

            if break_sim or stopFunc():
                print("Wave too close to boundary or simulation stopped")           
                break

        self.save_figures()        
        print("Simulation stopped")
    
    #Conservative equation solved in cell centered manner with Transvere boundary conditions
    def solve_density_eqn(self,Dn,Vx,delta_t,delta_x):
        self.src.D = Dn
        self.src.V = Vx
        D = self.odesolver.solve_conservative_without_outerloop(delta_t,delta_x,Dn,Vx,self.D_eqid,cc=True)
        return D
    
    def solve_momentum_eqn(self,Mxn,Vx,P,delta_t,delta_x):
        self.src.P = P 
        self.src.V = Vx
        self.src.M = Mxn
        M = self.odesolver.solve_non_conservative_without_outerloop(delta_t,delta_x,Mxn,Vx,self.M_eqid,cc=False)
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