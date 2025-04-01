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

