---
title: Home
description: TinyMPC description and overview
---

# Welcome to TinyMPC's documentation!

TinyMPC is a model-predictive controller built for robots with small amounts of computational power. It's lean and fast, allowing it to run on cheap microcontrollers that have limited memory and speed.

[Get Started :material-arrow-right-box:](#){.md-button}
[Original Paper :simple-arxiv:](https://arxiv.org/pdf/2310.16985.pdf){:target="_blank" .md-button}
[Conic Code Gen Paper :simple-arxiv:](https://arxiv.org/pdf/2403.18149.pdf){:target="_blank" .md-button}
[Watch the Video :fontawesome-brands-youtube:](https://www.youtube.com/watch?v=NKOrRyhcr6w){:target="_blank" .md-button}

## Demos

### Dynamic obstacle avoidance

TinyMPC runs fast enough to re-linearize constraints at each time step, allowing it to reason about moving obstacles, as it is doing in both videos. The algorithm can additionally handle any number of arbitrary constraints. On the right, for example, it is avoiding the end of the stick while staying in the yz plane.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/favoid.mp4" type="video/mp4">
</video>

### Extreme pose recovery

TinyMPC can handle recovering from extreme initial conditions. In this example, it is compared against three of the [Crazyflie 2.1](https://www.bitcraze.io/products/crazyflie-2-1/){:target="_blank"}'s stock controllers. Only TinyMPC was able to keep the control inputs under the drone's limits, and the recovery looks pretty good!

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/fextreme.mp4" type="video/mp4">
</video>

### Figure-8 tracking

We compared against the same stock controllers for an infeasible figure-8 tracking task (the time given to complete a single figure-8 could only be met if the drone was much more powerful). TinyMPC and PID were able to stay upright, but TinyMPC's trajectory more closely resembled a figure-8.

<video width="100%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 100%;">
    <source src="media/fig82.mp4" type="video/mp4">
</video>
