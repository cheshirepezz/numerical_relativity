## question on intrinsic and extrinsic geometry

Consider hypersurfaces embedded in the Euclidean $\mathbb{R}^3$ manifold.

Compute the intrinsic and extrinsic curvature of:
  (**i**) an embedded $2^\d$ plane
  (**ii**) an (infinite) cylinder

## solution

We recall some definitions and make a comment:

A **hypersurface** of $(\mathcal{M},\,n+1)$ is the image $\Sigma$ of an $n$-dimensional manifold $\hat{\Sigma}$ by an embedding $\Phi:\hat{\Sigma}\rightarrow\mathcal{M}$: $\Sigma=\Phi(\hat{\Sigma})$.

An **embedding** means that the map $\Phi:\hat{\Sigma}\rightarrow\Sigma$ is a homeomorphism. Geometrically this avoids self-intersection.

A hypersurface can be defined **locally** as the set of points for which a scalar field on $\mathcal{M}$ is constant. Denote this field by $\sigma$ and set the constant to zero, we get:
$$
\begin{align*}
  \forall &p\in\mathcal{M}, & p\in\Sigma \Longleftrightarrow \sigma(p)=0
\end{align*}
$$
If $\Phi:\hat{\Sigma}\rightarrow\mathcal{M}$ is the embedding which induces the submanifold structure of $\mathcal{M}$, the pullback map $\Phi^*$ **induces** the natural metric $\gamma=\Phi^* g$ on $\Sigma$.
In components we have:
$$
\begin{align}\tag{eq:pullbackmetric}
  \gamma_{\mathrm{IJ}}(x) = g_{kl}(\Phi(x)) \frac{\partial \Phi^k}{\partial x^\mathrm{I}} \frac{\partial \Phi^l}{\partial x^\mathrm{J}},
\end{align}
$$
where $(\Phi^k)$ denote the coordinates of $\Phi(x)$.

Given a Manifold, metric and associated Levi-Civita connection $(\mathcal{M},\,g,\,\nabla)$, the intrinsic curvature is usually introduced as the anti-commutator: $[\nabla_a,\,\nabla_b]\omega_c=\mathrm{Riem}_{abc}{}^d\omega_d$. We may expand the definition of the covariant derivative to provide a method for computation:

$$
\begin{align}\tag{eq:Riem}
  \mathrm{Riem}{}_{abc}{}^d[g] = -2 \partial{}_{[a} \Gamma{}^d{}_{b]}{}_c + 2 \Gamma{}^e{}_{c[a}\Gamma{}^d{}_{b]e};
\end{align}
$$

with Christoffel symbols given by:

$$
\begin{align}\tag{eq:Christoffel}
  \Gamma{}^c{}_{ab}[g]= \frac{1}{2} g{}^{cd} \left(\partial_a[g_{bd}] + \partial_b[g_{ad}] - \partial_d[g_{ab}]\right).
\end{align}
$$

The extrinsic curvature of $\Sigma$ may be computed with the projector and unit normal $n^a$ to $\Sigma$:

$$
\begin{align}\tag{eq:Extrinsic}
  K_{ab}:=-\gamma{}^c_a\gamma{}^d_b \nabla{}_{(c}[n{}_{d)}]=-\gamma{}^c_a\gamma{}^d_b \nabla{}_{c}[n{}_{d}],
\end{align}
$$

this may also be written via direct evaluation over appropriate basis vectors:

$$
\begin{align}\tag{eq:Extrinsic2}
  K_{\mathrm{IJ}} = \mathbf{K}(\boldsymbol{\partial}_{\mathrm{I}},\,\boldsymbol{\partial}_{\mathrm{J}}) = -\nabla_i[n_j](\partial_\mathrm{I})^i(\partial_\mathrm{J})^j.
\end{align}
$$

**We need to construct**: Embedding map, induced metric, unit normal, intrinsic curvature $\mathrm{Riem}$ (Wald convention), extrinsic curvature $K$ (negative convention).

**(i)**

Let $\hat{\Pi}$ be a connected submanifold of $\mathcal{M}:=\mathbb{R}^3$ with topology $\mathbb{R}^2$, i.e., the $2$-d plane. Introduce locally (In this case they also hold globally) a set of coordinates for $\mathcal{M}$, $(x^i)=(x,y,z)$, such that $\sigma$ spans $\mathbb{R}$ and $(x,y)$ are Cartesian coordinates spanning $\mathbb{R}^2$. The hypersurface $\Pi$ is then defined by the coordinate condition $\sigma=0$. An explicit form of the mapping $\Phi$ can be obtained by considering $(x^\mathrm{I})=(x,y)$ as coordinates on $\hat{\Pi}$:

$$
\begin{align*}
  \Phi:=&\hat{\Pi}\rightarrow\mathcal{M},\\
  (x,y)\mapsto&(x,y,0).
\end{align*}
$$

In short, we view the hypersurface $\Pi$ as the $z=0$ plane. The scalar function $\sigma$ defining $\Pi$ is thus $\sigma=z$.

In order to find the induced metric we make use of Eq.(eq:pullbackmetric) and note that the Euclidean metric on $\mathcal{M}$ is simply $\delta_{ij}$. Clearly we must have $\gamma_{\mathrm{IJ}}=\mathrm{diag}(1,\,1)$.

Furthermore, it follows trivially from Eq.(eq:Riem) and Eq.(eq:Christoffel) that $\mathrm{Riem}$ vanishes (note $\Gamma[\delta]=0$).

In order to compute the extrinsic curvature we select a (global) unit normal to $\Pi$, namely, $n^i=(0,\,0,\,1)$. For the present case we have $n_i \delta{}^{ij} = n^j$. Due to this and $\Gamma[\delta]=0$ we have $\nabla_a[n_b]=\partial_a[n_b]=(0,\,0,\,0)$. Based on Eq.(eq:Extrinsic) we immediately conclude that the extrinsic curvature vanishes as well.

**Geometric intuition**: The unit vector stays constant when translated along $\Pi$ and hence the extrinsic curvature (measuring how the hypersurface bends in the ambient space) is zero. Furthermore, on a plane, the internal angles of a triangle must sum to $\pi$ - the intrinsic curvature vanishes verifies this fact.

**(ii)**

For the hypersurface describing our (infinite) cylinder $\mathcal{C}$ we take the local definition $\sigma:=\rho-a=0$, where $\rho:=\sqrt{x^2+y^2}$ and $a\in\mathbb{R}^{>0}$ is the radius of the cylinder. We introduce the cylindrical coordinates $(x^i)=(\rho,\,\varphi,\,z)$, such that $\varphi\in[0,\,2\pi)$, $x=\rho\cos\varphi$ and $y=\rho\sin\varphi$. On $\mathcal{C}$, $(x^\mathrm{I})=(\varphi,\,z)$ constitute a coordinate system.

Thus, we take:
$$
\begin{align*}
  \Phi:(\varphi,\,z)\mapsto(\rho\cos\varphi,\,\rho\sin\varphi,\,z).
\end{align*}
$$

From Eq.(eq:pullbackmetric) we can compute the induced metric:
$$
\begin{align*}
  \boldsymbol{\gamma}=\gamma_{\mathrm{IJ}} \d{x^\mathrm{I}}\otimes\d{x^\mathrm{J}} =& \delta_{ij} \frac{\partial \Phi^i}{\partial x^\mathrm{I}} \frac{\partial \Phi^j}{\partial x^\mathrm{J}} \d{x^\mathrm{I}}\otimes\d{x^\mathrm{J}}\\
  =& a^2\d{\varphi}\otimes\d{\varphi} + \d{z}\otimes \d{z}; 
\end{align*}
$$
Thus $\gamma_{\mathrm{IJ}}=\mathrm{diag}(a^2,\,1)$.

Notice that $a$ is constant. We may therefore introduce another coordinate $\eta:=a\varphi$ and further map the induced metric via coordinate transformation to:

$$
\begin{align*}
  \boldsymbol{\gamma}=\d{\eta}\otimes\d{\eta} + \d{z}\otimes\d{z}.
\end{align*}
$$

This is in the form of the Euclidean metric and therefore we once again conclude that the intrinsic curvature $\mathrm{Riem}$ is zero.

In order to compute extrinsic curvature we need a unit normal. Notice that on $\mathcal{C}$ for fixed $\varphi$, translation along the $z$-direction should leave the unit normal unaffected. We make the out-ward pointing choice:

$$
\begin{align*}
  n^i=&\left(\frac{x}{a},\,\frac{y}{a},\,0 \right)\Longrightarrow n_i=\delta_{ij}n^j=\left(\frac{x}{a},\,\frac{y}{a},\,0 \right),
\end{align*}
$$

with $a$ constant. It follows then that:

$$
\begin{align*}
  \nabla_i[n_j] = \partial_i[n_j]=\mathrm{diag}(1/a,\,1/a,\,0);
\end{align*}
$$

as $\Gamma[\gamma]=0$.

Consider Eq.(eq:Extrinsic2). We have the natural basis $(\boldsymbol{\partial}_\mathrm{I})=(\boldsymbol{\partial}_\varphi,\,\boldsymbol{\partial}_z)$ associated with the coordinates $(\varphi,\,z)$. The components $(\partial_\mathrm{I})^i$ are of the vector $\boldsymbol{\partial}_\mathrm{I}$ we take with respect to the natural basis $(\boldsymbol{\partial})_i=(\boldsymbol{\partial}_x,\,\boldsymbol{\partial}_y,\,\boldsymbol{\partial}_z)$ in Cartesian coordinates. As $\boldsymbol{\partial}_\varphi=-y\boldsymbol{\partial}_x + x \boldsymbol{\partial}_y$, one has $(\partial_\varphi)^i=(-y,\,x,\,0)$ and $(\partial_z)^i=(0,\,0,\,1)$.

We find:
$$
\begin{align*}
  \mathbf{K}(\boldsymbol{\partial}_\mathrm{I},\,\boldsymbol{\partial}_\mathrm{J})\d{x}^\mathrm{I}\otimes \d{x}^\mathrm{J}=&
  -\left(\frac{1}{a}(\boldsymbol{\partial}_I)^1 (\boldsymbol{\partial}_J)^1
+\frac{1}{a}(\boldsymbol{\partial}_I)^2 (\boldsymbol{\partial}_J)^2\right)\d{x}^\mathrm{I}\otimes \d{x}^\mathrm{J},\\
  =&-\frac{1}{a}\left[(-y)(-y) + x^2\right] \partial_\varphi\otimes \partial_\varphi,\\
  =&-a\partial_\varphi\otimes \partial_\varphi.
\end{align*}
$$
The trace of the extrinsic curvature can be found using the relation $\gamma^{\mathrm{IJ}}=\mathrm{diag}(a^{-2},1)$ which results in $K=-a^{-1}$.

## other things to try:
  - Intrinsic / extrinsic quantities associated with sphere embedded in $\mathbb{R}^3$.
  - Given Schwarzschild in isotropic coordinates compute (spatial) $3$-metric, extrinsic curvature and its trace. (see Eq.6.11 of lecture notes)