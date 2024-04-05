---
title: Home
description: TinyMPC description and overview
---

# Welcome to TinyMPC's documentation!

<!-- <img src="media/darkmode-banner.png" width=620 />
![Alt Text](media/darkmode-banner.png) -->
![TinyMPC dark mode banner](media/lightmode-banner.png#only-light){ width=620 }
![TinyMPC light mode banner](media/darkmode-banner.png#only-dark){ width=620 }

<!-- <picture>
  <!-- <source media="(prefers-color-scheme: light)" srcset="media/lightmode-banner.png">
  <source media="(prefers-color-scheme: dark)" srcset="media/lightmode-banner.png"> --/>
  <img media="(prefers-color-scheme: light)" src="media/lightmode-banner.png" width=620>
  <img media="(prefers-color-scheme: dark)" src="media/darkmode-banner.png">
</picture> -->

!!! success "" 

    🏆 TinyMPC has been selected as finalists for Best Conference Paper Award, Best Student Paper Award, and Best Paper Award in Automation at [IEEE ICRA 2024](https://2024.ieee-icra.org/).


TinyMPC is an open-source optimization solver tailored for convex model-predictive control, delivering high speed and low memory footprints. Implemented in pure C/C++ with minimal dependencies, this solver is particularly well-suited for embedded control and robotics applications on resource-constrained platforms. Additionally, we provide user-friendly interfaces for seamless integration with high-level languages such as Python, MATLAB, Julia.

[Get Started :material-arrow-right-box:](get-started/examples.md){.md-button}
[ICRA Paper :simple-arxiv:](https://arxiv.org/pdf/2310.16985.pdf){:target="_blank" .md-button}
[CDC Paper :simple-arxiv:](https://arxiv.org/pdf/2403.18149.pdf){:target="_blank" .md-button}
[Watch the Video :fontawesome-brands-youtube:](https://www.youtube.com/watch?v=NKOrRyhcr6w){:target="_blank" .md-button}

## Robot Demonstrations

Integrating TinyMPC into computationally underpowered robots enables them to execute agile maneuvers and exhibit safe behaviors.

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

TinyMPC outperforms state-of-the-art solvers in terms of speed and memory footprint on microcontroller benchmarks.

<img src="media/icra_bench.png" width=100% />

<img src="media/cdc_bench.png" width=100% />

<img src="media/cdc_bench2.png" width=100% />