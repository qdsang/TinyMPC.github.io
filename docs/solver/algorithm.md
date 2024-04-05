---
title: Algorithm
---

# Inside TinyMPC

!!! note ""

    💡 At its core, our solver is designed to accelerate and compress the ADMM algorithm by exploiting the structure of the MPC problem.

Our 2024 ICRA submission video provides a concise overview of the method:

[Watch the Video :fontawesome-brands-youtube:](https://www.youtube.com/watch?v=NKOrRyhcr6w){:target="_blank" .md-button }

<!-- <video width="80%" preload="auto" muted autoplay controls loop style="border: 0px solid #bbb; border-radius: 10px; width: 80%;">
    <source src="https://www.youtube.com/watch?v=NKOrRyhcr6w" type="video/mp4">
</video> -->

## The Algorithm

The underlying algorithm is the [alternating direction method of multipliers](https://stanford.edu/~boyd/admm.html){:target="_blank"}. TinyMPC reformulates the primal update step - the part that usually takes the longest - as an [LQR problem](https://en.wikipedia.org/wiki/Linear%E2%80%93quadratic_regulator){:target="_blank"}. These have been studied for decades, and we know how to write LQR problems in a closed form: specifically, using [Riccati recursion](https://en.wikipedia.org/wiki/Algebraic_Riccati_equation){:target="_blank"}. We reorganize some of this recursive function to extract big matrices that only need to be computed once. In the vanilla implementation, this restricts TinyMPC to solving only a *linear* trajectory tracking problem (with any kinds of constraints, as long as they can be quickly re-linearized online). However, as seen in our demo videos, a single linearization can go a long way.

## Alternating direction method of multipliers (ADMM)

The alternating direction method of multipliers algorithm was developed in the 1970s and [used in 2011 by researchers at Stanford](https://stanford.edu/~boyd/papers/pdf/admm_distr_stats.pdf){:target="_blank"} to better solve the problem of distributed convex optimization. Some of these researchers later helped in developing [OSQP, the Operator Splitting Quadratic Program solver](https://osqp.org/){:target="_blank"}. TinyMPC takes much of its inspiration from these two sources.

We want to solve optimization problems in which our cost function $f$ and set of valid states $\mathcal{C}$ are both convex:

$$
\begin{alignat}{2}
\min_x & \quad f(x) \\
\text{subject to} & \quad x \in \mathcal{C}.
\end{alignat}
$$

We define an indicator function for the set $\mathcal{C}$:

$$
I_\mathcal{C}(x) =
\begin{cases}
0 & x \in \mathcal{C} \\
\infty & \text{otherwise}.
\end{cases}
$$

The indicator function says simply that there is infinite additional cost when $x$ violates the constraints (the state $x$ is outside the set of valid states $\mathcal{C}$) and zero additional cost for obeying the constraints ($x$ is inside the set $\mathcal{C}$). Thus, we need to be able to determine whether or not a state is in the set $\mathcal{C}$ in order to know if all the constraints on our problem are being met. For speed of computation, this often takes the form $Hx \geq h$ (or $Hx \leq h$, or a combination of $Hx \geq h$ and $Gx \leq g$ (each of these can be rewritten to be equivalent to the others)). This form can describe any kind of linear constraint in $x$. To do obstacle avoidance, for example, it is common to arrange $H$ and $h$ as half-space constraints where, in three dimensions, the entire space is split by a plane and only one half is inside the set $\mathcal{C}$. For arbitrary dimensionality, we say the space is divided by a hyperplane.

We modify the generic optimization problem to include the indicator function by adding it to the cost. We introduce a new state variable $z$, called the slack variable, to describe the constrained version of the original state variable $x$, which we will now call the primal variable.

$$
\begin{alignat}{2}
\min_x & \quad f(x) + I_\mathcal{C}(z) \\
\text{subject to} & \quad x = z.
\end{alignat}
$$

At minimum cost, the primal variable $x$ must be equal to the slack variable $z$, but during each solve they will not necessarily be equal. This is because the slack variable $z$ manifests in the algorithm as the version of the primal variable $x$ that has been projected onto the feasible set $\mathcal{C}$, and thus whenever the primal variable $x$ violates any constraint, the slack variable at that iteration will be projected back onto $\mathcal{C}$ and thus differ from $x$. To push the primal variable $x$ back to the feasible set $\mathcal{C}$, we introduce a third variable, $\lambda$, called the dual variable. This method is referred to as the [augmented Lagrangian](https://en.wikipedia.org/wiki/Augmented_Lagrangian_method){:target="_blank"} (originally named the method of multipliers), and introduces a scalar penalty parameter $\rho$ alongside the dual variable $\lambda$ (also known as a Lagrange multiplier). The penalty parameter $\rho$ is the augmentation to what would otherwise just be the Lagrangian of our constrained optimization problem above. $\lambda$ and $\rho$ work together to force $x$ closer to $z$ by increasing the cost of the augmented Lagrangian the more $x$ and $z$ differ.

$$
\mathcal{L}_A(x,z,\lambda) = f(x) + I_\mathcal{C}(z) + \lambda^\intercal(x-z) + \frac{\rho}{2}\|x-z\|^2_2.
$$

Our optimization problem has now been divided into two variables: the primal $x$ and slack $z$, and we can optimize over each one individually while holding all of the other variables constant. To get the ADMM algorithm, all we have to do is alternate between solving for the $x$ and then for the $z$ that minimizes our augmented Lagrangian. After each set of solves, we then update our dual variable $\lambda$ based on how much $x$ differs from $z$.

$$
\begin{alignat}{3}
\text{primal update: } & x^+ & ={} & \underset{x}{\arg \min} \hspace{2pt} \mathcal{L}_A(x,z,\lambda), \\
\text{slack update: } & z^+ & ={} & \underset{z}{\arg \min} \hspace{2pt} \mathcal{L}_A(x^+,z,\lambda), \\
\text{dual update: } & \lambda^+ & ={} & \lambda + \rho(x^+ - z^+),
\end{alignat}
$$

where $x^+$, $z^+$, and $\lambda^+$ refer to the primal, slack, and dual variables to be used in the next iteration.

Now all we have to do is solve a few unconstrained optimization problems!

## TODO: primal and slack update and discrete algebraic riccati equation

<!--
this is an example of `code` in markdown
<!-- ``` py (or c or cpp) title="<custom title>" { .yaml .no-copy } --/>
``` julia
# This is a function
function function(x):
    return x**2 # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

<!-- 
1.  :man_raising_hand: I'm $\beta$ $\int_5^{3x^2}$ a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.
-->

<!-- 
Hi this is something I am writing. (1)
{.annotate}

1. Hi this is an annotation with $\int_5^{3x^2}\sin(t) dt$, <span style="color:blue">some *colorful* text</span>, and emojis: :material-rocket:
-->