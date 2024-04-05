---
title: Installation
description: Install TinyMPC
---

# How to Install TinyMPC

We offer user-friendly interfaces in high-level languages to enable low-level C++ code generation and verification, making them ready for deployment on embedded hardware. We also provide various robotic control examples, including the Crazyflie nano-quadrotor. 

Check out our GitHub repositories: [Python](https://github.com/TinyMPC/tinympc-python), [MATLAB](https://github.com/TinyMPC/tinympc-matlab), [Julia](https://github.com/TinyMPC/tinympc-julia)

To get started simply choose your language interface and follow the easy installation instructions below:

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
    #include <iostream>

    int main(void) {
    std::cout << "Hello world!" << std::endl;
    return 0;
    }
    ```

=== "MATLAB"

    ``` matlab
    #include <iostream>

    int main(void) {
    std::cout << "Hello world!" << std::endl;
    return 0;
    }
    ```