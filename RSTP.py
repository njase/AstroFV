from __future__ import division
from TestRoot import AbstractTest, Params
from IVBV_Root import InitialValues, BoundaryValues
from RSTPSrc import RSTPSrc
import numpy as np
import matplotlib.pyplot as plt


class RSTPExplicitParams(Params):
    def __init__(self,ncells,gamma=0,cfl=1.0):
        Params.__init__(self,"explicit") 
        self.gamma = gamma
        self.cfl = cfl
        self.ncells = ncells
        self.fv_boundary_strategy = None
        #self.alpha is NA and not defined

class RSTPImplicitParams(Params):
    def __init__(self,ncells,alpha,gamma=0,iter_count=1,cfl=0.50):
        Params.__init__(self,"implicit") 
        self.gamma = gamma
        self.ncells = ncells
        self.alpha = alpha
        self.fv_boundary_strategy = None        
        self.cfl = cfl #This parameter is typically not user defined
        self.iter_count = iter_count
        
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
            self.src = RSTPSrc.factory(ode_strategy)(self.params)
            self.odesolver.set_src(self.src)
        self.initval = initval
        self.bryval = bryval
        self.D_eqid = 1
        self.M_eqid = 2
        self.E_eqid = 3        

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
        self.ax_v.set_title('Transport Velocity Vx')
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
        self.ax_u.set_title('Lorentz Factor Ut')
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
        ###For debugging
        rstp_debug = False
        
        if rstp_debug == True:
            f = open("op_"+str(self.test_id)+".log",'w')
        else:
            f = None
        
        if stopFunc is None:
            stopFunc = self.noStop
            
        #Define grid
        delta_x = (self.params.xmax - self.params.xmin)/self.params.ncells
        numj = self.params.ncells + 1
        delta_t = self.params.cfl*delta_x
        nsteps = int((self.params.tmax-self.params.tmin)//delta_t) #Time steps
        print('Total number of time steps = '+str(nsteps))
        
        #Set initial and boundary values
        Vxn = self.initval.get_init_Vx(numj)
        Mxn = self.initval.get_init_Mx(numj)
        Dn = self.initval.get_init_D(self.params.ncells)
        Rhon = self.initval.get_init_Rho(self.params.ncells)
        Pn = self.initval.get_init_P(self.params.ncells)
        Edn = self.initval.get_init_Ed(self.params.ncells)
        if self.params.gamma != 0:
            Edn[0:] = Pn/(self.params.gamma-1)
            
        Utn = np.zeros(numj)
        Vxn_iter = Vxn
        Pn_iter = Pn
        
        #For Extrapolation using last 5 values
        Ut_old = np.zeros((5,numj))
        pdegree = 2

        #Stop condition - when shock wave is 90% close to end boundary
        xbreak = int(0.9*numj)-1
        break_sim = False
        
        #Figure and stat collection
        stats_counter = np.linspace(0,nsteps,collect_cnt,True,dtype=int)
        print("Stats will be collected at " + str(stats_counter))
        col_index = 1 #Dont plot Initial condition (t=0)
        self.init_figures()
                        
        #Setup outer loop for time
        # Use solver to solve the 3 equations without loop
        for n in range(0,nsteps):
            if n%100 == 0:
                print('\n' + 'Simulation ongoing at n = ' + str(n))
                
            if f:
                f.write('Simulation ongoing at n = ' + str(n) + '\n')
                f.write('Before iteration' + '\n')
                f.write('D = ' + str(Dn) + '\n')
                f.write('V = ' + str(Vxn) + '\n')
                f.write('M = ' + str(Mxn) + '\n')
                f.write('E = ' + str(Edn) + '\n')
            
            for sub_iter in range(0,self.params.iter_count):
                #print 'Sub iteration = ' + str(sub_iter), #progress bar                
                
                #Solve first equation
                self.src.D = Dn
                self.src.V = Vxn
                Dn_1 = self.solve_density_eqn(Dn,Vxn_iter,delta_t,delta_x)
            
                #Solve second equation
                self.src.P = Pn
                self.src.P_star = Pn_iter
                self.src.V = Vxn
                self.src.M = Mxn
                Mxn_1 = self.solve_momentum_eqn(Mxn,Vxn_iter,Pn_iter,delta_t,delta_x)
            
                #Solve third equation
                if self.params.gamma != 0: #isothermal case
                    # Predict Ut(n+1)
                    Ut_fut = self.predict_Ut(Ut_old,pdegree)
                    print '.', #progress bar
                    
                    self.src.E = Edn
                    self.src.V = Vxn
                    self.src.V_star = Vxn_iter
                    self.src.U = Utn
                    self.src.U_new = Ut_fut
                    Edn_1 = self.solve_energy_eqn(Edn,Vxn_iter,Utn,Ut_fut,delta_t,delta_x)
                else:
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
                
                #Prepare for sub-iteration or iteration (if loop ends)
                Vxn_iter = Vxn_1
                Pn_iter = Pn_1

            Dn = Dn_1
            Mxn = Mxn_1
            Rhon = Rhon_1
            Vxn = Vxn_1
            #Vxn_iter = Vxn_1
            Utn = Utn_1
            Pn = Pn_1
            #Pn_iter = Pn_1
            Edn = Edn_1
            Ut_old[0:-1,:] = Ut_old[1:,:]
            Ut_old[-1,:] = Utn_1
            
            
            if f:
                f.write('After iteration' + '\n')
                f.write('D = ' + str(Dn) + '\n')
                f.write('V = ' + str(Vxn) + '\n')
                f.write('M = ' + str(Mxn) + '\n')
                f.write('E = ' + str(Edn) + '\n')
            
            # If shock wave is close to the boundary, stop!
            if abs(Utn[xbreak]-min(Utn)) > 0.1:
                break_sim = True

            if (n == stats_counter[col_index] or break_sim) : 
                print('\n' + 'collecting stats for n = ' + str(n))          
                t=n*delta_t
                self.plot_figures(t,Dn,Vxn,Utn,Pn)                
                col_index = col_index + 1

            if break_sim or stopFunc():
                print('\n' + 'Wave too close to boundary or simulation stopped')           
                break

        self.save_figures()        
        print('\n' + 'Simulation stopped')
        if f:
            f.close()
    
    #Conservative equation solved in cell centered manner with Transvere boundary conditions
    def solve_density_eqn(self,Dn,Vx,delta_t,delta_x):        
        D = self.odesolver.solve_conservative_without_outerloop(delta_t,delta_x,Dn,Vx,self.D_eqid,cc=True)
        return D
    
    def solve_momentum_eqn(self,Mxn,Vx,P,delta_t,delta_x):
        M = self.odesolver.solve_non_conservative_without_outerloop(delta_t,delta_x,Mxn,Vx,self.M_eqid,cc=False)
        return M
    
    def predict_Ut(self,Ut_old,pdeg):
        [xsize,numj] = np.shape(Ut_old)    
        Ut_new = np.zeros(numj)
        x = np.arange(1,xsize+1)
        for n in range(numj):        
            p = np.polyfit(x, Ut_old[:,n],pdeg)
            Ut_new[n] = np.polyval(p,xsize+1)
        
        return Ut_new
    
    
    def solve_energy_eqn(self,Edn,Vx,Ut,Ut_fut,delta_t,delta_x):
        if self.odesolver.get_name() == "implicit":
            E = self.odesolver.solve_user_defined_without_outerloop(self.params.ncells,delta_t,delta_x,self.E_eqid,cc=True)
        else:
            E = self.odesolver.solve_non_conservative_without_outerloop(delta_t,delta_x,Edn,Vx,self.E_eqid,cc=True)
        return E

    def calculate_Dh(self,gamma,D,Ed):
        if gamma == 0:
            Dh = D
        else:
            ncells = len(D)
            Dh = D + gamma*Ed[:ncells]
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
            P = (gamma-1)*np.divide(Ed,Ut[:-1])
            P[P==np.inf] = 0 #Take care of inf = division by zero
        return P