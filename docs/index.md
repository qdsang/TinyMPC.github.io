---
layout: docs/default
math: mathjax
title: Home
nav_order: 1
permalink: /docs/
---

# TinyMPC Solver Documentation

[Visit our GitHub Discussions page](https://github.com/orgs/TinyMPC/discussions) for any questions related to the solver!

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

