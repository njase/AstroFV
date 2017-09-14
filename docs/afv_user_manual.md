As a user, you can use [AstroFV](https://njase.github.io/AstroFV/) to perform simulation of an astrophysical application.
The following simulations are currently supported. Please click on the relevant one:
1. [Relativistic Shock Tube Problem (RSTP)](#RSTP) in 1-D

## RSTP
1. **Introduction**

Astrophysical scenarios involving relativistic flows occur in several phenomenon, most notably in the jets in extragalactic radio sources associated with active galactic nuclei. Similar to shock wave phenomenon in classical Newtonian fluid mechanics, strong shocks are a common feature in
such astrophysical scenarios. Numerical simulations are therefore needed to study the formation, evolution and interaction of shock waves in relativistic fluids.

Relativistic shock tube problem (RSTP) involves the decay of an initially discontinuous two fluids into three elementary wave structures:
a shock, a contact, and a rarefaction wave.

2. **Governing Equations**

This application considers the hydrodynamics model of a perfect fluid. The model is thus given by the hyperbolic system of conservation
laws of the relativistic hydrodynamics.

Following [Hujeirat](https://arxiv.org/abs/0903.3025) and [Font] (https://arxiv.org/abs/gr-qc/0003101), the 1-dimensional hydrodynamical system in Minkowski space can be reformulated in terms of dynamical variables
<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;$D,&space;M_{x},&space;E_{d}$" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;$D,&space;M_{\mu},&space;E_{d}$" title="$D, M_{\mu}, E_{d}$" /></a>
as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\frac{\partial&space;D}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(DV^{x})}{\partial&space;x}&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\frac{\partial&space;D}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(DV^{x})}{\partial&space;x}&space;=&space;0" title="\frac{\partial D}{\partial t} + \frac{\partial (DV^{x})}{\partial x} = 0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\frac{M_{x}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(M_{x}V^{x})}{\partial&space;x}&space;=&space;-\frac{\partial&space;P}{\partial&space;x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\frac{M_{x}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(M_{x}V^{x})}{\partial&space;x}&space;=&space;-\frac{\partial&space;P}{\partial&space;x}" title="\frac{M_{x}}{\partial t} + \frac{\partial (M_{x}V^{x})}{\partial x} = -\frac{\partial P}{\partial x}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\frac{E^{d}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(E^{d}V^{x})}{\partial&space;x}&space;=&space;-(\gamma&space;-&space;1)\frac{E^d}{u^t}&space;\lbrack&space;\frac{\partial&space;u^t}{t}&space;&plus;&space;\frac{\partial&space;^x}{\partial&space;x}\rbrack" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\frac{E^{d}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(E^{d}V^{x})}{\partial&space;x}&space;=&space;-(\gamma&space;-&space;1)\frac{E^d}{u^t}&space;\lbrack&space;\frac{\partial&space;u^t}{t}&space;&plus;&space;\frac{\partial&space;^x}{\partial&space;x}\rbrack" title="\frac{E^{d}}{\partial t} + \frac{\partial (E^{d}V^{x})}{\partial x} = -(\gamma - 1)\frac{E^d}{u^t} \lbrack \frac{\partial u^t}{t} + \frac{\partial ^x}{\partial x}\rbrack" /></a>

where we define

<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;D&space;=&space;\rho&space;u^t" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;D&space;=&space;\rho&space;u^t" title="D = \rho u^t" /></a>
 = Relativistic Density
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;M_{x}&space;=&space;\rho&space;h&space;u_{x}u^t" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;M_{x}&space;=&space;\rho&space;h&space;u_{x}u^t" title="M_{x} = \rho h u_{x}u^t" /></a>
 = Momentum
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;E^{d}&space;=&space;\rho&space;\epsilon&space;u^t" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;E^{d}&space;=&space;\rho&space;\epsilon&space;u^t" title="E^{d} = \rho \epsilon u^t" /></a>
 = Total energy (assuming conservation of mechanical energy)
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;V^x&space;=&space;\frac{u^x}{u^t}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;V^x&space;=&space;\frac{u^x}{u^t}" title="V^x = \frac{u^x}{u^t}" /></a>
 = Transport Velocity
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\sqrt{-g}&space;=&space;1" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\sqrt{-g}&space;=&space;1" title="\sqrt{-g} = 1" /></a>
   in Minkowski space
 
 <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;u^{\mu}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;u^{\mu}" title="u^{\mu}" /></a>
  = four-velocity of the fluid
  
 <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\rho" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\rho" title="\rho" /></a>
  = rest mass density in locally intertial reference frame
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;h&space;=&space;1&space;&plus;&space;\epsilon&space;&plus;&space;\frac{p}{\rho}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;h&space;=&space;1&space;&plus;&space;\epsilon&space;&plus;&space;\frac{p}{\rho}" title="h = 1 + \epsilon + \frac{p}{\rho}" /></a>
   = relativistic specific enthalpy
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\epsilon" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\epsilon" title="\epsilon" /></a>
   = specific internal energy
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;p&space;&&space;=&space;$(\gamma&space;-&space;1)\rho&space;\epsilon" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;p&space;&&space;=&space;$(\gamma&space;-&space;1)\rho&space;\epsilon" title="p & = $(\gamma - 1)\rho \epsilon" /></a>
   = pressure of ideal gas
  
The above equations are the desired equations which can be solved for the following cases:
* **Adiabatic conditions**
  * isothermal gas (specified with gamma = 0)
  * non-isothermal gas with gamma = User defined (practically 4/3, 5/3, 2)
* **Initial conditions**
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\rho_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\rho_{init}" title="\rho_{init}" /></a>
     = User input
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space; p_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;p_{init}" title="p_{init}" /></a>
      = User input
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;D_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;D_{init}" title="D_{init}" /></a>
      = User input
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;M^{x}_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;M^{x}_{init}" title="M^{x}_{init}" /></a>
      = User input
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;V^{x}_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;V^{x}_{init}" title="V^{x}_{init}" /></a>
      = User input
  * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;E^{d}_{init}&space;=&space;\frac{p_{init}}{\gamma&space;-&space;1}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;E^{d}_{init}&space;=&space;\frac{p_{init}}{\gamma&space;-&space;1}" title="E^{d}_{init} = \frac{p_{init}}{\gamma - 1}" /></a>
  
 ## Remarks
 * The hydrodynamical system represents a coupled set of advection equations
 * If fluid is considered isothermal, h~1 and the equation in E should be ignored (need not solved)
 * Dh = D + <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\gamma&space;E^d" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\gamma&space;E^d" title="\gamma E^d" /></a> for non-isothermal case
 * Dh ~ D for isothermal case
 * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;M_{t}^2&space;=&space;M_{x}^2&space;&plus;&space;(Dh)^2" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;M_{t}^2&space;=&space;M_{x}^2&space;&plus;&space;(Dh)^2" title="M_{t}^2 = M_{x}^2 + (Dh)^2" /></a>
 * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;u^{t}&space;=&space;\frac{M_{t}}{Dh}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;u^{t}&space;=&space;\frac{M_{t}}{Dh}" title="u^{t} = \frac{M_{t}}{Dh}" /></a>
 * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;u^{x}&space;=&space;\frac{M_{x}}{Dh}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;u^{x}&space;=&space;\frac{M_{x}}{Dh}" title="u^{x} = \frac{M_{x}}{Dh}" /></a>
 * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;V^{x}&space;=&space;\frac{u^{x}}{u^{t}}&space;=&space;\frac{M_{x}}{M_{t}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;V^{x}&space;=&space;\frac{u^{x}}{u^{t}}&space;=&space;\frac{M_{x}}{M_{t}}" title="V^{x} = \frac{u^{x}}{u^{t}} = \frac{M_{x}}{M_{t}}" /></a>
 * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\rho&space;=&space;\frac{D}{u^{t}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\rho&space;=&space;\frac{D}{u^{t}}" title="\rho = \frac{D}{u^{t}}" /></a>
 * <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;p&space;=&space;\frac{E^{d}(\gamma-1)}{u^{t}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;p&space;=&space;\frac{E^{d}(\gamma-1)}{u^{t}}" title="p = \frac{E^{d}(\gamma-1)}{u^{t}}" /></a>
 * To get <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;E^{d}_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;E^{d}_{init}" title="E^{d}_{init}" /></a>
    we have used that 
    
    <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;E^{d}&space;=&space;\frac{u^{t}p}{(\gamma&space;-&space;1)}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;E^{d}&space;=&space;\frac{u^{t}p}{(\gamma&space;-&space;1)}" title="E^{d} = \frac{u^{t}p}{(\gamma - 1)}" /></a>
    and 
    <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;u^{t}&space;=&space;\frac{M^{t}}{Dh}&space;=&space;\frac{\sqrt{M_{x}^2&plus;(Dh)^2}}{Dh}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;u^{t}&space;=&space;\frac{M^{t}}{Dh}&space;=&space;\frac{\sqrt{M_{x}^2&plus;(Dh)^2}}{Dh}" title="u^{t} = \frac{M^{t}}{Dh} = \frac{\sqrt{M_{x}^2+(Dh)^2}}{Dh}" /></a>
    
3. **Key Data structures**

      3.1 Parameters
```python
 class RSTPExplicitParams(Params):
    def __init__(self,ncells,gamma=0,cfl=1.0):
        Params.__init__(self,"explicit") 
        self.gamma = gamma
        self.cfl = cfl
        self.ncells = ncells
        self.fv_boundary_strategy = None
   
  class RSTPImplicitParams(Params):
    def __init__(self,ncells,alpha,gamma=0):
        Params.__init__(self,"implicit") 
        self.gamma = gamma
        self.ncells = ncells
        self.alpha = alpha
        self.fv_boundary_strategy = None        
        self.cfl = 0.30 #This parameter is not user defined
 ```
 These is used to define parameters for Explicit Euler time integration and Implicit/Crank-nicholson time integration. 
 
 gamma = 0 defines isothermal gas
 
 Time limits are default [0,1] and spatial limits are default [0,1]
 
 Example:
 ```python
  eparams = RSTPExplicitParams(1000,0,0.25) #isothermal gas, CFL=0.25
  iparams_1 = RSTPImplicitParams(1000,1.0,0.0) #isothermal gas, Implicit Euler solver
  iparams_2 = RSTPImplicitParams(1000,0.5,5/2) #non-isothermal gas, Crnk-Nicholson solver  
 ```
     3.2 Initial Values
  ```python
   class RSTPIV(InitialValues):
    def __init__(self,Vx,Mx,D,Rho):
        self.Vx = Vx
        self.Mx = Mx
        self.D = D
        self.Rho = Rho
  ```
 Used to provide initial values. The initial values are provided as a list for the two discontinuous fluids.
 
 Example:
 ```python
  iv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
 
 ```
4. **Usage examples**
###### Solve RSTP with Explicit Euler technique
Number of FV cells = 1000, gamma = 4/3, CFL = 0.25
```python
    eparams = RSTPExplicitParams(1000,4/3,0.25) 
    eparams.set_fig_path('./figs/')
    eparams.fv_boundary_strategy = FVTransverse #Default 
    eiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ebv = RSTPBV()
    test_explicit = RSTPTest(1,eparams,eiv,ebv,ode_strategy=ODEExplicit)
    test_explicit.solve()
```

###### Solve RSTP with Implicit Euler technique
Number of FV cells = 1000, gamma = 5/3
```python
    iparams = RSTPImplicitParams(1000,1.0,5/3)
    iparams.set_fig_path('./figs/')
    iparams.fv_boundary_strategy = FVTransverse #Default 
    iiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ibv = RSTPBV()
    test_implicit = RSTPTest(2,iparams,iiv,ibv,ode_strategy=ODEImplicit)
    test_implicit.solve()
```

###### Solve RSTP with Crank-Niholson technique
Number of FV cells = 1000, gamma = 0 (isothermal)
```python
    iparams = RSTPImplicitParams(1000,0.5,0)
    iparams.set_fig_path('./figs/')
    iparams.fv_boundary_strategy = FVTransverse #Default 
    iiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
    ibv = RSTPBV()
    test_implicit = RSTPTest(3,iparams,iiv,ibv,ode_strategy=ODEImplicit)
    test_implicit.solve()
```
#### Output
The output is generated as a set of 4 image files in the same directory as provided in set_fig_path() API.

The 4 image files correspond to plot of spatial variable x against Density (D), Pressure(P), time-like velocity (<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;u^{t}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;u^{t}" title="u^{t}" /></a>) and Transport Velocity (<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;V^x" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;V^x" title="V^x" /></a>) respectively

5. **Solver basics**
TBD. Currently see [Developer manual](afv_developer_manual.md)
