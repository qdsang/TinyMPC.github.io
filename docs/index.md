---
title: Home
description: TinyMPC description and overview
---

# Welcome to TinyMPC's documentation!

[Get Started :material-arrow-right-box:](#){ .md-button } [Read the Paper :simple-arxiv:](https://arxiv.org/abs/2310.16985){ .md-button } [Watch the Video :fontawesome-brands-youtube:](https://github.com/tinympc/){ .md-button }

TinyMPC is a model-predictive controller built for robots with small amounts of computational power. It's lean and fast, allowing it to run on cheap microcontrollers that have limited memory and speed.


## Demos from the paper

### Dynamic obstacle avoidance

TinyMPC runs fast enough to re-linearize constraints at each time step, allowing it to reason about moving obstacles, as it is doing in both videos. The algorithm can additionally handle any number of arbitrary constraints. On the right, for example, it is avoiding the end of the stick while staying in the yz plane.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/favoid.mp4" type="video/mp4">
</video>

### Extreme pose recovery

TinyMPC can handle recovering from extreme initial conditions. In this example, it is compared against three of the [Crazyflie 2.1](https://www.bitcraze.io/products/crazyflie-2-1/)'s stock controllers.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/fextreme.mp4" type="video/mp4">
</video>

### Figure-8 tracking

We compared against the same stock controllers for an infeasible figure-8 tracking task (the time given to complete a single figure-8 could only be met if the drone was much more powerful). TinyMPC and PID were able to stay upright, but TinyMPC's trajectory more closely resembled a figure-8.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/fig82.mp4" type="video/mp4">
</video>

# How it works

TinyMPC's trick is to precompute expensive matrices offline so that only a small amount of computation is required during operation.

The underlying algorithm is the [Alternating Direction Method of Multipliers (ADMM)](https://stanford.edu/~boyd/admm.html), which cycles through four main steps, the 