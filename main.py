from RSTP import RSTPTest, RSTPIV, RSTPBV, RSTPExplicitParams, RSTPImplicitParams
from ODESolver import ODEExplicit, ODEImplicit , FVTransverse
import sys,os


def main():
    #Read input from external source like DB
 
    #Params for explicit solver    
    params = RSTPExplicitParams() 
    params.gamma = 0
    params.cfl = 0.25
    params.fv_boundary_strategy = FVTransverse #Default, may also be skipped 
    iv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    bv = RSTPBV()
    testlist = [RSTPTest(params,iv,bv,ode_strategy=ODEExplicit)]    
    [test.solve() for test in testlist]

    #Params for implicit solver
#     params = RSTPImplicitParams()
#     params.gamma = 0
#     params.fv_boundary_strategy = FVTransverse #Default, may also be skipped
#     iv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
#     bv = RSTPBV()
#     testlist = [RSTPTest(params,iv,bv,ode_strategy=ODEImplicit)]
#     [test.solve() for test in testlist]
    

if __name__ == "__main__":
    main()

