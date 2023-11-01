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

**Carnegie Mellon University, Barnard College**

<sup>*Equal contribution and alphabetically ordered</sup>

[Paper](https://just-the-docs.com){: .btn }
[arXiv](https://just-the-docs.com){: .btn }
[Video](https://just-the-docs.com){: .btn }
[Summary](https://just-the-docs.com){: .btn }
[Code](https://just-the-docs.com){: .btn }

## Abstract

Model-predictive control (MPC) is a powerful tool for controlling highly dynamic robotic systems subject to complex constraints. However, MPC is computationally demanding, and is often impractical to implement on small, resource-constrained robotic platforms. We present TinyMPC, a high-speed MPC solver with a low memory footprint targeting the microcontrollers common on small robots. Our approach is based on the alternating direction method of multipliers (ADMM) and leverages the structure of the MPC problem for efficiency. We demonstrate TinyMPC both by benchmarking against the state-of-the-art solver OSQP, achieving nearly an order of magnitude speed increase, as well as through hardware experiments on a 27 g quadrotor, demonstrating high-speed trajectory tracking and dynamic obstacle avoidance.

## Hardware Comparison

![Hardware Comparison](../assets/images/hardware_comp2.png)

![Hardware Comparison](../assets/images/hardware_comp1.png)

## Microcontroller Benchmarks ↓

![Microcontroller Benchmarks](../assets/images/mcu_bench.png)

## Robot Hardware

![Crazyflie](../assets/images/cf.png)

## Medium-Pace Figure-8 Tracking

<iframe width="840" height="473" src="../assets/videos/fig81.mp4" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Fast-Pace Figure-8 Tracking

<iframe width="840" height="473" src="../assets/videos/fig82.mp4" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Extreme Pose Recovery

<iframe width="840" height="473" src="../assets/videos/fextreme.mp4" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Dynamic Obstacle Avoidance

<iframe width="840" height="473" src="../assets/videos/favoid.mp4" title="youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>