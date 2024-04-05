---
title: Model
description: How to obtain the model
---

TinyMPC in its vanilla implementation can only handle linear dynamics, which means systems must be linearized about an equilibrium before being used by the solver. Extensions to TinyMPC allow the user to approximate a system's nonlinear dynamics by storing multiple linearizations, but we will start with only one.

A discrete, linearized system is of the form $x_{k+1} = Ax_k + Bu_k$, where $x_k$ and $u_k$ are the state and control at the current time step, $A$ is the state-transition matrix, $B$ is the control or input matrix, and $x_{k+1}$ is the state at the next time step. For each of the examples given in [the previous page](getting-started/examples), the state-transition matrix $A$ and input matrix $B$ were computed from the system's continuous, nonlinear dynamics. (1)
{.annotate}

1. The system still needs to be discretized even if it is already linear. This can be done with the matrix exponential or by the same methods shown for the nonlinear system below.

## Cart-pole example

The continuous time dynamics for the cart-pole [have](https://courses.ece.ucsb.edu/ECE594/594D_W10Byl/hw/cartpole_eom.pdf) [been](https://www.matthewpeterkelly.com/tutorials/cartPole/index.html) [derived](https://underactuated.mit.edu/acrobot.html) [many](https://sharpneat.sourceforge.io/research/cart-pole/cart-pole-equations.html) [times](https://danielpiedrahita.wordpress.com/portfolio/cart-pole-control/). For this example we'll use the convention from [this derivation](https://coneural.org/florian/papers/05_cart_pole.pdf), where the pole is upright at $\theta=0$. If we ignore friction for this model, the only equations we care about in that derivation are (23) and (24). (1)
{.annotate}

1. If you're following along and want to use a cart-pole model that has friction, use equations (21) and (22).

Let's write those down in a dynamics function

=== "Python"

    ```py
    def cartpole_dynamics(x, u):
        r       = x[0] # cart position
        theta   = x[1] # pole angle
        rd      = x[2] # change in cart position
        theta_d = x[3] # change in pole angle
        F       = u[0] # force applied to cart
        
        theta_dd = (g*np.sin(theta) + np.cos(theta) * ((-F - mp*ℓ*(theta_d**2) * \
                        np.sin(theta))/(mc + mp))) / (ℓ*(4/3 - (mp*(np.cos(theta)**2))/(mc + mp)))
        rdd = (F + mp*ℓ*((theta_d**2)*np.sin(theta) - theta_dd*np.cos(theta))) / (mc + mp)

        return np.array([rd, theta_d, rdd, theta_dd])
    ```

=== "Julia"

    ```julia
    function cartpole_dynamics(x::Vector, u::Vector)
        r  = x[1] # cart position
        θ  = x[2] # pole angle
        rd = x[3] # change in cart position
        θd = x[4] # change in pole angle
        F  = u[1] # force applied to cart
        
        θdd = (g*sin(θ) + cos(θ) * ((-F - mp*ℓ*(θd^2) * sin(θ))/(mc + mp))) /
                 (ℓ*(4/3 - (mp*(cos(θ)^2))/(mc + mp)))
        rdd = (F + mp*ℓ*((θd^2)*sin(θ) - θdd*cos(θ))) / (mc + mp)
    
        return [rd; θd; rdd; θdd]
    end
    ```


This function describes the continuous dynamics of our system. Before linearizing, we first discretize with an integrator. RK4 (Runge-Kutta 4th order) is a common explicit integrator, but you can write down whatever you like.

=== "Python"

    ```py
    def cartpole_rk4(x, u):
        f1 = cartpole_dynamics(x, u)
        f2 = cartpole_dynamics(x + 0.5*h*f1, u)
        f3 = cartpole_dynamics(x + 0.5*h*f2, u)
        f4 = cartpole_dynamics(x + h*f3, u)
        return x + (h/6.0)*(f1 + 2*f2 + 2*f3 + f4)
    ```

=== "Julia"

    ```julia
    function rk4(params::NamedTuple, x::Vector, u::Vector, dt::Float64)
        k1 = dt*dynamics(params, x, u)
        k2 = dt*dynamics(params, x + k1/2, u)
        k3 = dt*dynamics(params, x + k2/2, u)
        k4 = dt*dynamics(params, x + k3, u)
        return x + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    end
    ```