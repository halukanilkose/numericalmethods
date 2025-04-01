**Problem:** <br /> 
A fuel element of a nuclear reactor is in the shape of a plane wall of thickness 2L=20mm and is convectively cooled at both surfaces, 
with h=1100 W/m<sup>2</sup> K and T 250°C. At normal operating power, heat is generated uniformly within the element at a volumetric 
rate of 10<sup>7</sup>W/m<sup>3</sup>. A departure from the steady-state conditions associated with normal operation will occur if 
there is a change in the generation rate. Consider a sudden change to 2x10<sup>7</sup>W/m<sup>3</sup>, and use the explicit finite-difference 
method to determine the fuel element temperature distribution after 1.5s. The fuel element thermal properties are k=30 W/mK and α=5x10<sup>-6</sup>m<sup>2</sup>/s.<br /> 
**Assumptions:** <br /> 
1. One dimensional heat conduction in x direction. <br />
2. Uniform heat generation. <br />
3. Constant thermophysical properties. <br />

**Mathematical Background** <br /> 
To solve the given problem, it is necessary to determine the temperature distribution in the steady state, where the heat generation is 10<sup>7</sup> W/m<sup>3</sup>. Therefore, if the energy balance is written for a one-dimensional heat transfer problem in the steady state, equation given below can be obtained.<br />

$${{{\partial ^2}T} \over {\partial {x^2}}} + {q \over k} = 0$$ <br />

T, x, q and k represents the temperature, position, heat generation and thermal conductivity, respectively. The temperature as a function of position has been solved using the method of separable ordinary differential equations, and the equation given below has been obtained.<br />

$$T\left( x \right) =  - {q \over {2k}}{x^2} + {C_1}x + {C_2}$$<br />

As seen in Equation,there are constants C<sub>1</sub>	 and C<sub>2</sub>. To determine these constants, two boundary conditions are required. As specified in the problem, heat transfer occurs due to forced heat transfer on both sides of the wall. In this context, in order to reduce the computational cost of the problem by dividing the wall in half, the right side of the wall has been analyzed. The resulting temperature distribution can also be applied to the other side of the wall. The boundary condition at x=0 is given in the following equation.<br />

$${{dT} \over {dx}} = 0$$ <br />
The boundary condition at x=L is given in the following equation.<br />

$$ - k{{dT} \over {dx}} = h\left( {{T_s} - {T_\infty }} \right)$$ <br />

By applying the symmetric boundary condition, the constant 𝐶<sub>1</sub> is found to be 0. Furthermore, by applying the boundary condition at 𝑥=𝐿, $${C_2} = {T_\infty } + {{qL} \over h} - {{q{L^2}} \over {2k}}$$ has been determined.If the constant 𝐶<sub>2</sub> is written into the general solution and the necessary adjustments are made, the temperature variation with respect to position in the steady-state regime is given by the following equation.<br />

$$T\left( x \right) = {{q{L^2}} \over {2k}}\left( {1 - {{{x^2}} \over {{L^2}}}} \right) + T{}_\infty  + {{qL} \over h}$$<br />

A numerical time-dependent solution will be obtained using the FTCS (Forward Time Central Space) finite difference method, with a position increment of Δx=0.002m. Except for the regions where boundary conditions apply, the discretized form of the equation in heat equation shall be used.<br />

$$k{{{\partial ^2}T} \over {\partial {x^2}}} + q = \rho {c_p}{{\partial T} \over {\partial t}}$$ <br />

When the equation is discretized, it will take the following form:<br />

$$k{{T_{i + 1}^j - 2T_i^j + T_{i - 1}^j} \over {\Delta {x^2}}} + q = \rho {c_p}{{T_i^{j + 1} - T_i^j} \over {\Delta t}}$$<br />

When the necessary adjustments are made, the following time-dependent 1-dimensional heat equation is obtained:<br />

$$T_i^{j + 1} = Fo\left[ {T_{i - 1}^j - T_{i + 1}^j + {{q\Delta {x^2}} \over k}} \right] + \left( {1 - 2Fo} \right)T_i^j$$ <br />

where <br />, 

$$Fo = {{k\Delta t} \over {\rho {c_p}\Delta {x^2}}}$$  <br />

$$Fo\left( {1 + Bi} \right) \le {1 \over 2}$$ <br />

By considering the symmetry around x=0, the symmetry boundary condition is applied, and for the region with the symmetry boundary condition, $${T_{m + 1}} = {T_{m - 1}}$$ is used. Therefore, the general equation for the 0th node is written, and the following equality is obtained:<br />

$$T_0^{j + 1} = Fo\left[ {2T_1^p + {{q\Delta {x^2}} \over k}} \right] + \left( {1 - 2Fo} \right)T_0^j$$<br />

Apart from this, at the outermost node, the following equality is used. The outermost point of the 0.01 meter grid, divided into intervals of 0.002 meters, is the 5th point. If energy conservation is applied at this point, Equation given below is obtained.<br />

$${h\left( {{T_\infty } - T{}_L} \right) + k{{\partial T} \over {\partial x}} + {{q\Delta x} \over 2} = \rho {{\Delta x} \over 2}{c_p}{{\partial T} \over {\partial t}}}$$ <br />

When the necessary adjustments are made, the following equation is obtained for the outermost node:<br />

$$T_5^{j + 1} = 2Fo\left[ {T_4^p + Bi{T_\infty } + {{q\Delta {x^2}} \over {2k}}} \right] + \left( {1 - 2Fo - 2BiFo} \right)T_5^j$$<br />


| Time[s]/Location[m]     | 0.000   | 0.002 | 0.004 | 0.006 | 0.008 | 1.000 | 
| ---                     | ---     | ---   | ---   | ---   | ---   | ---   |
| 0                       | 357.58  | 356.91| 354.91| 351.58| 346.91| 340.91| 
| 0.3                     | 358.08  | 357.41| 355.41| 352.08| 347.41| 341.41| 
| 0.6                     | 358.58  | 357.91| 355.91| 352.58| 347.91| 341.88| 
| 0.9                     | 359.08  | 358.41| 356.41| 353.08| 348.41| 342.35| 
| 1.2                     | 359.58  | 358.91| 356.91| 353.58| 348.89| 342.82| 
| 1.5                     | 360.08  | 359.41| 357.41| 354.07| 349.37| 343.27| 
| 1.5                     | 465.15  | 463.82| 459.82| 453.15| 443.82| 431.82|
