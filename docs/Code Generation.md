---
layout: default
title: Code Generation
nav_order: 5
has_children: no
---

# Code Generation

TinyMPC can generate tailored C code that compiles into a fast and reliable solver for the given family of convex MPC problems in which the problem data, but not its dimensions, change between problem instances.

The generated code is:

### Malloc-free
It does not perform any dynamic memory allocation.

### Dependency-minimal
It is only linked to Eigen library.

### Division-free
There are no division required in the ADMM algorithm

{: .note }
Please check interactive examples in [Get Started](/docs/get-started/get-started/) for how to use code-generation in different languages.
