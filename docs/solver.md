---
layout: docs/default
math: mathjax
title: The Solver
nav_order: 2
# permalink: /docs/
---

{: .warning }
This website is under construction. It is heavily based on OSQP website.

# TinyMPC Solver Documentation

[Visit our GitHub Discussions page](https://github.com/orgs/TinyMPC/discussions){:target="_blank"} for any questions related to the solver!

The TinyMPC solver is a numerical optimization package for solving convex quadratic model-predictive control programs in the default form

$$
\begin{array}{ll}
  \mbox{minimize} & \frac{1}{2} (x_N - \bar{x}_N)^T Q_f (x_N - \bar{x}_N) + \\
  & \sum_{k=0}^{N} \bigl( \frac{1}{2} (x_k - \bar{x}_k)^T Q (x_k - \bar{x}_k) + \frac{1}{2}(u_k - \bar{u}_k)^T R (u_k - \bar{u}_k) \bigr)\\
  \mbox{subject to} & x_{k+1} = A x_k + B u_k \\
                    & \overline u \le u_k \le \underline u \\
                    & \overline x \le x_k \le \underline x
\end{array}
$$

where $$x_k \in \mathbb{R}^n$$, $$u_k \in \mathbb{R}^m$$ are the state and control input at time step $$k$$, $$N$$ is the number of time steps (also referred to as the horizon), $$A \in \mathbb{R}^{n \times n}$$ and $$B \in \mathbb{R}^{n \times m}$$ define the system dynamics, $$Q \succeq 0$$, $$R \succ 0$$, and $$Q_f \succeq 0$$ are symmetric cost weight matrices and $$\bar{x}_k$$ and $$\bar{u}_k$$ are state and input reference trajectories.

**Code available on** [GitHub](https://github.com/tinympc/tinympc){:target="_blank"}.

## Citing TinyMPC

If you are using TinyMPC for your work, we encourage you to

* [Cite the related papers](citing)
* Put a star on [GitHub](https://github.com/TinyMPC/TinyMPC){:target="_blank"}

**We are looking forward to hearing your success stories with TinyMPC!** Please [share them with us](mailto:khai.nx1201@gmail.com){:target="_blank"}.

## Features (Expected)

### Efficient

It uses a custom ADMM-based first-order method requiring no matrix factorization. All the other operations are extremely cheap. It also implements a Riccati recursion for primal update exploiting structures in the MPC problem.

### Robust

The algorithm is absolutely division free and it requires no assumptions on problem data (the problem only needs to be convex). It just works!

<!-- ### Detects primal / dual infeasible problems

When the problem is primal or dual infeasible, OSQP detects it. It is the first available QP solver based on first-order methods able to do so. -->

### Embeddable

It has an easy interface to generate customized embeddable C code with no memory manager required.

### Dependency-minimal

It only needs Eigen to run.

### Efficiently warm-started

It can be easily warm-started and the matrix factorization can be cached to solve parametrized problems extremely efficiently.

### Interfaces

It provides interfaces to C, C++, Julia, Matlab, Python.

## License

TinyMPC is distributed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)

## Credits

The following people have been involved in the development of TinyMPC:

* [Khai Nguyen]( https://xkhainguyen.github.io/){:target="_blank"} (Carnegie Mellon University): main developer
* [Sam Schoedel](https://samschoedel.com/){:target="_blank"} (Carnegie Mellon University): main developer
* [Anoushka Alavilli](https://www.linkedin.com/in/anoushka-alavilli-89586b178/){:target="_blank"} (Carnegie Mellon University): main developer
* [Zachary Manchester](https://www.linkedin.com/in/zacmanchester/){:target="_blank"} (Carnegie Mellon University): advisor
* [Brian Plancher](https://brianplancher.com/){:target="_blank"} (Barnard College): advisor

## Bug reports and support

Please report any issues via the [Github issue tracker](https://github.com/tinympc/tinympc/issues){:target="_blank"}. All types of issues are welcome including bug reports, documentation typos, feature requests and so on.

## Numerical benchmarks

Numerical benchmarks against other solvers on microcontrollers are available here.