# A look at initial data

## physical problem

**Motivation**:

We have spent some time looking at the evolution problem which on the numerical front entailed solution of hyperbolic PDEs subject to elliptic constraints. Initial data we provided through appeal to known, analytical solutions.

What if we don't know initial data but merely a scenario we want to model? Then we must initially solve the constraints somehow. It turns out that there is a whole art to this problem itself - we consider an example here.

**Setup**:

In the conformal transverse-traceless approach one considers splitting the conformal traceless extrinsic curvature $\hat{A}{}^{ij}$ into longitudinal (L)  and transverse-traceless (TT) parts:

$$
\begin{equation*}
  \hat{A}{}^{ij} := \hat{A}_{\mathrm{L}}{}^{ij}
  + \hat{A}{}^{ij}{}_{\mathrm{TT}}
  = \mathbb{L}_{\tilde{\gamma}}[X]{}^{ij} + \hat{A}_{\mathrm{TT}}{}^{ij},
\end{equation*}
$$
where $\tilde{\gamma}{}_{ij} \hat{A}_{\mathrm{TT}}{}^{ij}{} = 0 =%
\tilde{\D}{}_j[\hat{A}_{\mathrm{TT}}{}^{ij}{}]$ and $X{}^k$ is a vector  potential.
We have also introduced the (symmetric and traceless) __conformal Killing operator__:

$$
\begin{equation*}
  \mathbb{L}_{\tilde{\gamma}}[X]{}^{ij}:=
  \tilde{\D}{}^i[X{}^j] + \tilde{\D}{}^j[X{}^i]
  -\frac{2}{3}\tilde{\D}{}_k [X{}^k] \tilde{\gamma}{}^{ij},
\end{equation*}
$$

and one also introduces the __vector Laplacian__:

$$
\begin{equation*}
  \tilde{\D}{}_j[\hat{A}{}^{ij}]
  = \tilde{\D}{}_j [\mathbb{L}_{\tilde{\gamma}}[X]{}^{ij}]
  = \tilde{\D}{}_j [\tilde{\D}{}^j[X{}^i]]
  + \frac{1}{3} \tilde{\D}{}^i[\tilde{\D}{}_j[X{}^j]]
  + \widetilde{\mathrm{Ric}}{}^i_j X{}^j =: \Delta{}_{\tilde{\gamma}}[X{}^i].
\end{equation*}
$$

Under this decomposition the constraints become:

$$
\begin{align}
  \tag{eq:CTTMom}
  \Delta{}_{\tilde{\gamma}}[X{}^i] - \frac{2}{3} \tilde{\D}{}^i[\mathcal{K}]\Psi{}^6
  -8\pi\tilde{j}{}^i &=0,\\
  \tag{eq:CTTHam}
  \tilde{\D}{}_i[\tilde{\D}{}^i[\Psi]]
  - \frac{1}{8}\tilde{\mathcal{R}}\Psi
  + \frac{1}{8}\hat{A}{}_{ij} \hat{A}{}^{ij} \Psi{}^{-7}
  - \frac{1}{12}\mathcal{K}^2 \Psi^5 + 2\pi \tilde{\rho}\Psi{}^{-3} &= 0;
\end{align}
$$

where $(\tilde{\gamma},\,\hat{A}_{\mathrm{TT}}{}^{ij},\,\mathcal{K},\,\rho,\,j{}^i)$ may be  freely prescribed and $(\Psi,\,X{}^i)$ are to be solved for.

Several choices can be made at this juncture, depending on the type of problem. Here we focus on the so-called **Bowen-York** (BY) class of solutions describing different types of black hole configurations. Thus we assume that we work in vacuum such that $\rho=0=j{}^i$, assume maximal slicing $\mathcal{K}=0$, and for simplicity suppose that $\hat{A}_{\mathrm{TT}}$ vanishes. Finally, we consider conformally flat data $\tilde{\gamma}{}_{ij}=\delta{}_{ij}$.

The constraints Eq.(eq:CTTMom) and Eq.(eq:CTTHam) reduce to:
$$
\begin{align}
  \tag{eq:CTTMomD}
  \Delta{}_{\tilde{\gamma}}[X{}^i]&=0,\\
  \tag{eq:CTTHamD}
  \tilde{\D}{}_i[\tilde{\D}{}^i[\Psi]] + \frac{1}{8}\hat{A}{}_{ij} \hat{A}{}^{ij} \Psi{}^{-7}&= 0;
\end{align}
$$

and consequently may be solved one-by-one.

Focusing on Eq.(eq:CTTMomD) we have:
 $$
\begin{align*}
     \Delta{}_{\tilde{\gamma}}[X{}^i] =0 &= \tilde{\D}{}_j[\hat{A}{}^{ij}] = \tilde{\D}{}_j[\mathbb{L}{}_{\tilde{\gamma}}[X]{}^{ij}],\\
     &=\tilde{\D}{}_j[\tilde{\D}{}^j[X{}^i]] + \frac{1}{3}\tilde{\D}{}^i[\tilde{\D}{}_j[X{}^j]] + \underbrace{\widetilde{\mathrm{Ric}}{}^i_j}_{=0} X{}^j;
\end{align*}
$$
and for Cartesian coordinates we find reduction to:
$$
\begin{equation*}
  \partial{}^j[\partial{}_j[X{}^i]] + \frac{1}{3}\partial{}^i[\partial{}_j[X{}^j]]=0.
\end{equation*}
$$

Introduce a vector field $l{}^i$ pointing away from a coordinate coordinate location $x{}^i_\mathrm{BH}$ (a black hole centre, say):

$$
\begin{aligned}
  l{}^i &:= \frac{x{}^i-x{}^i_\mathrm{BH}}{s}, &
  s&:= \sqrt{(x_i-x{}^{\mathrm{BH}}_i)(x{}^i-x{}^i_\mathrm{BM})}.
\end{aligned}
$$

It may be verified that:

$$
\begin{equation}\tag{eq:solX}
  X{}^i = -\frac{1}{4s}\left(7P{}^i + l{}^i l{}_j P{}^k \right),
\end{equation}
$$

satisfies the reduced momentum constraint in Cartesian coordinates above where $P{}^i$ plays the role of a (constant) linear momentum.

**Notes**:
- This is not the only possible solution for $X{}^i$.
- The equation is linear with our assumptions and hence could be superposed with other solutions.
- For later reference Eq.(eq:solX) translates to:

$$
\begin{equation}\tag{eq:BYAL}
  \hat{A}{}^{ij}_\mathrm{L}=
  \frac{3}{2s^2}
  \left(
    P{}^i l{}^j + P{}^j l{}^i
    -[\delta{}^{ij}-l{}^il{}^j]l{}_k P{}^k
  \right).
\end{equation}
$$

This deals with the momentum constraint but what about the Hamiltonian constraint?

In particular given $\hat{A}{}^{ij}_\mathrm{L}$ as above how do we approach solution of:

$$
\begin{equation}
\tilde{\D}{}_i[\tilde{\D}{}^i[\Psi]] + \frac{1}{8}\hat{A}{}_{ij} \hat{A}{}^{ij} \Psi{}^{-7} = 0.
\end{equation}
$$

## numerical problem

Equation (eq:CTTHamD) is of elliptic character albeit *non-linear*; there is also a question of _regularity_ (notice the negative power), and, one should always keep in mind questions of solution uniqueness.

### non-linearity
For the non-linearity one way to proceed is through linearization and iterative improvement via a sequence of succesively better approximants to the original non-linear problem.

Consider (schematically):

$$
\begin{equation}\tag{eq:nlschem}
  \D^2[f] = h[f],
\end{equation}
$$

with $h[f]$ considered to be a (non)-linear functional of $f$. Put $f{}^{[n+1]}:=f{}^{[n]}+\delta f$ where $n$ serves to label the $n^\th$ iterate. Suppose $\delta f\ll f^{[n]}$. We can (formally) expand, to linear order, the $(n+1)^\th$ iteration for $h$ about the $n^\th$:

$$
\begin{equation}
  h\left[f^{[n+1]}\right] =
  h\left[f{}^{[n]} + \delta f\right]=
  h\left[f{}^{[n]} \right] + (\delta f)  h'\left[
  f{}^{[n]}\right] + \mathcal{O}(\delta f^2),
\end{equation}
$$

where $h'=\partial h / \partial f$. Replace $f$ with $f{}^{[n+1]}$ in Eq.(eq:nlschem) to obtain:

$$
\begin{equation}
  \D^2[\delta f] - (\delta f) h'\left[ f{}^{[n]}\right]
  = -\D^2\left[f{}^{[n]}\right]
  + h\left[f{}^{[n]}\right].
\end{equation}
$$

Define the _residual_ of the $n^\th$ iteration as the difference:

$$
\begin{equation}
  \mathrm{R}{}^{[n]} := \D^2\left[f{}^{[n]} \right]
  -h\left[f{}^{[n]} \right],
\end{equation}
$$

which allows us to write:

$$
\begin{equation}\tag{eq:linschem}
  \D^2[\delta f] - (\delta f) h'\left[ f{}^{[n]}\right]
  = -\mathrm{R}{}^{[n]},
\end{equation}
$$

which is a linear elliptic equation for $\delta f$ that we can solve directly.

**summary**:
- **(I)**: Set $n=0$. Choose initial iterate $f{}^{[0]}$.
- **(II)**: Given a current $n$ and consequently $f{}^{[n]}$ compute $\mathrm{R}{}^{[n]}$ and $h'\left[ f{}^{[n]}\right]$ then solve Eq.(eq:linschem) for $\delta f$.
- **(III)**: Compute $f{}^{[n+1]}=f{}^{[n]}+\delta f$.
- Repeat **(II)** and **(III)** until the residual $\mathrm{R}{}^{[n]}$ drops to a desired level.

For "sufficiently nice" operators and inhomogeneities in Eq.(eq:nlschem) the corrections $\delta f$ will decrease and we will find a solution to the original non-linear problem.

## regularity

Consider now our target problem of Eq.(eq:CTTHamD) with BY data. In order for the previously described algorithm to converge in the form described we need to work with regular (finite) solutions.

Observe that close to each black hole centre $x{}^i_\mathrm{BH}$ (henceforth referred to as a puncture) the conformal factor is dominated by a term of the form $\psi\simeq \mathcal{M}/s$. The term $\mathcal{M}$ is the so-called puncture mass. 

Recall that according to our definition $\lim_{x{}^i\rightarrow x{}^i_\mathrm{BH}} s=0$. In other words $\psi$ blows up in the vicinity of a puncture.

In light of Eq.(eq:BYAL) we see that the term $\hat{A}_{ij} \hat{A}{}^{ij}$ diverges at most as fast as $\propto s^{-4}$ which in turn is suppressed by the $\psi^{-7}\propto s^7$. Consequently, near the BH the product  $\hat{A}_{ij} \hat{A}{}^{ij}\psi^{-7}$ must vanish.

This motivates us to split off the (analytically determined) singular behaviour off before attacking the problem numerically. Specifically we make the ansatz:

$$
\begin{equation}
  \psi:=1 + \frac{1}{\alpha} + u,
\end{equation}
$$

where $1/\alpha$ carries the singular behaviour and is defined through (allowing multiple punctures):

$$
\begin{equation}
  \frac{1}{\alpha} = \sum_n \frac{\mathcal{M}_n}{2s_n},
\end{equation}
$$

and $u$ carries the (regular) correction.

Substitution into Eq.(eq:CTTHamD) leads to the following equation for $u$:

$$
\begin{equation}\tag{eq:corrnlHamD}
  \D^2[u] = -\beta(\alpha+\alpha u + 1)^{-7},
\end{equation}
$$

where we have set:

$$
\begin{equation}
  \beta := \frac{1}{8} \alpha^7 \hat{A}{}^L_{ij} \hat{A}{}_L^{ij}.
\end{equation}
$$

Clearly Eq.(eq:corrnlHamD) is of the form of Eq.(eq:nlschem). Let's map it to the specific form of the algorithm we wrote down.

We identify $f$ with $u$ and obtain:

$$
\begin{equation}
  h(f) = h(u) = -\beta(\alpha+\alpha u + 1)^{-7}.
\end{equation}
$$

Our equation is non-linear in $u$ and the iterative procedure is carried out as $u{}^{[n+1]}=u{}^{[n]} + \delta u$. For reference, notice that:

$$
\begin{equation}
  h'\left[u{}^{[n]} \right]
  =
  7\alpha\beta
  \left(\alpha+\alpha u{}^{[n]}+1\right)^{-8}.
\end{equation}
$$

## code

We consider construction of puncture initial data for a single black hole in `puncture.py` . The usual comments on clarity over efficiency apply for the implementation. Here the approach taken to to specify things as directly as possible. From the `python3` point of view, this time we demonstrate how `class` objects can be useful in structuring code.

### final concerns
- Suppose we wish to numerically solve Eq.(eq:corrnlHamD). Fix a uniform sampling in $(x,\,y,\,z)$ and consequently uniform grid-spacing $\Delta$. We may discretize the $\D^2[u]$ operator through:
$$
\begin{aligned}
  (\D^2[u]){}_{ijk} &=
  (\partial{}_x^2[f]){}_{ijk}
  +(\partial{}_y^2[f]){}_{ijk}
  +(\partial{}_z^2[f]){}_{ijk},\\
  &=\frac{1}{\Delta^2}
  \Big[
  u{}_{i+1,j,k}
  +u{}_{i-1,j,k}
  +u{}_{i,j+1,k}
  +u{}_{i,j-1,k}
  \\
  &
  +u{}_{i,j,k+1}+u{}_{i,j,k-1}-6u{}_{ijk}\Big],
\end{aligned}
$$
which follows from combining dimension-by-dimension the familiar $1^\d$ stencils.

- The domain we solve over will be a cube ${\Omega}:=[-x_M,\,x_M]^3$. For the grid itself we adopt uniform, cell-centered sampling in $(x,\,y,\,z)$.

- While we have dealt with prescribing the system, together with discretization strictly speaking we have only identified what to do on the interior $\overset{\circ}{\Omega}$ and we still need to say something about the boundary $\partial\Omega$.

- To this end we consider adopting so-called _Robin_ boundary conditions which will force $u$ to drop off with inverse distance from the origin. That is $r u=\mathrm{const}$ as $r\rightarrow\infty$ (or $s$ if you prefer).
- A simple way to impose this is to set $ru$ on the boundary equal to its value just inside the boundary; e.g. we put $x_0 u{}_{0jk}-x_1 u{}_{1jk}=0$.

## further reading

The books of Baumgarte & Shapiro have some nice discussion (the code example is adapted from there).