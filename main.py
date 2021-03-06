from __future__ import division
from RSTP import RSTPTest, RSTPIV, RSTPBV, RSTPExplicitParams, RSTPImplicitParams
from ODESolver import ODEExplicit, ODEImplicit , FVTransverse


def main():
    #Params for explicit solver    
    eparams = RSTPExplicitParams(500,0,0.25) 
    eparams.set_fig_path('./figs/')
    eparams.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    eiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ebv = RSTPBV()
    test_id = 1
    test_explicit_0 = RSTPTest(test_id,eparams,eiv,ebv,ode_strategy=ODEExplicit)

    eparams = RSTPExplicitParams(500,4/3,0.25) 
    eparams.set_fig_path('./figs/')
    eparams.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    eiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ebv = RSTPBV()
    test_id = 2
    test_explicit_1 = RSTPTest(test_id,eparams,eiv,ebv,ode_strategy=ODEExplicit)
        
    #Params for implicit solver
    iparams = RSTPImplicitParams(500,1.0,0.0,2,0.7)
    iparams.set_fig_path('./figs/')
    iparams.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    iiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ibv = RSTPBV()
    test_id = 3
    test_implicit_0 = RSTPTest(test_id,iparams,iiv,ibv,ode_strategy=ODEImplicit)
    
    iparams = RSTPImplicitParams(500,1.0,4/3,2,0.7)
    iparams.set_fig_path('./figs/')
    iparams.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    iiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ibv = RSTPBV()
    test_id = 4
    test_implicit_1 = RSTPTest(test_id,iparams,iiv,ibv,ode_strategy=ODEImplicit)
        
    testlist = [test_explicit_0,test_explicit_1,test_implicit_0,test_implicit_1]
    #testlist = [test_implicit_1]
    [test.solve(collect_cnt=10) for test in testlist]
    

if __name__ == "__main__":
    main()

