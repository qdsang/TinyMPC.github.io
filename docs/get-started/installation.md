---
title: Installation
description: Install TinyMPC
---

# How to install TinyMPC

We offer user-friendly interfaces in high-level languages to enable low-level C++ code generation and verification, making them ready for deployment on embedded hardware. We also provide various [robotic control examples](examples.md), including the Crazyflie nano-quadrotor.

Check out our GitHub repositories for implementation details: [C++](https://github.com/TinyMPC/TinyMPC), [Python](https://github.com/TinyMPC/tinympc-python), [MATLAB](https://github.com/TinyMPC/tinympc-matlab), [Julia](https://github.com/TinyMPC/tinympc-julia)

Visit our [GitHub Discussions](https://github.com/TinyMPC/discussions) page for any questions related to the solver!

---

To get started simply choose your language interface and follow the easy installation instructions below (tested on Ubuntu):

=== "C++"

    Clone the GitHub repository 

    `git clone https://github.com/TinyMPC/TinyMPC.git`

    Navigate to root directory and run

    `cd TinyMPC && mkdir build && cd build`

    Run CMake configure step

    `cmake ..`

    Build TinyMPC
    
    `cmake --build .`

    Run an example

    `./examples/quadrotor_hovering`

=== "Python"

    Clone the GitHub repository with submodule

    `git clone --recurse-submodules https://github.com/TinyMPC/tinympc-python.git`

    Install the package

    `cd tinympc-python & pip install -e .`

    Run the `interactive_cartpole.ipynb` example

=== "Julia"

    Clone the GitHub repository with submodule

    `git clone --recurse-submodules https://github.com/TinyMPC/tinympc-julia.git`

    Run the `interactive_cartpole_ext.ipynb` example

=== "MATLAB"

    Clone the GitHub repository with submodule

    `git clone --recurse-submodules https://github.com/TinyMPC/tinympc-matlab.git`

    Run the `interactive_cartpole.mlx` example
