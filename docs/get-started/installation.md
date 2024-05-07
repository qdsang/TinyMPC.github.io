---
title: Installation
description: Install TinyMPC
---

# How to install TinyMPC

We offer user-friendly interfaces in high-level languages to enable low-level C++ code generation and verification, making them ready for deployment on embedded hardware. We provide [examples](examples.md) for a few robots and have [firmware](https://github.com/RoboticExplorationLab/tinympc-crazyflie-firmware) for running TinyMPC on the Crazyflie 2.1 quadrotor.

Check out our GitHub repositories for implementation details: [C++](https://github.com/TinyMPC/TinyMPC), [Python](https://github.com/TinyMPC/tinympc-python), [Julia](https://github.com/TinyMPC/tinympc-julia), [MATLAB](https://github.com/TinyMPC/tinympc-matlab).

Visit our [GitHub Discussions](https://github.com/TinyMPC/discussions) page for any questions related to the solver!

---

To get started simply choose your language interface and follow the installation instructions (tested on Ubuntu 22.04):

=== "Python"

    Make sure you have an up-to-date version of pip, then

    ```bash
    pip install tinympc
    ```
    
    Go to the [examples](./examples.md) page to see how to use TinyMPC.

=== "Julia"

    !!! warning "The Julia interface is still under development. Do not expect correct behavior."

    Clone the GitHub repository with submodules

    `git clone --recurse-submodules https://github.com/TinyMPC/tinympc-julia.git`

    Run the `interactive_cartpole_ext.ipynb` example
    
=== "MATLAB"

    !!! warning "The MATLAB interface is still under development. Do not expect correct behavior."

    Clone the GitHub repository with submodules

    `git clone --recurse-submodules https://github.com/TinyMPC/tinympc-matlab.git`

    Run the `interactive_cartpole.mlx` example


## Build from source

If you'd rather build from source, you can do so by following these steps: 


Clone the repository and build the project

```bash
git clone https://github.com/TinyMPC/TinyMPC.git
cd TinyMPC
mkdir build
cd build
cmake ..
cmake --build .
```

Run an example from the build directory

```bash
./examples/quadrotor_hovering
```
