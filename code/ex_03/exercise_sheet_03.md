# maximal slicing

## exercise 1.1: Maximal slicing of Schwarzschild 
The 3+1 decomposition can be performed with different choices for the slicing of spacetime.
The choice of time slicing amounts to making a choice for the lapse 
$\alpha$ by either prescribing a function or an equation. Since $\alpha$ can vary depending on the position on the spatial slice, the proper time is allowed to advance at different rates at different points on a given slice. 
A common choice is the _maximal slicing_ condition:

$$
\begin{equation}\tag{eq:maxslicecond}
 K = 0.
\end{equation}
$$

If we want maximal slicing to hold at all times, then we should impose
$\partial_t K = 0$ as well.
In this case, the evolution equation for the extrinsic curvature scalar reduces to an elliptic equation for the lapse function

$$
\begin{equation}
 D_iD^i \alpha = \alpha \left(K_{ij} K^{ij}\right).
\end{equation}
$$

  * [**Step 1**]: In Schwarzschild coordinates, consider $\bar{t} = t + h(r)$ and enforce $K=0$. Find the family of time independent slicings. 
  * [**Step 2**]: From the general result in [**Step 1**], recover the specific solutions for Schwarzschild and isotropic metric.
  * [**Step 3**]: Draw the Kruskal-Szekeres diagrams for the Schwarzschild and the isotropic slicings.
  * [**Step 4**]: Draw the embedding diagram.

## (soln) exercise 1.1

There are many ways to get the required equation. In order to reduce some of the effort involved in the computation we proceed as follows.

As a preliminary note that in $3+1$ decomposition the ambient metric can be written in the form:

$$
\begin{align*}
  \d{s}^2 = -\alpha^2\d{t}^2 + \gamma_{ij}(\d{x}^i + \beta^i \d{t})(\d{x}^j + \beta^j \d{t});
\end{align*}
$$

or:

$$
\begin{align}\tag{eq:metrDecEx3}
  g{}_{ab} =& \begin{bmatrix}
  -\alpha{}^2 + \beta{}_l \beta{}^l & \beta{}_i\\
  \beta{}_j & \gamma{}_{ij}
  \end{bmatrix}.
\end{align}
$$

Furthermore:

$$
\begin{align*}
  n^a=&(\alpha^{-1},\,-\alpha^{-1}\beta^i), &
  n_a=&(-\alpha,\,0,\,0,\,0);
\end{align*}
$$

and

$$
\begin{align*}
 \beta{}^a = (0,\,\beta{}^i).
\end{align*}
$$

Put $\mu(r):=1-2m/r$, then, the standard form of the Schwarzschild solution takes the form:

$$
\begin{equation}\tag{eq:solnStdSS}
  \mathrm{d}s^2 = - \mu(r)\mathrm{d}t^2 + \frac{1}{\mu(r)} \mathrm{d}r^2 + r^2 \mathrm{d}\Omega^2.
\end{equation}
$$

As written, we are working with the so-called "areal" radius. The nomenclature is due to $r$ being related to the area $\mathcal{A}$ of a spherical surface at $r$ centred on the black hole according to the Euclidean expression $r=(\mathcal{A}/(4\pi))^{1/2}$.

The time coordinate is to be mapped as:

$$
\begin{equation}
  t\mapsto \overline{t}=t+h(r).
\end{equation}
$$

The interpretation here is that $h(r)$ is in a sense a kind of "height-function" measuring how far $\overline{t}=\mathrm{const}$ surfaces "lift-off" the usual $t=\mathrm{const}$ surfaces.

With the reparametrization Eq.(eq:solnStdSS) becomes:

$$
\begin{align}\nonumber
  \mathrm{d}s^2 &= -\mu(r) \mathrm{d}\overline{t}^2
  +2\mu(r) h'(r) \mathrm{d}\overline{t} \mathrm{d} r\\
  &+\left(\frac{1}{\mu(r)} - \mu(r) (h'(r))^2 \right) \mathrm{d}r^2
  +r^2 \mathrm{d}\Omega^2.
  \tag{eq:solnStdSSRepar}
\end{align}
$$

Comparing to the standard form of $3+1$ decomposition in Eq.(eq:metrDecEx3) we see:

$$
\begin{align*}
  \beta{}_{i} =& \mu(r) h'(r) (1,\,0,\,0), &
  -\alpha{}^2 + \beta{}_l\beta{}^l =& -\mu(r);
\end{align*}
$$

$$
\begin{align*}
  \gamma{}_{ij} = \mathrm{diag}\left(
    \frac{1}{\mu(r)} \left(1-\mu(r)^2 (h'(r))^2\right),\,
    r^2,\, r^2\sin^2\theta
  \right);
\end{align*}
$$

and:

$$
\begin{align*}
  \beta{}^j = \gamma{}^{ij} \beta{}_i = \frac{\mu(r)^2 h'(r)}{1-\mu(r)^2 (h'(r)^2)};
\end{align*}
$$

with:

$$
\begin{align*}
  \alpha{}^2 = \frac{\mu(r)}{1-\mu(r)^2 (h'(r))^2}.
\end{align*}
$$

We may immediately relate the mean extrinsic curvature through the divergence relation:

$$
\begin{align*}
  -K =& \nabla{}_{a}[n{}^{a}] = \frac{1}{\sqrt{|g|}}
  \partial{}_{a}\left[\sqrt{|g|}n{}^a\right]=0,\\
  \Longrightarrow 0 =& \partial{}_{a}\left[\alpha\gamma{}^{1/2}n{}^a\right],
\end{align*}
$$

where the determinant relation $|g|^{1/2}=\alpha\gamma^{1/2}=r^2\sin\theta$ has been used. Expanding, we find:

$$
\begin{align*}
  &\frac{\mathrm{d}}{\mathrm{d}r}
  \left[r^2
    \left(
      \frac{\mu(r)}{1-\mu(r)^2 (h'(r)^2)}
    \right)^{1/2} \mu(r) h'(r)
  \right] = 0,\\
  \Longrightarrow&
  r^2\left(
  \frac{\mu(r)}{1-\mu(r)^2 (h'(r)^2)}
  \right)^{1/2} \mu(r)h'(r) = C,
\end{align*}
$$

for some constant of integration $C$. It is useful to rearrange this into:

$$
\begin{equation}
  \mu(r)^2 (h'(r)^2) = \frac{C^2}{\mu(r) r^4 + C^2},
\end{equation}
$$

as we may then write (plugging back into previous expressions):

$$
\begin{equation*}
  \gamma{}_{ij}
  = \frac{1}{\mu(r;\,C)} \mathrm{d}r^2 + r^2\mathrm{d}\Omega^2,
\end{equation*}
$$

together with:

$$
\begin{align*}
  \alpha =& \mu(r;\,C),&
  \beta{}^a =& (0, C\mu(r;\,C)^{1/2} / r^2,\,0,\,0);
\end{align*}
$$

where:

$$
\begin{equation*}
  \mu(r;\,C)=1-\frac{2m}{r} + \frac{C^2}{r^4}.
\end{equation*}
$$

Clearly $C$ parametrizes the family of solutions with $C\rightarrow0$ resulting in recovery of $t=\mathrm{const}$ slices of Schwarzschild space-time.

__Recall__: An alternate description of the Schwarzschild solution is provided in so-called "isotropic" coordinates. Here the isotropy is made manifest by transforming to a form where:

$$
\begin{equation}\tag{eq:isomapSS}
  \mathrm{d}s^2 = A(\rho)\mathrm{d}t^2-B(\rho)\mathrm{d}\Sigma^2,
\end{equation}
$$

and $\mathrm{d}\Sigma^2$ represents flat $3$-space:

$$
\begin{equation*}
  \mathrm{d}\Sigma^2 = \mathrm{d}\rho^2
  +\rho^2\mathrm{d}\theta^2
  +\rho^2\sin^2\theta\,\mathrm{d}\phi^2.
\end{equation*}
$$

Comparing Eq.(eq:solnStdSS) and Eq.(eq:isomapSS) we can immediately write:

$$
\begin{align*}
  \mathrm{d}s^2 = -\mu(r)\mathrm{d}t^2+f(\rho)^2\left[
  \mathrm{d}\rho^2
  +\rho^2\mathrm{d}\theta^2
  +\rho^2\sin^2\theta\,\mathrm{d}\phi^2\right],
\end{align*}
$$

and it follows that $r^2=f^2\rho^2$. Furthermore, we impose:

$$
\begin{equation*}
  \frac{1}{\mu(r)}\mathrm{d}r^2 = f(\rho)^2\mathrm{d}\rho^2,
\end{equation*}
$$

and demand that $\rho\rightarrow \infty$ when $r\rightarrow\infty$ which yields:

$$
\begin{equation*}
  \frac{\mathrm{d}r}{\sqrt{r^2-2mr}} = \frac{\mathrm{d}\rho}{\rho};
\end{equation*}
$$

Integrating and rearranging yields the transformation from areal $r$ to isotropic $\rho$ coordinates:

$$
\begin{equation}
  r = \rho (1 + m / (2\rho))^2.
\end{equation}
$$

This leads to the isotropic form of Schwarzschild as:

$$
\begin{equation}\tag{eq:solnIsoSS}
  \mathrm{d}s^2 = -\left(\frac{1-m/(2\rho)}{1+m/(2\rho)}\right)^2\mathrm{d}t^2
  +\left(1+\frac{m}{2\rho} \right)^4
  \left[
    \mathrm{d}\rho^2
    +\rho^2\mathrm{d}\theta^2
    +\rho^2\sin^2\theta\,\mathrm{d}\phi^2
  \right].
\end{equation}
$$

The form of Eq.(eq:solnIsoSS) describes only the region of Schwarzschild geometry with $r\geq 2m$. The horizon is located at $\rho=m/2$ in these coordinates. 

Following this sort of idea, we may consider mapping Eq.(eq:solnStdSSRepar) such that the spatial part takes an isotropic form in some new coordinates:

$$
\begin{equation}
  \left(\frac{1}{\mu(r)} - \mu(r) (h'(r))^2 \right) \mathrm{d}r^2
  +r^2 \mathrm{d}\Omega^2 = \psi^4(\rho)
  \left[\mathrm{d}\rho^2 + \rho^2 \mathrm{d}\Omega^2\right],
\end{equation}
$$

and we regard $\rho=\rho(r)$, say. We omit further details of this calculation but remark that this leads to so-called "trumpet" geometries; (see Class. Quantum Grav. 31 (2014) 117001).

For construction of __Kruskal-Szekeres (KS)__ diagrams and properties see e.g. Wald. KS diagrams displaying properties of different kinds of maximal-slicings for Schwarzschild is provided in Alcubierre Fig. $4.2$ together with a very nice discussion. Gourgoulhon's book ($\S10.2.2$) is also a good place to look.

We give a brief description of __embedding__:

Consider equatorial "plane" at a fixed moment in time $t=\mathrm{const}$, $\theta=\pi/2$:

$$
\begin{equation}
{}^{[2]}\mathrm{d}s^2 = \frac{1}{\mu(r)} \mathrm{d}r^2 + r^2\mathrm{d}\phi^2.
\end{equation}
$$

We aim to embed in three dimensional Euclidean space a two dimensional surface describing the two dimensional geometry. Introduce cylindrical coordinates $(r,\,z,\,\phi)$:

$$
\begin{equation}
{}^{[3]}\mathrm{d}s^2=\mathrm{d}r^2 + \mathrm{d}z^2 + r^2 \mathrm{d}\phi^2.
\end{equation}
$$

The surface to embed is cylindrically symmetric so should only need to regard as function of radius, i.e., $z=z(r)$.

Plugging this in we have:

$$
\begin{equation}
{}^{[3]}\mathrm{d}s^2\rightarrow {}^{[2]}\mathrm{d}s^2=\mathrm{d}r^2+\left(\frac{\mathrm{d}z}{\mathrm{d}r}\right)^2\mathrm{d}r^2+r^2\mathrm{d}\phi^2.
\end{equation}
$$

Comparing with earlier ${}^{[2]}\mathrm{d}s^2$:

$$
\begin{equation}
  \left(1+\left(\frac{\mathrm{d}z}{\mathrm{d}r}\right)^2 \right)=\frac{1}{\mu(r)} \Longrightarrow \frac{\mathrm{d}z}{\mathrm{d}r} = \sqrt{\frac{1}{\mu(r)}-1}.
\end{equation}
$$

We may instead compare with the maximal slicing form which leads to $\mu(r)\rightarrow \mu(r;\,C)$ in the above.

__Embedding diagram__ (both branches of the solution are included corresponding to extended Schwarzschild):

![[_img/2020_06_18_tutorial/20200618-101059.png|600]]

__Maximal (standard Schwarzschild) slice__:

From Alcubierre:
![[_img/2021_05_20_tutorial/Pasted image 20210520124858.png|446]]

- Remark: It is also possible to construct other (maximal) slicings - see the previously mentioned references.

## exercise 1.2
In the lecture notes it was demonstrated (see $\S6.6$) that imposing the maximal slicing condition of Eq.(eq:maxslicecond) extremises volume. 
Argue that in the case of a Lorentzian manifold the extremum constitutes a 
maximum.

## (soln) exercise 1.2
Consider second variation while working in vacuum; use results from 3+1 decomposition and recall that we are working at an extremum.

Some related details: "Isolated Maximal Surfaces in Spacetime, Brill & Flaherty".


# approximations
## exercise 1.1: Newtonian limit
Recall that if the gravitational field is weak and static then it is always possible to find a coordinate system $(x{}^\alpha)=(x{}^0=t,\,x{}^i)$ such that the metric components take the form:

$$
\begin{equation}\tag{eq:metricWeakField}
  g{}_{\mu\nu} \mathrm{d}x{}^\mu{}\mathrm{d}x{}^\nu
  = -(1+2\Phi) \mathrm{d}t{}^2 + (1-2\Phi) f{}_{ij}
  \mathrm{d}x{}^i \mathrm{d}x{}^j,
\end{equation}
$$

where $\Phi$ is the gravitational potential and $|\Phi|\ll1$.

In performing $3+1$ and conformal decompositions, we have found that the mean curvature evolves according to:

$$
\begin{equation}\tag{eq:KtrEvo}
  \mathcal{L}_m[K] = -D_i D^i[\alpha] + \alpha(4\pi(E+S)+K{}_{ij}K{}^{ij}),
\end{equation}
$$

Working within the regime of validity for Eq.(eq:metricWeakField) show that Eq.(eq:KtrEvo) reduces to the Poisson equation:

$$
\begin{equation}
  \mathcal{D}{}_i\mathcal{D}{}^i[\Phi] = 4\pi\rho,
\end{equation}
$$

where $\mathcal{D}$ is the derivative operator associated with the flat metric $f{}_{ij}$.

## (soln) exercise 1.1
We adopt spherical coordinates. As a preliminary note that approximate staticity entails $\Phi=\Phi(r,\,\theta,\,\phi)$. Furthermore, from Eq.(eq:metricWeakField) we may immediately write:

$$
\begin{align*}
  \alpha^2=&(1+2\Phi) \Longrightarrow \alpha = 1+\Phi + \mathcal{O}(\Phi^2),\\
  \beta{}^a=&0,\\
  \gamma{}_{ij}=& (1-2\Phi)\mathrm{diag}\left(1,\,r^2,\,r^2\sin^2\theta \right).
\end{align*}
$$

Considering $\Phi$ as $|\Phi|\ll 1$ we find:

$$
\begin{equation*}
  \partial{}^i[1+f] = \gamma{}^{ij}\partial{}_j[f]
  =\left(
    (1+2\Phi) \partial_r[f],\,
    \frac{(1+2\Phi)}{r^2}\partial_\theta[f],\,
    \frac{(1+2\Phi)}{r^2}\csc^2\theta\,\partial_\phi[f]
  \right)+ \mathcal{O}(\Phi^2);
\end{equation*}
$$

where $f=f(r,\,\theta,\,\phi)\in\mathcal{F}(\Sigma)$ and thus replacement with $\partial\rightarrow\mathcal{D}$ on the LHS of this expression is permitted.

Recall that for $V{}^i\in\mathcal{T}(\Sigma)$:

$$
\begin{equation}
  D{}_i[V{}^i]=\frac{1}{\sqrt{\gamma}}\partial{}_i
  \left[
    \sqrt{\gamma} V{}^i
  \right] = \partial{}_i[V{}^i] + \frac{1}{\sqrt{\gamma}} \partial{}_i[\sqrt{\gamma}]V{}^i,
\end{equation}
$$

where in the present case:

$$
\begin{equation}
  \sqrt{\gamma} = (1-3\Phi)r^2\sin\theta + \mathcal{O}(\Phi^2).
\end{equation}
$$

If we set $V{}^i:=\partial{}^i[1+f]$ and replace $f\rightarrow\Phi$ then we find:

$$
\begin{equation}
  D{}_i[D{}^i[\alpha]]/\alpha = \mathcal{D}{}_i[\mathcal{D}{}^i[\Phi]] + \mathcal{O}(\Phi^2),
\end{equation}
$$

where $\mathcal{D}{}_i[\cdot]$ is the covariant derivative operator associated with the flat $3$-metric in spherical coordinates.

One can also verify directly from definition that $K{}_{ij}=0+\mathcal{O}(\Phi^2)\Longrightarrow K=0+\mathcal{O}(\Phi^2)$. Thus, with $\rho=E+S$ we find that Eq.(eq:KtrEvo) becomes:

$$
\begin{equation*}
  \mathcal{D}{}_i[\mathcal{D}{}^i[\Phi]] = 4\pi\rho,
\end{equation*}
$$

exactly as was required.
