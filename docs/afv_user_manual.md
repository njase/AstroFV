As a user, you can use [AstroFV](https://njase.github.io/AstroFV/) to perform simulation of an astrophysical application.
The following simulations are currently supported. Please click on the relevant one:
1. [Relativistic Shock Tube Problem (RSTP)](#RSTP) in 1-D

## RSTP
**Introduction**

   Astrophysical scenarios involving relativistic flows occur in several phenomenon, most notably in the jets in extragalactic radio sources associated with active galactic nuclei. Similar to shock wave phenomenon in classical Newtonian fluid mechanics, strong shocks are a common feature in such astrophysical scenarios. Numerical simulations are therefore needed to study the formation, evolution and interaction of shock waves in relativistic fluids.

   Relativistic shock tube problem (RSTP) involves the decay of an initially discontinuous two fluids into three elementary wave   structures: a shock, a contact, and a rarefaction wave.
 
**Governing Equations**

   This application considers the hydrodynamics model of a perfect fluid. The model is thus given by the hyperbolic system of conservation laws of the relativistic hydrodynamics.

   Following [Hujeirat](https://arxiv.org/abs/0903.3025) and [Font](https://arxiv.org/abs/gr-qc/0003101), the 1-dimensional hydrodynamical system in Minkowski space can be reformulated in terms of dynamical variables <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;$D,&space;M_{x},&space;E_{d}$" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;$D,&space;M_{\mu},&space;E_{d}$" title="$D, M_{\mu}, E_{d}$" /></a> as:

   <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\frac{\partial&space;D}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(DV^{x})}{\partial&space;x}&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\frac{\partial&space;D}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(DV^{x})}{\partial&space;x}&space;=&space;0" title="\frac{\partial D}{\partial t} + \frac{\partial (DV^{x})}{\partial x} = 0" /></a>

   <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\frac{M_{x}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(M_{x}V^{x})}{\partial&space;x}&space;=&space;-\frac{\partial&space;P}{\partial&space;x}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\frac{M_{x}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(M_{x}V^{x})}{\partial&space;x}&space;=&space;-\frac{\partial&space;P}{\partial&space;x}" title="\frac{M_{x}}{\partial t} + \frac{\partial (M_{x}V^{x})}{\partial x} = -\frac{\partial P}{\partial x}" /></a>

   <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\frac{E^{d}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(E^{d}V^{x})}{\partial&space;x}&space;=&space;-(\gamma&space;-&space;1)\frac{E^d}{u^t}&space;\lbrack&space;\frac{\partial&space;u^t}{t}&space;&plus;&space;\frac{\partial&space;^x}{\partial&space;x}\rbrack" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\frac{E^{d}}{\partial&space;t}&space;&plus;&space;\frac{\partial&space;(E^{d}V^{x})}{\partial&space;x}&space;=&space;-(\gamma&space;-&space;1)\frac{E^d}{u^t}&space;\lbrack&space;\frac{\partial&space;u^t}{t}&space;&plus;&space;\frac{\partial&space;^x}{\partial&space;x}\rbrack" title="\frac{E^{d}}{\partial t} + \frac{\partial (E^{d}V^{x})}{\partial x} = -(\gamma - 1)\frac{E^d}{u^t} \lbrack \frac{\partial u^t}{t} + \frac{\partial V^x}{\partial x}\rbrack" /></a>

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
   
     <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\rho_{init}" target="_blank"><img   src="https://latex.codecogs.com/png.latex?\bg_white&space;\rho_{init}" title="\rho_{init}" /></a>
       = User input
       
     <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space; p_{init}" target="_blank"><img  src="https://latex.codecogs.com/png.latex?\bg_white&space;p_{init}" title="p_{init}" /></a>
       = User input
       
     <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;D_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;D_{init}" title="D_{init}" /></a>
       = User input
       
     <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;M^{x}_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;M^{x}_{init}" title="M^{x}_{init}" /></a>
       = User input
       
     <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;V^{x}_{init}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;V^{x}_{init}" title="V^{x}_{init}" /></a>
       = User input
       
     <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;E^{d}_{init}&space;=&space;\frac{p_{init}}{\gamma&space;-&space;1}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;E^{d}_{init}&space;=&space;\frac{p_{init}}{\gamma&space;-&space;1}" title="E^{d}_{init} = \frac{p_{init}}{\gamma - 1}" /></a>

  
   * **Remarks** 
     * The hydrodynamical system represents a coupled set of non-linear advection equations
     * If fluid is considered isothermal, h~1 and the equation in E should be ignored (need not solved)
     * For non-isothermal case, Dh = D + <a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;\gamma&space;E^d" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;\gamma&space;E^d" title="\gamma E^d" /></a>
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

**Numerical techniques**

##### Spatial discretization 
Using first order upwinding with constant grid size

##### Temporal discretization
Constant grid size is used

We use cell centered FV discretization for Density and Momentum conservation and vertex centered FV discretization  for Total energy. This is shown below
(images/fv_cells.jpeg)

For vertex centered approach, the transport velocity at FV cell surface is taken as the mean value across the boundary. i.e

<a href="https://www.codecogs.com/eqnedit.php?latex=\qquad&space;\langle&space;V_{j-1}^x&space;\rangle&space;=&space;\frac{V_{j-1}^x&space;&plus;&space;V_{j}^x}{2}&space;\qquad&space;\langle&space;V_{j}^x&space;\rangle&space;=&space;\frac{V_{j}^x&space;&plus;&space;V_{j&plus;1}^x}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\qquad&space;\langle&space;V_{j-1}^x&space;\rangle&space;=&space;\frac{V_{j-1}^x&space;&plus;&space;V_{j}^x}{2}&space;\qquad&space;\langle&space;V_{j}^x&space;\rangle&space;=&space;\frac{V_{j}^x&space;&plus;&space;V_{j&plus;1}^x}{2}" title="\qquad \langle V_{j-1}^x \rangle = \frac{V_{j-1}^x + V_{j}^x}{2} \qquad \langle V_{j}^x \rangle = \frac{V_{j}^x + V_{j+1}^x}{2}" /></a>

The upwind flux across the FV cell surfaces is defined as:

<a href="https://www.codecogs.com/eqnedit.php?latex=D_{j}^{up}&space;=&space;\begin{cases}&space;D_{j}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;\leq&space;0&space;\\&space;D_{j-1}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;>&space;0&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{j}^{up}&space;=&space;\begin{cases}&space;D_{j}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;\leq&space;0&space;\\&space;D_{j-1}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;>&space;0&space;\end{cases}" title="D_{j}^{up} = \begin{cases} D_{j} \quad \text{ if } V_{j}^x \leq 0 \\ D_{j-1} \quad \text{ if } V_{j}^x > 0 \end{cases}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=Ed_{j}^{up}&space;=&space;\begin{cases}&space;Ed_{j}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;\leq&space;0&space;\\&space;Ed_{j-1}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;>&space;0&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Ed_{j}^{up}&space;=&space;\begin{cases}&space;Ed_{j}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;\leq&space;0&space;\\&space;Ed_{j-1}&space;\quad&space;\text{&space;if&space;}&space;V_{j}^x&space;>&space;0&space;\end{cases}" title="Ed_{j}^{up} = \begin{cases} Ed_{j} \quad \text{ if } V_{j}^x \leq 0 \\ Ed_{j-1} \quad \text{ if } V_{j}^x > 0 \end{cases}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{cases}&space;Mx_{j}&space;\quad&space;\text{&space;if&space;}&space;\langle&space;V_{j}^x&space;\rangle&space;\leq&space;0&space;\\&space;Mx_{j-1}&space;\quad&space;\text{&space;if&space;}&space;\langle&space;V_{j}^x&space;\rangle&space;>&space;0&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{cases}&space;Mx_{j}&space;\quad&space;\text{&space;if&space;}&space;\langle&space;V_{j}^x&space;\rangle&space;\leq&space;0&space;\\&space;Mx_{j-1}&space;\quad&space;\text{&space;if&space;}&space;\langle&space;V_{j}^x&space;\rangle&space;>&space;0&space;\end{cases}" title="\begin{cases} Mx_{j} \quad \text{ if } \langle V_{j}^x \rangle \leq 0 \\ Mx_{j-1} \quad \text{ if } \langle V_{j}^x \rangle > 0 \end{cases}" /></a>

###### Discretized equations using Explicit Euler
  <a href="https://www.codecogs.com/eqnedit.php?latex=D_{j}^{n&plus;1}&space;=&space;D_{j}^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{D_{j}^{up}V_{j&plus;1}^x&space;-&space;D_{j}^{up}V_{j}^x}{\Delta&space;x}&space;\right)^{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{j}^{n&plus;1}&space;=&space;D_{j}^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{D_{j}^{up}V_{j&plus;1}^x&space;-&space;D_{j}^{up}V_{j}^x}{\Delta&space;x}&space;\right)^{n}" title="D_{j}^{n+1} = D_{j}^{n} - \Delta t \left( \frac{D_{j}^{up}V_{j+1}^x - D_{j}^{up}V_{j}^x}{\Delta x} \right)^{n}" /></a>
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=Mx_{j}^{n&plus;1}&space;=&space;Mx_{j}^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{Mx_{j}^{up}\langle&space;V^{x}&space;\rangle_{j}&space;-&space;Mx_{j-1}^{up}&space;\langle&space;V^{x}&space;\rangle_{j-1}}{\Delta&space;x}&space;\right)^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{p_{j}-p_{j-1}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Mx_{j}^{n&plus;1}&space;=&space;Mx_{j}^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{Mx_{j}^{up}\langle&space;V^{x}&space;\rangle_{j}&space;-&space;Mx_{j-1}^{up}&space;\langle&space;V^{x}&space;\rangle_{j-1}}{\Delta&space;x}&space;\right)^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{p_{j}-p_{j-1}}{\Delta&space;x}&space;\right)" title="Mx_{j}^{n+1} = Mx_{j}^{n} - \Delta t \left( \frac{Mx_{j}^{up}\langle V^{x} \rangle_{j} - Mx_{j-1}^{up} \langle V^{x} \rangle_{j-1}}{\Delta x} \right)^{n} - \Delta t \left( \frac{p_{j}-p_{j-1}}{\Delta x} \right)" /></a>
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=Ed_{j}^{n&plus;1}&space;=&space;Ed_{j}^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{Ed_{j}^{up}V_{j&plus;1}^x&space;-&space;Ed_{j}^{up}V_{j}^x}{\Delta&space;x}\right)^{n}&space;-&space;\Delta&space;t&space;\left(&space;(\gamma&space;-&space;1)&space;\left(&space;\frac{Ed}{u^t}\right)^n&space;\left(&space;\frac{(u^t)^{n&plus;1}-(u^t)^n}{\Delta&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^x&space;-&space;V_{j}^x}{\Delta&space;x&space;}\right)&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Ed_{j}^{n&plus;1}&space;=&space;Ed_{j}^{n}&space;-&space;\Delta&space;t&space;\left(&space;\frac{Ed_{j}^{up}V_{j&plus;1}^x&space;-&space;Ed_{j}^{up}V_{j}^x}{\Delta&space;x}\right)^{n}&space;-&space;\Delta&space;t&space;\left(&space;(\gamma&space;-&space;1)&space;\left(&space;\frac{Ed}{u^t}\right)^n&space;\left(&space;\frac{(u^t)^{n&plus;1}-(u^t)^n}{\Delta&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^x&space;-&space;V_{j}^x}{\Delta&space;x&space;}\right)&space;\right)" title="Ed_{j}^{n+1} = Ed_{j}^{n} - \Delta t \left( \frac{Ed_{j}^{up}V_{j+1}^x - Ed_{j}^{up}V_{j}^x}{\Delta x}\right)^{n} - \Delta t \left( (\gamma - 1) \left( \frac{Ed}{u^t}\right)^n \left( \frac{(u^t)^{n+1}-(u^t)^n}{\Delta t} + \frac{V_{j+1}^x - V_{j}^x}{\Delta x }\right) \right)" /></a>


###### Discretized equations using Implicit Euler

The paramater <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a> controls the implicit scheme. Value 1.0 implies Implicit Euler. Other useful values like 0.5 which imply Crank-Nicholson are for future use.

The 3 set of equations can be written as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{D_{j}^{n&plus;1}&space;-&space;D_{j}^{n}}{\Delta&space;t}&space;&plus;&space;\alpha&space;\left(&space;\frac{D_{j&plus;1}^{up,n&plus;1}V_{j&plus;1}^{x,n&plus;1}&space;-&space;D_{j}^{up,n&plus;1}V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;(1-\alpha)&space;\left(&space;\frac{D_{j&plus;1}^{up,n}V_{j&plus;1}^{x,n}&space;-&space;D_{j}^{up,n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{D_{j}^{n&plus;1}&space;-&space;D_{j}^{n}}{\Delta&space;t}&space;&plus;&space;\alpha&space;\left(&space;\frac{D_{j&plus;1}^{up,n&plus;1}V_{j&plus;1}^{x,n&plus;1}&space;-&space;D_{j}^{up,n&plus;1}V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;(1-\alpha)&space;\left(&space;\frac{D_{j&plus;1}^{up,n}V_{j&plus;1}^{x,n}&space;-&space;D_{j}^{up,n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)&space;=&space;0" title="\frac{D_{j}^{n+1} - D_{j}^{n}}{\Delta t} + \alpha \left( \frac{D_{j+1}^{up,n+1}V_{j+1}^{x,n+1} - D_{j}^{up,n+1}V_{j}^{x,n+1}}{\Delta x} \right) + (1-\alpha) \left( \frac{D_{j+1}^{up,n}V_{j+1}^{x,n} - D_{j}^{up,n}V_{j}^{x,n}}{\Delta x} \right) = 0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{M_{j}^{n&plus;1}&space;-&space;M_{j}^{n}}{\Delta&space;t}&space;&plus;&space;\alpha&space;\left(&space;\frac{M_{j}^{up,n&plus;1}\langle&space;V_{j}^{x,n&plus;1}&space;\rangle&space;-&space;M_{j-1}^{up,n&plus;1}&space;\langle&space;V_{j-1}^{x,n&plus;1}&space;\rangle}{\Delta&space;x}&space;\right)&space;&plus;&space;(1-\alpha)&space;\left(&space;\frac{M_{j}^{up,n}\langle&space;V_{j}^{x,n}&space;\rangle&space;-&space;M_{j-1}^{up,n}&space;\langle&space;V_{j-1}^{x,n}&space;\rangle}{\Delta&space;x}&space;\right)&space;=&space;-\alpha&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)&space;-(1-\alpha)&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{M_{j}^{n&plus;1}&space;-&space;M_{j}^{n}}{\Delta&space;t}&space;&plus;&space;\alpha&space;\left(&space;\frac{M_{j}^{up,n&plus;1}\langle&space;V_{j}^{x,n&plus;1}&space;\rangle&space;-&space;M_{j-1}^{up,n&plus;1}&space;\langle&space;V_{j-1}^{x,n&plus;1}&space;\rangle}{\Delta&space;x}&space;\right)&space;&plus;&space;(1-\alpha)&space;\left(&space;\frac{M_{j}^{up,n}\langle&space;V_{j}^{x,n}&space;\rangle&space;-&space;M_{j-1}^{up,n}&space;\langle&space;V_{j-1}^{x,n}&space;\rangle}{\Delta&space;x}&space;\right)&space;=&space;-\alpha&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)&space;-(1-\alpha)&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)" title="\frac{M_{j}^{n+1} - M_{j}^{n}}{\Delta t} + \alpha \left( \frac{M_{j}^{up,n+1}\langle V_{j}^{x,n+1} \rangle - M_{j-1}^{up,n+1} \langle V_{j-1}^{x,n+1} \rangle}{\Delta x} \right) + (1-\alpha) \left( \frac{M_{j}^{up,n}\langle V_{j}^{x,n} \rangle - M_{j-1}^{up,n} \langle V_{j-1}^{x,n} \rangle}{\Delta x} \right) = -\alpha \left( \frac{p_{j}^{n+1}-p_{j-1}^{n+1}}{\Delta x} \right) -(1-\alpha) \left( \frac{p_{j}^{n+1}-p_{j-1}^{n+1}}{\Delta x} \right)" /></a>
   
<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{E_{j}^{n&plus;1}&space;-&space;E_{j}^{n}}{\Delta&space;t}&space;&plus;&space;\alpha&space;\left(&space;\frac{E_{j&plus;1}^{up,n&plus;1}V_{j&plus;1}^{x,n&plus;1}&space;-&space;E_{j}^{up,n&plus;1}V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;(1-\alpha)&space;\left(&space;\frac{E_{j&plus;1}^{up,n}V_{j&plus;1}^{x,n}&space;-&space;E_{j}^{up,n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)&space;=&space;(\gamma&space;-&space;1)&space;\frac{E_{j}^{n&plus;1}}{u^{n&plus;1}}&space;\left(&space;\frac{u^{n&plus;1}&space;-&space;u^{n}}{\Delta&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^{n&plus;1}-V_{j}^{n&plus;1}}{\Delta&space;x}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{E_{j}^{n&plus;1}&space;-&space;E_{j}^{n}}{\Delta&space;t}&space;&plus;&space;\alpha&space;\left(&space;\frac{E_{j&plus;1}^{up,n&plus;1}V_{j&plus;1}^{x,n&plus;1}&space;-&space;E_{j}^{up,n&plus;1}V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;(1-\alpha)&space;\left(&space;\frac{E_{j&plus;1}^{up,n}V_{j&plus;1}^{x,n}&space;-&space;E_{j}^{up,n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)&space;=&space;(\gamma&space;-&space;1)&space;\frac{E_{j}^{n&plus;1}}{u^{n&plus;1}}&space;\left(&space;\frac{u^{n&plus;1}&space;-&space;u^{n}}{\Delta&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^{n&plus;1}-V_{j}^{n&plus;1}}{\Delta&space;x}&space;\right&space;)" title="\frac{E_{j}^{n+1} - E_{j}^{n}}{\Delta t} + \alpha \left( \frac{E_{j+1}^{up,n+1}V_{j+1}^{x,n+1} - E_{j}^{up,n+1}V_{j}^{x,n+1}}{\Delta x} \right) + (1-\alpha) \left( \frac{E_{j+1}^{up,n}V_{j+1}^{x,n} - E_{j}^{up,n}V_{j}^{x,n}}{\Delta x} \right) = (\gamma - 1) \frac{E_{j}^{n+1}}{u^{n+1}} \left( \frac{u^{n+1} - u^{n}}{\Delta t} + \frac{V_{j+1}^{n+1}-V_{j}^{n+1}}{\Delta x} \right )" /></a>
      
which when re-arranged gives a tridiagonal system of equations as follows:
    
**<a href="https://www.codecogs.com/eqnedit.php?latex=\text{&space;if&space;}&space;V_{j}^x&space;>&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{&space;if&space;}&space;V_{j}^x&space;>&space;0" title="\text{ if } V_{j}^x > 0" /></a> , then**
      
<a href="https://www.codecogs.com/eqnedit.php?latex=D_{j-1}^{n&plus;1}&space;\left(&space;\frac{-\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;D_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;&plus;&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;D_{j&plus;1}^{n&plus;1}&space;(0)&space;=&space;\frac{D_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{D_{j}^{n}V_{j&plus;1}^{x,n}&space;-&space;D_{j-1}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{j-1}^{n&plus;1}&space;\left(&space;\frac{-\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;D_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;&plus;&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;D_{j&plus;1}^{n&plus;1}&space;(0)&space;=&space;\frac{D_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{D_{j}^{n}V_{j&plus;1}^{x,n}&space;-&space;D_{j-1}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" title="D_{j-1}^{n+1} \left( \frac{-\alpha V_{j}^{x,n+1}}{\Delta x} \right) + D_{j}^{n+1} \left( \frac{1}{\Delta t} + \frac{\alpha V_{j+1}^{x,n+1}}{\Delta x} \right) + D_{j+1}^{n+1} (0) = \frac{D_{j}^{n}}{\Delta t} - (1-\alpha) \left(\frac{D_{j}^{n}V_{j+1}^{x,n} - D_{j-1}^{n}V_{j}^{x,n}}{\Delta x} \right)" /></a>
  
<a href="https://www.codecogs.com/eqnedit.php?latex=M_{j-1}^{n&plus;1}&space;\left(&space;\frac{-\alpha&space;\langle&space;V_{j-1}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;M_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;&plus;&space;\frac{\alpha&space;\langle&space;V_{j}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;M_{j&plus;1}^{n&plus;1}&space;(0)&space;=&space;\frac{M_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{M_{j}^{n}\langle&space;V_{j}&space;\rangle&space;^{x,n}&space;-&space;M_{j-1}^{n}\langle&space;V_{j-1}&space;\rangle&space;^{x,n}}{\Delta&space;x}&space;\right)&space;-&space;\alpha&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)&space;-&space;(1-\alpha)&space;\left(&space;\frac{p_{j}^{n}-p_{j-1}^{n}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?M_{j-1}^{n&plus;1}&space;\left(&space;\frac{-\alpha&space;\langle&space;V_{j-1}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;M_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;&plus;&space;\frac{\alpha&space;\langle&space;V_{j}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;M_{j&plus;1}^{n&plus;1}&space;(0)&space;=&space;\frac{M_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{M_{j}^{n}\langle&space;V_{j}&space;\rangle&space;^{x,n}&space;-&space;M_{j-1}^{n}\langle&space;V_{j-1}&space;\rangle&space;^{x,n}}{\Delta&space;x}&space;\right)&space;-&space;\alpha&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)&space;-&space;(1-\alpha)&space;\left(&space;\frac{p_{j}^{n}-p_{j-1}^{n}}{\Delta&space;x}&space;\right)" title="M_{j-1}^{n+1} \left( \frac{-\alpha \langle V_{j-1} \rangle ^{x,n+1}}{\Delta x} \right) + M_{j}^{n+1} \left( \frac{1}{\Delta t} + \frac{\alpha \langle V_{j} \rangle ^{x,n+1}}{\Delta x} \right) + M_{j+1}^{n+1} (0) = \frac{M_{j}^{n}}{\Delta t} - (1-\alpha) \left(\frac{M_{j}^{n}\langle V_{j} \rangle ^{x,n} - M_{j-1}^{n}\langle V_{j-1} \rangle ^{x,n}}{\Delta x} \right) - \alpha \left( \frac{p_{j}^{n+1}-p_{j-1}^{n+1}}{\Delta x} \right) - (1-\alpha) \left( \frac{p_{j}^{n}-p_{j-1}^{n}}{\Delta x} \right)" /></a>
  
<a href="https://www.codecogs.com/eqnedit.php?latex=E_{j-1}^{n&plus;1}&space;\left(&space;\frac{-\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;E_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;&plus;&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;-&space;\frac{\gamma&space;-&space;1}{u^{n&plus;1}}&space;\left(&space;\frac{\partial&space;u}{\partial&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^{x,n&plus;1}-V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;\right)&space;&plus;&space;E_{j&plus;1}^{n&plus;1}&space;(0)&space;=&space;\frac{E_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{E_{j}^{n}V_{j&plus;1}^{x,n}&space;-&space;E_{j-1}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{j-1}^{n&plus;1}&space;\left(&space;\frac{-\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;E_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;&plus;&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;-&space;\frac{\gamma&space;-&space;1}{u^{n&plus;1}}&space;\left(&space;\frac{\partial&space;u}{\partial&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^{x,n&plus;1}-V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;\right)&space;&plus;&space;E_{j&plus;1}^{n&plus;1}&space;(0)&space;=&space;\frac{E_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{E_{j}^{n}V_{j&plus;1}^{x,n}&space;-&space;E_{j-1}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" title="E_{j-1}^{n+1} \left( \frac{-\alpha V_{j}^{x,n+1}}{\Delta x} \right) + E_{j}^{n+1} \left( \frac{1}{\Delta t} + \frac{\alpha V_{j+1}^{x,n+1}}{\Delta x} - \frac{\gamma - 1}{u^{n+1}} \left( \frac{\partial u}{\partial t} + \frac{V_{j+1}^{x,n+1}-V_{j}^{x,n+1}}{\Delta x} \right) \right) + E_{j+1}^{n+1} (0) = \frac{E_{j}^{n}}{\Delta t} - (1-\alpha) \left(\frac{E_{j}^{n}V_{j+1}^{x,n} - E_{j-1}^{n}V_{j}^{x,n}}{\Delta x} \right)" /></a>
   
**and  <a href="https://www.codecogs.com/eqnedit.php?latex=\text{&space;if&space;}&space;V_{j}^x&space;\leq&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\text{&space;if&space;}&space;V_{j}^x&space;\leq&space;0" title="\text{ if } V_{j}^x \leq 0" /></a> , then**
      
<a href="https://www.codecogs.com/eqnedit.php?latex=D_{j-1}^{n&plus;1}(0)&space;&plus;&space;D_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;-&space;\frac{\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;D_{j&plus;1}^{n&plus;1}&space;\left(&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;=&space;\frac{D_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{D_{j&plus;1}^{n}V_{j&plus;1}^{x,n}&space;-&space;D_{j}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?D_{j-1}^{n&plus;1}(0)&space;&plus;&space;D_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;-&space;\frac{\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;D_{j&plus;1}^{n&plus;1}&space;\left(&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;=&space;\frac{D_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{D_{j&plus;1}^{n}V_{j&plus;1}^{x,n}&space;-&space;D_{j}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" title="D_{j-1}^{n+1}(0) + D_{j}^{n+1} \left( \frac{1}{\Delta t} - \frac{\alpha V_{j}^{x,n+1}}{\Delta x} \right) + D_{j+1}^{n+1} \left( \frac{\alpha V_{j+1}^{x,n+1}}{\Delta x} \right) = \frac{D_{j}^{n}}{\Delta t} - (1-\alpha) \left(\frac{D_{j+1}^{n}V_{j+1}^{x,n} - D_{j}^{n}V_{j}^{x,n}}{\Delta x} \right)" /></a>
 
<a href="https://www.codecogs.com/eqnedit.php?latex=M_{j-1}^{n&plus;1}&space;(0)&space;&plus;&space;M_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;-&space;\frac{\alpha&space;\langle&space;V_{j-1}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;M_{j&plus;1}^{n&plus;1}&space;\left(&space;\frac{\alpha&space;\langle&space;V_{j}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;=&space;\frac{M_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{M_{j&plus;1}^{n}\langle&space;V_{j}&space;\rangle&space;^{x,n}&space;-&space;M_{j}^{n}\langle&space;V_{j-1}&space;\rangle&space;^{x,n}}{\Delta&space;x}&space;\right)&space;-&space;\alpha&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)&space;-&space;(1-\alpha)&space;\left(&space;\frac{p_{j}^{n}-p_{j-1}^{n}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?M_{j-1}^{n&plus;1}&space;(0)&space;&plus;&space;M_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;-&space;\frac{\alpha&space;\langle&space;V_{j-1}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;&plus;&space;M_{j&plus;1}^{n&plus;1}&space;\left(&space;\frac{\alpha&space;\langle&space;V_{j}&space;\rangle&space;^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;=&space;\frac{M_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{M_{j&plus;1}^{n}\langle&space;V_{j}&space;\rangle&space;^{x,n}&space;-&space;M_{j}^{n}\langle&space;V_{j-1}&space;\rangle&space;^{x,n}}{\Delta&space;x}&space;\right)&space;-&space;\alpha&space;\left(&space;\frac{p_{j}^{n&plus;1}-p_{j-1}^{n&plus;1}}{\Delta&space;x}&space;\right)&space;-&space;(1-\alpha)&space;\left(&space;\frac{p_{j}^{n}-p_{j-1}^{n}}{\Delta&space;x}&space;\right)" title="M_{j-1}^{n+1} (0) + M_{j}^{n+1} \left( \frac{1}{\Delta t} - \frac{\alpha \langle V_{j-1} \rangle ^{x,n+1}}{\Delta x} \right) + M_{j+1}^{n+1} \left( \frac{\alpha \langle V_{j} \rangle ^{x,n+1}}{\Delta x} \right) = \frac{M_{j}^{n}}{\Delta t} - (1-\alpha) \left(\frac{M_{j+1}^{n}\langle V_{j} \rangle ^{x,n} - M_{j}^{n}\langle V_{j-1} \rangle ^{x,n}}{\Delta x} \right) - \alpha \left( \frac{p_{j}^{n+1}-p_{j-1}^{n+1}}{\Delta x} \right) - (1-\alpha) \left( \frac{p_{j}^{n}-p_{j-1}^{n}}{\Delta x} \right)" /></a>
  
<a href="https://www.codecogs.com/eqnedit.php?latex=E_{j-1}^{n&plus;1}&space;(0)&space;&plus;&space;E_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;-&space;\frac{\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;-&space;\frac{\gamma&space;-&space;1}{u^{n&plus;1}}&space;\left(&space;\frac{\partial&space;u}{\partial&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^{x,n&plus;1}-V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;\right)&space;&plus;&space;E_{j&plus;1}^{n&plus;1}&space;\left(&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;=&space;\frac{E_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{E_{j&plus;1}^{n}V_{j&plus;1}^{x,n}&space;-&space;E_{j}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{j-1}^{n&plus;1}&space;(0)&space;&plus;&space;E_{j}^{n&plus;1}&space;\left(&space;\frac{1}{\Delta&space;t}&space;-&space;\frac{\alpha&space;V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;-&space;\frac{\gamma&space;-&space;1}{u^{n&plus;1}}&space;\left(&space;\frac{\partial&space;u}{\partial&space;t}&space;&plus;&space;\frac{V_{j&plus;1}^{x,n&plus;1}-V_{j}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;\right)&space;&plus;&space;E_{j&plus;1}^{n&plus;1}&space;\left(&space;\frac{\alpha&space;V_{j&plus;1}^{x,n&plus;1}}{\Delta&space;x}&space;\right)&space;=&space;\frac{E_{j}^{n}}{\Delta&space;t}&space;-&space;(1-\alpha)&space;\left(\frac{E_{j&plus;1}^{n}V_{j&plus;1}^{x,n}&space;-&space;E_{j}^{n}V_{j}^{x,n}}{\Delta&space;x}&space;\right)" title="E_{j-1}^{n+1} (0) + E_{j}^{n+1} \left( \frac{1}{\Delta t} - \frac{\alpha V_{j}^{x,n+1}}{\Delta x} - \frac{\gamma - 1}{u^{n+1}} \left( \frac{\partial u}{\partial t} + \frac{V_{j+1}^{x,n+1}-V_{j}^{x,n+1}}{\Delta x} \right) \right) + E_{j+1}^{n+1} \left( \frac{\alpha V_{j+1}^{x,n+1}}{\Delta x} \right) = \frac{E_{j}^{n}}{\Delta t} - (1-\alpha) \left(\frac{E_{j+1}^{n}V_{j+1}^{x,n} - E_{j}^{n}V_{j}^{x,n}}{\Delta x} \right)" /></a>


*   Remarks
   * The dependence on values from (n+1)th iteration for Vx and P are handled by using an iterative procedure. This is explained in pseudo code below:
   ```
   Expectation: We are in iteration n, given values of step n we want to calculate values for n+1
   Input: Dn, Vn, Mn, Edn, Pn as the values from step n, iter_count as number of sub-iterations
   Procedure:
   	Set:
   		V* = Vn
   		P* = Pn
   	Loop: Execute the below sub-iteration for iter_count:
   		#Solve the 3 equations
   		D' = f1(Dn,Vn,V*)
   		M' = f2(Mn,Vn,V*,P*)
   		E' = f3(En,Vn,V*)
   		
   		#Update phase
   		V* = update_Vx(D',M')
   		P* = update_pressure(D',E')
   		
   		Repeat loop
   		
   	Finally:
   		Vn+1 = V*
   		Pn+1 = P*
   		Dn+1 = D'
   		Mn+1 = M'
   		En+1 = E'   		
   ```

**Key Data structures**
 
 1. Parameters

 ```python
  class RSTPExplicitParams(Params):
     def __init__(self,ncells,gamma=0,cfl=1.0):
         Params.__init__(self,"explicit") 
         self.gamma = gamma
         self.cfl = cfl
         self.ncells = ncells
         self.fv_boundary_strategy = None
   
  class RSTPImplicitParams(Params):
     def __init__(self,ncells,alpha,gamma=0,iter_count=1,cfl=0.50):
         Params.__init__(self,"implicit") 
         self.gamma = gamma
         self.ncells = ncells
         self.alpha = alpha
         self.fv_boundary_strategy = None        
         self.cfl = cfl #This is used to define time step size
         self.iter_count = iter_count
  ```
   These are used to define parameters for Explicit Euler time integration and Implicit time integration. 
 
   gamma = 0 defines isothermal gas
 
   Time limits are default [0,1] and spatial limits are default [0,1].
   
   Spatial grid size is automatically chosen by dividing spatial limit by ncells.
   
   Temporal grid size is automatically derived from spatial grid size by using CFL parameter.
	delta_t = self.params.cfl*delta_x   
 
   Example:
  ```python
   eparams = RSTPExplicitParams(1000,0,0.25) #isothermal gas, CFL=0.25
   iparams = RSTPImplicitParams(1000,1.0,0.0,2,0.7) #isothermal gas, Implicit Euler solver, iter_count=2, cfl=0.7  
  ```
 1. Initial Values
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
**Usage examples**

 ###### Solve RSTP using Explicit Euler
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

 ###### Solve RSTP using Implicit Euler
 Number of FV cells = 1000, gamma = 4/3, CFL = 0.7, no of subiterations = 2
 ```python
     iparams = RSTPImplicitParams(1000,1.0,4/3,2,0.7)
     iparams.set_fig_path('./figs/')
     iparams.fv_boundary_strategy = FVTransverse #Default 
     iiv = RSTPIV(Vx=[0,0],Mx=[0,0],D=[1,10**-2],Rho=[1,10**-2])
     ibv = RSTPBV()
     test_implicit = RSTPTest(2,iparams,iiv,ibv,ode_strategy=ODEImplicit)
     test_implicit.solve()
 ```

 #### Output
 The output is generated as a set of 4 image files in the same directory as provided in set_fig_path() API.

 The 4 image files correspond to plot of spatial variable x against Relativistic Density (D), Pressure(P), Lorentz factor (<a  href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;u^{t}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;u^{t}" title="u^{t}" /></a>) and Transport Velocity (<a href="https://www.codecogs.com/eqnedit.php?latex=\bg_white&space;V^x" target="_blank"><img src="https://latex.codecogs.com/png.latex?\bg_white&space;V^x"  title="V^x" /></a>) respectively

An example is shown below:
(images/D_img.png)
(images/P_img.png)
(images/U_img.png)
(images/V_img.png)
