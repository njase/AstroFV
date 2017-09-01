from RSTP import RSTPTest, RSTPIV, RSTPBV, RSTPExplicitParams, RSTPImplicitParams
from ODESolver import ODEExplicit, ODEImplicit , FVTransverse
import sys,os


def main():
    #Params for explicit solver    
    eparams = RSTPExplicitParams(400,0,0.25) 
    eparams.set_fig_path('./figs/')
    eparams.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    eiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ebv = RSTPBV()
    test_id = 2
    test_explicit = RSTPTest(test_id,eparams,eiv,ebv,ode_strategy=ODEExplicit)
    
    #Params for implicit solver
    iparams = RSTPImplicitParams(300,0.5,0.0)
    iparams.set_fig_path('./figs/')
    iparams.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    iiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ibv = RSTPBV()
    test_id = 1
    test_implicit = RSTPTest(test_id,iparams,iiv,ibv,ode_strategy=ODEImplicit)
    
    #testlist = [test_explicit,test_implicit]
    testlist = [test_implicit]
    [test.solve(collect_cnt=5) for test in testlist]
    

if __name__ == "__main__":
    main()

