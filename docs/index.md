---
layout: docs/default
math: mathjax
title: Home
nav_order: 1
permalink: /docs/
---

# TinyMPC: Model-Predictive Control on Resource-Constrained Microcontrollers

[Anoushka Alavilli* ](https://www.linkedin.com/in/anoushka-alavilli-89586b178/),
[Khai Nguyen* ](https://xkhainguyen.github.io/), 
[Sam Schoedel* ](https://samschoedel.com/), 
[Brian Plancher ](https://brianplancher.com/), 
[Zachary Manchester ](https://www.linkedin.com/in/zacmanchester/)

Carnegie Mellon University, Barnard College

<sup>*Equal contribution and alphabetically ordered</sup>

[Paper]() \| [arXiv]() \| [Video]() \| [Summary]() \| [Code]()

## Abstract

Model-predictive control (MPC) is a powerful tool for controlling highly dynamic robotic systems subject to complex constraints. However, MPC is computationally demanding, and is often impractical to implement on small, resource-constrained robotic platforms. We present TinyMPC, a high-speed MPC solver with a low memory footprint targeting the microcontrollers common on small robots. Our approach is based on the alternating direction method of multipliers (ADMM) and leverages the structure of the MPC problem for efficiency. We demonstrate TinyMPC both by benchmarking against the state-of-the-art solver OSQP, achieving nearly an order of magnitude speed increase, as well as through hardware experiments on a 27 g quadrotor, demonstrating high-speed trajectory tracking and dynamic obstacle avoidance.

## A comparison of micro, tiny, and full-scale robot platforms and their associated computational hardware.
