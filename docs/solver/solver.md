---
title: Inside TinyMPC
---

# Inside TinyMPC

!!! note ""

    :fontawesome-solid-microchip: At its core, TinyMPC accelerates and compresses the ADMM algorithm by exploiting the structure of the MPC problem.

Our 2024 ICRA submission video provides a concise overview of the solver:

[Watch the Video :fontawesome-brands-youtube:](https://www.youtube.com/watch?v=NKOrRyhcr6w){:target="_blank" .md-button}

## Problem formulation

TinyMPC solves convex quadratic model-predictive control programs of the form

$$
\begin{array}{ll}
  \mbox{minimize} & \sum_{k=0}^{N-1} \frac{1}{2} (x_k - \bar{x}_k)^T Q (x_k - \bar{x}_k) + \frac{1}{2}(u_k - \bar{u}_k)^T R (u_k - \bar{u}_k) \\
  \mbox{subject to} & x_{0} = x_{\text{init}},  \\
                    & x_{k+1} = A x_k + B u_k, \\
                    & u_k^l \le u_k \le u_k^u, \\
                    & x_k^l \le x_k \le x_k^u,
\end{array}
$$

where $x_k \in \mathbb{R}^n$, $u_k \in \mathbb{R}^m$ are the state and control input at time step $k$, $N$ is the number of time steps (also referred to as the horizon), $A \in \mathbb{R}^{n \times n}$ and $B \in \mathbb{R}^{n \times m}$ define the system dynamics, $Q \succeq 0$, $R \succ 0$, and $Q_f \succeq 0$ are symmetric cost weight matrices and $\bar{x}_k$ and $\bar{u}_k$ are state and input reference trajectories.

## Algorithm

TODO

## Implementations

The TinyMPC library offers a C++ implementation of the algorithm mentioned above, along with [interfaces to several high-level languages](../get-started/examples.md). This integration allows these languages to effectively solve optimal control problems using TinyMPC. 

There are also several community-developed implementations of this algorithm: [Rust](https://github.com/peterkrull/tinympc-rs)

Numerical benchmarks against other solvers on microcontrollers are available at [this repository](https://github.com/RoboticExplorationLab/mcu-solver-benchmarks).