---
title: Home
description: TinyMPC description and overview
---

# Welcome to TinyMPC's documentation!

<!-- <img src="media/darkmode-banner.png" width=620 />
![Alt Text](media/darkmode-banner.png) -->
<p align="center">
  <img width="50%" src="media/lightmode-banner.png#only-light" />
  
</p>
<p align="center">
  <img width="50%" src="media/darkmode-banner.png#only-dark" />
</p>

!!! success "" 

    🏆 TinyMPC has been selected as a finalist for Best Conference Paper Award, Best Student Paper Award, and Best Paper Award in Automation at [IEEE ICRA 2024](https://2024.ieee-icra.org/)! Thank you to everyone who has used TinyMPC and provided feedback!


TinyMPC is an open-source optimization solver tailored for convex model-predictive control, delivering high speed and low memory footprints. Implemented in pure C/C++ with minimal dependencies, this solver is particularly well-suited for embedded control and robotics applications on resource-constrained platforms. Additionally, we provide user-friendly interfaces for seamless integration with high-level languages such as Python, MATLAB, Julia.

[Get Started :material-arrow-right-box:](get-started/examples.md){.md-button}
[ICRA Paper :simple-arxiv:](https://arxiv.org/pdf/2310.16985.pdf){:target="_blank" .md-button}
[CDC Paper :simple-arxiv:](https://arxiv.org/pdf/2403.18149.pdf){:target="_blank" .md-button}
[Watch the Video :fontawesome-brands-youtube:](https://www.youtube.com/watch?v=NKOrRyhcr6w){:target="_blank" .md-button}

## Robot Demonstrations

TinyMPC contributes to bridging the gap between computationally intensive convex model-predictive control and resource-constraint processing platforms. Integrating TinyMPC into computationally underpowered robots enables them to execute agile maneuvers and exhibit safe behaviors.

### Dynamic obstacle avoidance

TinyMPC runs fast enough to enable re-linearizing constraints at each time step, allowing it to reason about moving obstacles, as it is doing in both videos. The algorithm can additionally handle any number of arbitrary linear constraints. On the right, for example, it is avoiding the end of the stick while staying in the yz plane.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/favoid.mp4" type="video/mp4">
</video>

### Extreme pose recovery

TinyMPC can enable recovering from extreme initial conditions. In this example, it is compared against three of the [Crazyflie 2.1](https://www.bitcraze.io/products/crazyflie-2-1/){:target="_blank"}'s stock controllers. Only TinyMPC was able to keep the control inputs under the drone's limits, and the recovery looks pretty good!

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/fextreme.mp4" type="video/mp4">
</video>

### Figure-8 tracking

We compared against the same stock controllers for an infeasible figure-8 tracking task (the time given to complete a single figure-8 could only be met if the drone was much more powerful). TinyMPC and PID were able to stay upright, but TinyMPC's trajectory more closely resembled a figure-8.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/fig82.mp4" type="video/mp4">
</video>

## Microcontroller Benchmarks

TinyMPC outperforms state-of-the-art solvers in terms of speed and memory footprint on microcontroller benchmarks (smaller is better). 


### QP problems 

TinyMPC and OSQP were benchmarked with random QP-based MPC problems of different sizes on a Teensy 4.1 board.

<p align="center">
  <img width="80%" src="media/icra_bench.png" />
</p>

### SOCP problems

Left, TinyMPC and OSQP were benchmarked with QP-based predictive safety filtering problems of different sizes on a STM32F405 Feather board.
Right, TinyMPC, ECOS and SCS were benchmarked with SOCP-based rocket soft-landing MPC problems of different sizes on a Teensy 4.1 board.

<p align="center">
  <img width="80%" src="media/cdc_bench.png" />
</p>

### Early termination 

TinyMPC, ECOS and SCS were benchmarked with SOCP-based rocket soft-landing MPC problems with early termination on a Teensy 4.1 board.

<p align="center">
  <img width="50%" src="media/cdc_bench2.png" />
</p>