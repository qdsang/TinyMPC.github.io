---
title: Installation
description: Install TinyMPC
---

# Installing TinyMPC

A python interface is available that allows for [direct usage](./examples.md/#setup-problem) of TinyMPC. The interface can also be used to [generate C++ code](./examples.md/#code-generation) and an associated python module which allows for quick testing before integrating the generated code with your project. We provide examples for a few robots and have [firmware](https://github.com/RoboticExplorationLab/tinympc-crazyflie-firmware) for running TinyMPC on the Crazyflie 2.1 quadrotor.

Source code is [here](https://github.com/TinyMPC/TinyMPC). Check out our other GitHub repositories for interface implementation details: [Python](https://github.com/TinyMPC/tinympc-python), [Julia](https://github.com/TinyMPC/tinympc-julia), [MATLAB](https://github.com/TinyMPC/tinympc-matlab).

Visit our [GitHub Discussions](https://github.com/TinyMPC/discussions) page for any questions related to the solver!

---

## Install from PyPI

!!!note "Currently only available on Linux operating systems"

``` bash
pip install --upgrade tinympc
```

Go to the [examples](./examples.md) page to see how to use TinyMPC.

<!-- To get started simply choose your language interface and follow the installation instructions (tested on Ubuntu 22.04): -->


<!-- 
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

    Run the `interactive_cartpole.mlx` example -->

---

## Build from source

If you'd like to build from source, you can do so by following these steps: 

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
