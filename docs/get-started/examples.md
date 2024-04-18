---
title: Examples
description: TinyMPC examples
---

# How to use TinyMPC

We provide various robotic control examples, including the Crazyflie nano-quadrotor, in high-level language interfaces. Make sure you are able to [install the package](installation.md).

Check out our GitHub repositories for implementation details: [C++](https://github.com/TinyMPC/TinyMPC), [Python](https://github.com/TinyMPC/tinympc-python), [MATLAB](https://github.com/TinyMPC/tinympc-matlab), [Julia](https://github.com/TinyMPC/tinympc-julia)

Visit our [GitHub Discussions](https://github.com/TinyMPC/discussions) page for any questions related to the solver!

---

To get started simply choose your language interface and follow the instructions below (tested on Ubuntu):

## Load the library

=== "Python"

    ``` py
    import tinympc
    import numpy as np

    tinympc_python_dir = "/path/to/tinympc-python"
    tinympc_dir = tinympc_python_dir + "/tinympc/TinyMPC"

    prob = tinympc.TinyMPC()
    prob.compile_lib(tinympc_dir)

    os_ext = ".so" # (1)
    lib_dir = tinympc_dir + "/build/src/tinympc/libtinympcShared" + os_ext  # Path to the compiled library
    prob.load_lib(lib_dir)
    ```

    1. Change this based on your OS! Linux: .so, Mac: .dylib, Windows: .dll

=== "Julia"

    ``` julia
    TODO
    ```

=== "MATLAB"

    ``` matlab
    TODO
    ```

=== "C++"

    ``` cpp
    TODO
    ```

## Set up the problem

[Learn how to obtain discrete, linearized system dynamics](./model.md).

=== "Cart-pole"

    For the cart-pole, we use the linearized model of the discretized cart-pole dynamics to stabilize about the upright position.

    === "Python"

        ``` py
        n = 4  # states: x, xdot, theta, thetadot
        m = 1  # controls: force on cart
        N = 10  # horizon

        A = [ # row-major order (1)
            1, 0, 0, 0, 
            0.01, 1, 0, 0, 
            2.2330083403-5, 0.0044662105, 1.0002605176, 0.0521057900,
            7.4430379746-8, 2.2330083403-5, 0.0100008683, 1.0002605176
        ]
        B = [ # row-major order
            7.4683685627-5,
            0.0149367653,
            3.7976332318-5,
            0.0075955962
        ]

        Q = [10.0, 1, 10, 1]  # diagonal elements in row-major order
        R = [1.0]  # diagonal elements in row-major order
        rho = 0.1  # ADMM penalty parameter

        x_min = [-5.0] * n * N  # state constraints
        x_max = [5.] * n * N  # state constraints
        u_min = [-5.] * m * (N - 1)  # force constraints
        u_max = [5.] * m * (N - 1)  # force constraints

        abs_pri_tol = 1.0e-3  # absolute primal tolerance
        abs_dual_tol = 1.0e-3  # absolute dual tolerance
        max_iter = 100  # maximum number of iterations
        check_termination = 1  # how often termination conditions are checked

        # Setup problem data
        prob.setup(n, m, N, A, B, Q, R, x_min, x_max, u_min, u_max, rho,
            abs_pri_tol, abs_dual_tol, max_iter, check_termination)
        ```

        1. In the future, A and B will be matrices and row/column-major ordering will be handled inside prob.setup

    === "Julia"

        ``` julia
        TODO
        ```

    === "MATLAB"

        ``` matlab
        TODO
        ```

    === "C++"

        ``` cpp
        TODO
        ```

=== "Quadrotor"

    For the quadrotor, we start with the full, continuous dynamics, then discretize and linearize about hover.

    === "Python"

        ``` py
        n = 4  # states: x, xdot, theta, thetadot
        m = 1  # controls: force on cart
        N = 10  # horizon

        A = [ # row-major order (1)
            1, 0, 0, 0, 
            0.01, 1, 0, 0, 
            2.2330083403-5, 0.0044662105, 1.0002605176, 0.0521057900,
            7.4430379746-8, 2.2330083403-5, 0.0100008683, 1.0002605176
        ]
        B = [ # row-major order
            7.4683685627-5,
            0.0149367653,
            3.7976332318-5,
            0.0075955962
        ]

        Q = [10.0, 1, 10, 1]  # diagonal elements in row-major order
        R = [1.0]  # diagonal elements in row-major order
        rho = 0.1  # ADMM penalty parameter

        x_min = [-5.0] * n * N  # state constraints
        x_max = [5.] * n * N  # state constraints
        u_min = [-5.] * m * (N - 1)  # force constraints
        u_max = [5.] * m * (N - 1)  # force constraints

        abs_pri_tol = 1.0e-3  # absolute primal tolerance
        abs_dual_tol = 1.0e-3  # absolute dual tolerance
        max_iter = 100  # maximum number of iterations
        check_termination = 1  # how often termination conditions are checked

        # Setup problem data
        prob.setup(n, m, N, A, B, Q, R, x_min, x_max, u_min, u_max, rho,
            abs_pri_tol, abs_dual_tol, max_iter, check_termination)
        ```

        1. In the future, A and B will be matrices and row/column-major ordering will be handled inside prob.setup

    === "Julia"

        ``` julia
        TODO
        ```

    === "MATLAB"

        ``` matlab
        TODO
        ```

    === "C++"

        ``` cpp
        TODO
        ```

## Generate solver code

We generated low-level C++ code ready for deployment on embedded hardware.

=== "Python"

    ``` py
    output_dir = tinympc_python_dir + "/generated_code"  # Path to the generated code
    prob.tiny_codegen(tinympc_dir, output_dir)
    prob.compile_lib(output_dir)

    prob.load_lib(output_dir + "/build/tinympc/libtinympcShared" + os_ext)  # Load the library
    ```

=== "Julia"

    ``` julia
    TODO
    ```

=== "MATLAB"

    ``` matlab
    TODO
    ```

=== "C++"

    ``` cpp
    TODO
    ```

## Interact with solver code

We can also verify our program by interacting in high-level languages before deployment. This naturally provides a convenient software-in-the-loop (SIL) testing pipeline. Below is an example of running MPC in simulation, you can use any simulators.

=== "Python"

    ``` py
    x = [0.0] * n * N  # Initial state
    u = [0.0] * m * (N - 1)  # List of control inputs in horizon
    x_all = []  # List of all stored states
    x_noise = x * 1
    # Matrices for simulation
    Anp = np.array(A).reshape((n, n)).transpose()
    Bnp = np.array(B).reshape((n, m))

    print("=== START INTERACTIVE MPC ===")

    NSIM = 300
    for i in range(NSIM):
        # 1. Set initial state from measurement    
        prob.set_x0(x_noise, 0)  # Set initial state to C code
        
        # 2. Set the reference state if needed    

        # 3. Solve the problem
        prob.solve(0)  # Call the solve in C code

        # 4. Get the control input
        prob.get_u(u, 0)  # Get the control input from C code

        # 5. Simulate the dynamics    
        x = Anp@np.array(x).reshape((n, 1))+ Bnp*np.array(u[0]) 

        noise = np.random.normal(0, 0.01, (n, 1))
        x_noise = x + noise
        # print(f"X = {x}")
        x = x.reshape(n).tolist() 
        x_noise = x_noise.reshape(n).tolist() 
        # print(f"X = {x}")
        x_all.append(x)

    print((x_all))
    ```

=== "Julia"

    ``` julia
    TODO
    ```

=== "MATLAB"

    ``` matlab
    TODO
    ```

=== "C++"

    ``` cpp
    TODO
    ```
