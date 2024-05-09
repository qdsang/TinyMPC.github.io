---
title: Examples
description: TinyMPC examples
---

# Using TinyMPC

Here we show how to use TinyMPC to control a cart-pole and 3D quadrotor with the python interface. Make sure you have [installed the package](installation.md).

Check out our GitHub repository for [examples in C++](https://github.com/TinyMPC/TinyMPC/tree/main/examples), and visit our [GitHub Discussions](https://github.com/TinyMPC/discussions) page for any questions related to the solver!
<!-- !!!note "Julia and MATLAB examples are under construction." -->

---

## Set up problem

TinyMPC requires four matrices (A, B, Q, and R) and one number (N) to use. A and B describe the linearized system dynamics and Q and R are the costs on the state and control inputs. N is the length of the prediction horizon (or the number of time steps in the problem). This page assumes you already have a discrete, linearized model of your system dynamics (A and B). [The next page](./model.md) walks through obtaining these starting from a nonlinear model.

=== "Cart-pole"

    For the cart-pole, we use the linearized model of the discretized cart-pole dynamics to stabilize about the upright position. The state is the position of the cart, the angle of the pole, the velocity of the cart, and the angular velocity of the pole, which looks like $x = [p, \theta, v, \omega]^T$. The control input is a single force $u$ acting on the cart. (1)
    {.annotate}

    1. TinyMPC always produces a $\Delta u$ and $\Delta x$ about the linearization point. Because we linearized the cart-pole about an equilibrium position that required no control input, $\Delta u$ = $u$. Additionally, as discussed in [this page](./model.md), because we defined the coordinate frame of our cart-pole system such that the vertical equilibrium position (which is where we linearized) corresponds to a state of all zeros, $\Delta x$ = $x$. This is irrelevant for the following example, but is important to keep in mind when simulating the system with its full dynamics or applying a control input when the linearization point is not at $x=0$ or $u=0$.


    ``` py
    import tinympc
    import numpy as np

    # Define necessary data
    A = np.array([[1.0, 0.01, 0.0, 0.0], # (1)
                  [0.0, 1.0, 0.039, 0.0],
                  [0.0, 0.0, 1.002, 0.01],
                  [0.0, 0.0, 0.458, 1.002]])
    B = np.array([[0.0  ], # (2)
                  [0.02 ],
                  [0.0  ],
                  [0.067]])
    Q = np.diag([10.0, 1, 10, 1]) # (3)
    R = np.diag([1.0]) # (4)

    N = 20 # (5)

    # Set up the problem
    prob = tinympc.TinyMPC()
    prob.setup(A, B, Q, R, N)

    # Define initial condition
    x0 = np.array([0.5, 0, 0, 0])
    ```

    1. This is the state transition matrix, which you get when linearizing the discretized version of your model's full nonlinear dynamics (in this case the cart-pole dynamics, described on [this page](./model.md)) with respect to the state.
    2. This is the input or control matrix, which you get when linearizing the discretized version of your model's full nonlinear dynamics (in this case the cart-pole dynamics, described on [this page](./model.md)) with respect to the input.
    3. This is the stage cost for the state, and defines how much to penalize the state for deviating from the reference state at each time step in the horizon. Change this to modify the controller's behavior.
    4. This is the stage cost for the input, and defines how much to penalize the input for deviating from the reference control at each time step in the horizon. Change this to modify the controller's behavior.
    5. This is the length of the horizon, and can be anything greater than one. The problem size scales linearly with this variable.



=== "Quadrotor"

    For the quadrotor, we use the linearized model of the discretized quadrotor dynamics to stabilize about a hovering position. The state is composed of twelve variables: the three dimensional position, orientation, translational velocity, and angular velocity, which looks like $x = [p_x, p_y, p_z, \theta_x, \theta_y, \theta_z, v_x, v_y, v_z, \omega_x, \omega_y, \omega_z]^T$. The control input is a four dimensional vector describing the thrust of each motor, and looks like $u = [u_1, u_2, u_3, u_4]^T$.
    
    In this case, because the dynamics were linearized about a state which required some nominal thrust $u_\text{hover}$ to keep the quadrotor airborne, the solution from TinyMPC is actually a $\Delta u$ from $u_\text{hover}$. In a real implementation, the command that should be sent to the quadrotor is the absolute thrust $\Delta u + u_\text{hover}$, where $u_\text{hover}$ depends on the specific quadrotor. (1)
    {.annotate}

    1. In the case of the cart-pole, the output from TinyMPC was still a $\Delta u$. However, because we linearized about an equilibrium position that required no control input, this was a $\Delta u$ from zero, and so there was no difference between the computed $\Delta u$ and the absolute value $u$ which would be sent to the cart-pole's motor controller.


    ``` py
    import tinympc
    import numpy as np

    # Define necessary data
    A = np.array([ # (1)
        [1.0, 0.0, 0.0, 0.0, 0.0245250, 0.0, 0.050, 0.0, 0.0, 0.0, 0.02044, 0.0],
        [0.0, 1.0, 0.0, -0.0245250, 0.0, 0.0, 0.0, 0.050, 0.0, -0.02044, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.050, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0250000, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0250000, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.025],
        [0.0, 0.0, 0.0, 0.0, 0.9810000, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0122625, 0.0],
        [0.0, 0.0, 0.0, -0.9810000, 0.0, 0.0, 0.0, 1.0, 0.0, -0.0122625, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])

    B = np.array([ # (2)
        [-0.07069, 0.07773, 0.07091, -0.07795],
        [0.07034, 0.07747, -0.07042, -0.07739],
        [0.0052554, 0.0052554, 0.0052554, 0.0052554],
        [-0.1720966, -0.1895213, 0.1722891, 0.1893288],
        [-0.1729419, 0.1901740, 0.1734809, -0.1907131],
        [0.0123423, -0.0045148, -0.0174024, 0.0095748],
        [-0.0565520, 0.0621869, 0.0567283, -0.0623632],
        [0.0562756, 0.0619735, -0.0563386, -0.0619105],
        [0.2102143, 0.2102143, 0.2102143, 0.2102143],
        [-13.7677303, -15.1617018, 13.7831318, 15.1463003],
        [-13.8353509, 15.2139209, 13.8784751, -15.2570451],
        [0.9873856, -0.3611820, -1.3921880, 0.7659845]])

    Q = np.diag([100.0, 100.0, 100.0, 4.0, 4.0, 400.0, # (3)
                4.0, 4.0, 4.0, 2.0408163, 2.0408163, 4.0]);
    R = np.diag([400.0]*4); # (4)

    N = 20 # (5)

    # Set up the problem
    prob = tinympc.TinyMPC()
    prob.setup(A, B, Q, R, N)

    # Define initial condition
    x0 = np.array([0.5, 1.3, -0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ```

    1. This is the state transition matrix, which you get when linearizing the discretized version of your model's full nonlinear dynamics (in this case the cart-pole dynamics, described on [this page](./model.md)) with respect to the state.
    2. This is the input or control matrix, which you get when linearizing the discretized version of your model's full nonlinear dynamics (in this case the cart-pole dynamics, described on [this page](./model.md)) with respect to the input.
    3. This is the stage cost for the state, and defines how much to penalize the state for deviating from the reference state at each time step in the horizon. Change this to modify the controller's behavior.
    4. This is the stage cost for the input, and defines how much to penalize the input for deviating from the reference control at each time step in the horizon. Change this to modify the controller's behavior.
    5. This is the length of the horizon, and can be anything greater than one. The problem size scales linearly with this variable.

---

## Solve problem

``` py
# Set the first state in the horizon
prob.set_x0(x0)

# Solve the problem
solution = prob.solve()

# Print the controls at the first time step
print(solution["controls"])
```


---

## Model-predictive control

To use TinyMPC as a controller, all we have to do is solve in a loop, setting the first state in the horizon to the most recent estimate of the system's state at each time step. This estimate can come from a Kalman filter, for example. In this simple example we assume we have a perfect estimate of the state. On an actual robot, the simulation step would just be the physics from the real world acting on the system. To more accurately predict what that would look like, you can simulate the nonlinear system dynamics forward by one time step using an implicit integrator, of which there are many. We simulate with the linearized system dynamics for brevity.
    
### Solve

``` py
# Loop for an arbitrary number of time steps
Nsim = 1000
xs = np.zeros((Nsim-N, Q.shape[0])) # History of states for plotting
us = np.zeros((Nsim-N, R.shape[0])) # History of controls for plotting
for i in range(Nsim-N):
    prob.set_x0(x0) # Set the first state in the horizon
    solution = prob.solve() # Solve the problem
    x0 = A@x0 + B@solution["controls"] # Simulate the system (1)
    xs[i] = x0
    us[i] = solution["controls"]
```

1. In this rudimentary example we simulate the system forward in time with the linearized dynamics. However, for a legitimate simulation this should be done by querying the nonlinear, discretized system dynamics, which might be implemented using the cartpole_rk4 function shown [here](./model.md/#cart-pole-example), for example.


### Plot solution


=== "Cart-pole"

    ``` py
    import matplotlib.pyplot as plt

    # Plot trajectory
    fig, axs = plt.subplots(2, 1, sharex=True)
    axs[0].plot(xs, label=["x (meters)", "theta (radians)", "x_dot (m/s)", "theta_dot (rad/s)"])
    axs[1].plot(us, label="control (Newtons)")
    axs[0].set_title("cartpole trajectory over time")
    axs[1].set_xlabel("time steps (100Hz)")
    axs[0].legend()
    axs[1].legend()
    plt.show()
    ```

    
=== "Quadrotor"

    ``` py
    import matplotlib.pyplot as plt
    
    # Plot trajectory
    fig, axs = plt.subplots(2, 1, sharex=True)
    axs[0].plot(xs[:,:3], label=["x", "y", "z"])
    axs[1].plot(us, label=["u1", "u2", "u3", "u4])
    axs[0].set_title("quadrotor trajectory over time")
    axs[1].set_xlabel("time steps (100Hz)")
    axs[0].legend()
    axs[1].legend()
    plt.show()
    ```

---

## Code generation

Generating code looks very similar to what we just did. All we have to do is set up the problem like before and code can be generated into a specified directory. Source, CMake, and example main files are copied or generated in the new directory. The generated code is then compiled into a python module that can be imported and used to validate its behavior before integrating it with a system.

The following code generates a solver for a cartpole with control bounds of -0.5 and 0.5 Newtons, and limits the maximum number of iterations at each time step to 50. It puts everything in a folder called "generated_code".

``` py
import tinympc
import numpy as np

A = np.array([[1.0, 0.01, 0.0, 0.0],
              [0.0, 1.0, 0.039, 0.0],
              [0.0, 0.0, 1.002, 0.01],
              [0.0, 0.0, 0.458, 1.002]])
B = np.array([[0.0  ],
              [0.02 ],
              [0.0  ],
              [0.067]])
Q = np.diag([10.0, 1, 10, 1])
R = np.diag([1.0])

N = 20

prob = tinympc.TinyMPC()

u_min = np.array([-0.5])
u_max = np.array([0.5])
prob.setup(A, B, Q, R, N, max_iter=50, u_min=u_min, u_max=u_max)

prob.codegen("generated_code", verbose=1)
```

### Validate with python

TinyMPC will automatically compile the generated code into a new python module called `tinympcgen`, which will exist inside the output folder as a file with the name `tinympcgen.python-version-and-system-type.so`. To use it, just `import tinympcgen`, then set the reference trajectory if desired with `set_x_ref` and `set_u_ref`, set the initial state with `set_x0`, and then call `solve`. The python interpreter must have access to the newly generated module. This can be done by creating a python file with the following code in the generated directory, for example.

``` py
import numpy as np
import tinympcgen
import matplotlib.pyplot as plt

tinympcgen.set_x_ref(np.array([1.0, 0, 0, 0])) # Set the goal position (1)
tinympcgen.set_x0(np.array([0.5, 0, 0, 0])) # Set first state in horizon
solution = tinympcgen.solve()
```

1. The reference trajectory can also be set for each time step in the horizon, which is what's normally done when tracking a reference trajectory instead of just stabilizing about a point. `set_x_ref` expects the entire trajectory reference to be a numpy array of the shape (nx x N) and `set_u_ref` expects a numpy array of the shape (nu x N-1). You can also just set the reference for a single time step as done here, and the python module will handle expanding it to the entire horizon.


### Build with CMake

Finally, a single top-level CMake file is provided for building an example executable called `tiny_codegen_example`, which has its main function inside `tiny_main.cpp`. To build it, run

``` bash
cd generated_code/build # (1)
cmake ..
cmake --build .
```

1. The build folder should have been generated when TinyMPC built the python module, but if for some reason it did not, run `mkdir build` once inside the generated_code directory.


`tiny_main.cpp` only calls `tiny_solve`, but all of the convenience functions available in the `tiny_api.hpp` header can be used to set the reference trajectory and update the initial state. This should be used as a starting point for integrating TinyMPC with your own project.