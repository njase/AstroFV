from RSTP import RSTPTest, RSTPIV, RSTPBV, RSTPParams
from ODESolver import ODEExplicit
import sys,os


def main():
    #Read input
 
    params = RSTPParams() 
    params.gamma = 0
    params.cfl = 0.25
    iv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    bv = RSTPBV()
    #testlist = [RSTPTest(params,iv,bv,strategy=ODEExplicit)]
    testlist = [RSTPTest(params,iv,bv)]
    [test.solve() for test in testlist]

if __name__ == "__main__":
    main()

