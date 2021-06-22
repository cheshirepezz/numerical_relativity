## Extrinsic curvature

### Exercise 1.1: 

Consider a sphere of radius $a$ under the embedding in $\mathbb{R}^3$ specified through $t:=r-a=0$ with $r=\sqrt{x^2+y^2+z^2}$. Compute the intrinsic and extrinsic curvature.

### (Soln) 1.1
_For the general idea_: see example from last tutorial.

We can introduce spherical coordinates $x{}^\alpha\dot{=}(r,\,\vartheta,\,\varphi)$ where:

$$
\begin{align}
  x(r,\,\vartheta,\,\varphi) &=
  r \sin(\vartheta) \cos(\varphi),\\
  y(r,\,\vartheta,\,\varphi) &=
  r\sin(\vartheta) \sin(\varphi),\\
  z(r,\,\vartheta,\,\varphi) &=
  r \cos(\vartheta).
\end{align}
$$

This provides us (components of) the embedding map $\Phi:\hat{\mathbb{S}}{}^2_a\rightarrow \mathbb{R}^3$. In particular we think of $\Phi^k\dot{=}(x(a,\,\vartheta,\,\varphi),\,y(a,\,\vartheta,\,\varphi),\,z(a,\,\vartheta,\,\varphi))$. Consequently via pullback we have the induced metric:

$$
\begin{align*}
  \gamma{}_{IJ}\d{x}{}^I\d{x}{}^J &=
  \underbrace{g_{kl}}_{=\delta{}_{kl}}
  \frac{\partial \Phi^k}{\partial x^\mathrm{I}}
  \frac{\partial \Phi^l}{\partial x^\mathrm{J}}
  \d{x}{}^I\d{x}{}^J,\\
  &=
  \underbrace{\left[a^2\cos^2(\varphi)\cos^2(\vartheta)
  + a^2 \cos^2(\vartheta)\sin^2(\varphi)
  + a^2 \sin^2(\vartheta) \right]}_{a^2}
  \d{\vartheta}{}^2\\
  &\quad+\underbrace{\left[
  -a^2\cos(\varphi)\cos(\vartheta)\sin(\varphi)\sin(\vartheta)
  +a^2\cos(\varphi)\cos(\vartheta)\sin(\varphi)\sin(\vartheta)
  +0\right]}_{=0} \d{\vartheta} \d{\varphi}\\
    &\quad+\underbrace{\left[
  -a^2\cos(\varphi)\cos(\vartheta)\sin(\varphi)\sin(\vartheta)
  +a^2\cos(\varphi)\cos(\vartheta)\sin(\varphi)\sin(\vartheta)
  +0\right]}_{=0} \d{\varphi} \d{\vartheta}\\
  &\quad+\underbrace{\left[
  a^2\sin^2(\varphi)\sin^2(\vartheta)
  +a^2\cos^2(\varphi)\sin^2(\vartheta)
  + 0
  \right]}_{a^2\sin^2(\vartheta)} \d{\varphi}{}^2\\
  &=
  a^2\Big(
  \underbrace{
  \d \vartheta^2 + \sin^2(\vartheta)\,\d \varphi^2}_{=:\d\Omega^2}
  \Big),
\end{align*}
$$

where we think of $x^I\dot{=}(\vartheta,\,\varphi)$.

So we have the _induced metric_ - what about Riemann, Ricci and scalar curvature?

First recall that these are related by (Wald convention) $\mathrm{Riem}{}_{ikjl} g^{kl}=\mathrm{Ric}{}_{ij}$ and $g{}^{ij}\mathrm{Ric}{}_{ij}=\mathcal{R}$.

**Dimensionality**:

In general for $(\mathcal{M},\,g)$ with $\dim(\mathcal{M})=n$ one has that the number of independent components of $\mathrm{Riem}[g]{}_{abcd}$ goes as $\frac{1}{12}n^2(n^2-1)$ (try to justify this). 

For $\dim(\Sigma)=2$ the tensor $\mathrm{Riem}$ should therefore only have one independent component.

Working the relations between geometric objects:

$$
\begin{equation}
  \mathrm{Ric}{}_{IJ} = \mathrm{Riem}{}_{IKJ}{}^K
  =\mathrm{Riem}{}_{I1J}{}^1 + \mathrm{Riem}{}_{I2J}{}^2,
\end{equation}
$$

Therefore (using antisymmetry of $\mathrm{Riem}$):

$$
\begin{align}
  \mathrm{Ric}{}_{11} &= \mathrm{Riem}{}_{121}{}^2,&
  \mathrm{Ric}{}_{12} &= \mathrm{Riem}{}_{122}{}^2,&
  \mathrm{Ric}{}_{21} &= \mathrm{Riem}{}_{211}{}^1,&
  \mathrm{Ric}{}_{22} &= \mathrm{Riem}{}_{212}{}^1;
\end{align}
$$

which permits us to write:

$$
\begin{equation}
  \mathcal{R} = \gamma{}^{IJ} \mathrm{Ric}{}_{IJ}
  = \gamma{}^{11}\mathrm{Riem}{}_{121}{}^2
  + \gamma{}^{12}\mathrm{Riem}{}_{122}{}^2
  + \gamma{}^{21}\mathrm{Riem}{}_{211}{}^1
  + \gamma{}^{22}\mathrm{Riem}{}_{212}{}^1.
\end{equation}
$$

Using:

$$
\begin{equation}
  \gamma{}^{IJ}\dot{=}\frac{1}{\gamma{}_{11}\gamma{}_{22}-\gamma{}_{12}\gamma{}_{21}}
  \begin{bmatrix}
    \gamma{}_{22} & -\gamma{}_{12}\\
    -\gamma{}_{21} & \gamma{}_{11}
  \end{bmatrix},
\end{equation}
$$

leads to:
$$
\begin{align}
  \mathcal{R} &=
  \frac{1}{\gamma{}_{11}\gamma{}_{22}-\gamma{}_{12}\gamma{}_{21}}
  \Big[
  \gamma{}_{22}\mathrm{Riem}{}_{121}{}^2
  + -\gamma{}_{12}\mathrm{Riem}{}_{122}{}^2
  + -\gamma{}_{21}\mathrm{Riem}{}_{211}{}^1
  + \gamma{}_{11}\mathrm{Riem}{}_{212}{}^1
  \Big],\\
  &=
  \frac{2}{\gamma{}_{11}\gamma{}_{22}-\gamma{}_{12}\gamma{}_{21}}
  \mathrm{Riem}{}_{1212};
\end{align}
$$

where we also used:

$$
\begin{align}
  \gamma{}_{22} \mathrm{Riem}{}_{121}{}^2
  -\gamma{}_{21}\mathrm{Riem}{}_{211}{}^1
  &=
  \gamma{}_{22}\mathrm{Riem}{}_{121}{}^2
  + \gamma{}_{21}\mathrm{Riem}{}_{121}{}^1
  = \gamma{}_{2I} \mathrm{Riem}{}_{121}{}^I
  = \mathrm{Riem}{}_{1212},\\
  -\gamma{}_{12}\mathrm{Riem}{}_{122}{}^2
  +\gamma{}_{11}\mathrm{Riem}{}_{212}{}^1
  &=
  \gamma{}_{12}\mathrm{Riem}{}_{212}{}^2
  +\gamma{}_{11}\mathrm{Riem}{}_{212}{}^1
  =\mathrm{Riem}{}_{2121}.
\end{align}
$$

In principle, we therefore only need to compute  $\mathrm{Riem}{}_{1212}$. Non-trivial Christoffel symbols are:

$$
\begin{align}
  \Gamma[\gamma]{}^2{}_{12} &= \Gamma[\gamma]{}^2{}_{21}
  =\cot(\vartheta), &
  \Gamma[\gamma]{}^1{}_{22} &= -\cos(\vartheta)\sin(\vartheta);
\end{align}
$$

which leads to $\mathrm{Riem}{}_{1212}=a^2\sin^2(\vartheta)$. When combined with the expression above for $\mathcal{R}$ we find:

$$
\begin{equation}
  \mathcal{R}[\gamma] = \frac{2}{a^2}.
\end{equation}
$$


** Extrinsic quantities **:

For this we identify an outward pointing normal to $\mathbb{S}{}^2_a$ in Cartesian coordinates as:

$$
\begin{equation}
  n{}^\alpha=\frac{1}{a}\left(x,\,y,\,z \right),
\end{equation}
$$

thus, working in these coordinates we immediately notice $\nabla{}_\beta[n{}^\alpha]=\partial{}_\beta[n{}^\alpha]=a^{-1}\delta{}^\alpha_\beta$ and therefore:

$$
\begin{equation}
  \nabla{}_\beta[n{}_\alpha] = a^{-1} g{}_{\alpha\beta}.
\end{equation}
$$

Recall that for the extrinsic curvature we have $K{}_{IJ}=\mathbf{K}(\boldsymbol{\partial}{}_I,\,\boldsymbol{\partial}{}_J)=-\nabla{}_\beta[n{}_\alpha](\partial{}_I){}^\alpha (\partial{}_J){}^\beta$, thus if we take the basis vectors $\boldsymbol{\partial}{}_I\dot{=}(\boldsymbol{\partial}_\vartheta,\,\boldsymbol{\partial}_\varphi)$ we find $\mathbf{K}=-a^{-1}\boldsymbol{\gamma}$. In components:

$$
\begin{equation}
  K{}_{IJ} = \begin{bmatrix}
    K{}_{\vartheta\vartheta} & K{}_{\vartheta\varphi}\\
    K{}_{\varphi\vartheta} & K{}_{\varphi\varphi}
  \end{bmatrix} =
  \begin{bmatrix}
    -a & 0\\
    0 & -a\sin^2(\vartheta)
  \end{bmatrix}.
\end{equation}
$$

Finally taking the trace with $\gamma$:

$$
\begin{equation}
  K = -\frac{2}{a}.
\end{equation}
$$

### Exercise 1.2: 

Consider Schwarzschild in isotropic coordinates:
$$
\begin{equation}
\d{} s^2 = - \alpha^2 \d{} t^2+ \psi^4(\d{} r^2 + r^2 \d{}\Omega^2),
\end{equation}
$$
where $\psi:=(1+M/2r)$, $\alpha:=(1-M/2r)/\psi$ and $\d{}\Omega^2$ is the standard $2$-sphere metric. Identify spatial slices $\Sigma$ with hypersurfaces of constant coordinate time $t$.

  * What is the $3$-metric?
  * Compute the intrinsic and extrinsic curvature.

### (Soln) 1.2

As a preliminary note that in $3+1$ decomposition the ambient metric can be written in the form:

$$
\begin{align}\tag{eq:metrDec}
  \d{s}^2 = -\alpha^2\d{t}^2 + \gamma_{ij}(\d{x}^i + \beta^i \d{t})(\d{x}^j + \beta^j \d{t});
\end{align}
$$

Furthermore:

$$
\begin{align*}
  n^a=&(\alpha^{-1},\,-\alpha^{-1}\beta^i), &
  n_a=&(-\alpha,\,0,\,0,\,0).
\end{align*}
$$

It will also be useful for us to recall the evolution equation for the spatial metric:

$$
\begin{align}\tag{eq:evogam}
  \partial_t[\gamma_{ij}] = -2\alpha K_{ij} + D_i[\beta_j] + D_i[\beta_j],
\end{align}
$$

where $D_i$ is the Levi-Civita connection associated with the induced metric $\gamma$.

Clearly it is the case that $\boldsymbol{\beta}=0$ and that the $3$-metric is given by:

$$
\begin{align*}
  \gamma_{ij} = \psi^4 \mathrm{diag}\left(1,\,r^2,\,r^2\sin^2\vartheta\right).
\end{align*}
$$

As $\gamma_{ij}$ is time-independent and $\boldsymbol{\beta}=0$ we immediately see that due to Eq.(eq:evogam) the extrinsic curvature and its trace are zero.

Notice that $\gamma_{ij}$ is diagonal. In this case Christoffel symbols may be computed with the assistance of:

$$
\begin{align*}
 \Gamma{}^a{}_{bc}[\gamma]=&0, & 
 \Gamma{}^a{}_{bb}[\gamma]=& -\frac{1}{2\gamma_{aa}} \partial_a[\gamma_{bb}],\\
 \Gamma{}^a{}_{ab}[\gamma]=& \partial_b\left[\log(\gamma_{aa})^{1/2} \right], &
 \Gamma{}^a{}_{aa}[\gamma]=& \partial_a\left[\log(\gamma_{aa})^{1/2} \right];
\end{align*}
$$

where $a\neq b\neq c$ and there is no summation over repeated indices.

As a check one should find that the non-zero Ricci $3$-tensor components are:

$$
\begin{align*}
  \mathrm{Ric}_{rr} =& - \frac{8rM}{(2r^2+Mr)^2)},\\
  \mathrm{Ric}_{\vartheta\vartheta} =& \frac{4r^3M}{(2r^2+Mr)^2},\\
  \mathrm{Ric}_{\varphi\varphi} =& \sin^2\vartheta\,\mathrm{Ric}_{\vartheta\vartheta};
\end{align*}
$$

with scalar curvature $\mathcal{R}[\gamma]=0$.

## Gauss-Codazzi-Ricci

The Gauss-Codazzi-Ricci equations are identities relating the $3+1$ projections of the $4^\d$ Riemann and Ricci tensors.

Note that:
$\gamma_b^a = g^{ac}\gamma_{cb}=\delta^a_b+n^an_b$ is the $3+1$ spatial projection operator and $n^a$ the unit normal vector to hypersurfaces $\Sigma_t$

### exercise 2.1: derivation of Gauss equations
The Gauss equation is the spatial projection of the $4^\d$ Riemann tensor ${}^4R_{abcd}$ that can be expressed in terms of the spatial ($3^\d$) Riemann tensor $R_{abcd}$ and extrinsic curvature $K_{ab}$ as 

$$
\begin{equation}
  \gamma_a^p\gamma_b^q\gamma_c^r\gamma_d^s {}^4R_{pqrs} 
  = R_{abcd} + K_{ac}K_{bd} - K_{ad}K_{bc}.
\end{equation}
$$

Compute the above relation and the contractions

$$
\begin{align}
  \gamma_a^p\gamma_b^q {}^4R_{pq} + \gamma_{ap}n^q\gamma^r_bn^s {}^4R^p_{qrs} 
  &= R_{ab} + K K_{ab} - K_{ap}K^p_{b},\\
  {}^4R + 2 n^an^b {}^4R_{ab} 
  &= R + K^2 - K_{ab}K^{ab}. 
\end{align}
$$

### (Soln) 2.1

We show:

$$
\begin{equation}
  \gamma{}^p_a\gamma{}^q_b\gamma{}^r_c\gamma{}^s_d
  {}^{[4]}\mathrm{Riem}{}_{pqrs}
  =
  {}^{[3]}\mathrm{Riem}{}_{abcd} + K{}_{ac}K{}_{bd}
  -K{}_{ad} K{}_{bc}.
\end{equation}
$$

As a preliminary recall the projector convention $\gamma{}^p_a=\delta{}^p_a+n{}^p n{}_a$.

**Idea**: we relate ${}^{[d]}\mathrm{Riem}$ and ${}^{[d-1]}\mathrm{Riem}$ definitions directly. To fix conventions suppose we have the ambient manifold, metric and Levi-Civita connection in the triplet $(\mathcal{M},\,g,\,\nabla)$ together with analogous quantities for the submanifold $(\Sigma,\,\gamma,\,D)$. Our first goal is to relate the two covariant derivatives.

Suppose $V\in\mathcal{T}^1(\Sigma)$. We have:

$$
\begin{align*}
  D{}_a[V{}^b] &=
  \gamma{}^c_a\gamma{}^b_d \nabla{}_c[V{}^d]
  = \gamma{}^c_a\Big(
  \underbrace{\delta{}^b_d}_{=g{}^b_d}+n{}_d n{}^b \Big)
  \nabla{}_c[V{}^d],\\
  &= \gamma{}^c_a\nabla{}_c[V{}^b]
  +\gamma{}^c_a n{}_d n{}^b \nabla{}_c[V{}^d]
  =:(\star).
\end{align*}
$$

Note:
$$
\begin{align*}
  n_d V^d=0 &\Longrightarrow
  0=\nabla{}_c[n{}_d V{}^d]
  = \big(\nabla{}_c[n{}_d]\big)V{}^d+n{}_d \nabla{}_c[V{}^d],\\
  &\Longleftrightarrow
  -\nabla{}_c[n{}_d]V{}^d = n{}_d\nabla{}_c[V{}^d].
\end{align*}
$$

Thus from $(\star)$:
$$
\begin{align*}
  D{}_a[V{}^b] &=
  \gamma{}^c_a \nabla{}_c[V{}^b]
  - \gamma{}^c_a V{}^d n{}^b \nabla{}_c[n{}_d],\\
  &=
  \gamma{}^c_a\nabla{}_c[V{}^b]
  -\gamma{}^c_a V{}^e \gamma{}^d_e n{}^b
  \nabla{}_c[n{}_d],\\
  &=
  \gamma{}^c_a \nabla{}_c[V{}^b] + K{}_{ae}V{}^e n{}^b;
\end{align*}
$$

where we use $K{}_{ab}=-\gamma{}^c_a\gamma{}^d_b\nabla{}_c[n{}_d]$.

We need a second derivative (Riemann requires commutator). Thus:

$$
\begin{align*}
  D{}_a[D{}_b[V{}^c]]
  &=
  D{}_a\Big[
    \gamma{}^p_b \gamma{}^c{}_q \nabla{}_p[V{}^q]
  \Big]
  = \gamma{}^r_a \gamma{}^s_b \gamma{}^c_t
  \nabla{}_r\Big[
    \gamma{}^p_s\gamma{}^t_q\nabla{}_p[V{}^q]
  \Big],\\
  &=
  \gamma{}^r_a\gamma{}^s_b\gamma{}^c_t
  \Big[
    \gamma{}^p_s\gamma{}^t_q
    \nabla{}_r[\nabla{}_p[V{}^q]]
    + \nabla{}_p[V{}^q]\nabla{}_r[\gamma{}^p_s\gamma{}^t_q]
  \Big],\\
  &=
  \gamma{}^r_a\gamma{}^s_b\gamma{}^c_t\gamma{}^p_s
  \gamma{}^t_q\nabla{}_r[\nabla{}_p[V{}^q]]
  + \gamma{}^r_a\gamma{}^s_b\gamma{}^c_t \nabla{}_p[V{}^q]
  \nabla{}_r[\gamma{}^p_s\gamma{}^t_q],\\
  &=
  \gamma{}^r_a\gamma{}^c_q\gamma{}^p_b
  \nabla{}_r[\nabla{}_p[V{}^q]]
  +\underbrace{
    \gamma{}^r_a\gamma{}^s_b\gamma{}^c_t
    \nabla{}_p[V{}^q]
    \Big[
      \gamma{}^p_s\nabla{}_r[\gamma{}^t_q]
      +\gamma{}^t_q\nabla{}_r[\gamma{}^p_s]
    \Big]
  }_{(\star\star)};
\end{align*}
$$

$$
\begin{align*}
  (\star\star) &= \gamma{}^s_a\gamma{}^s_b\gamma{}^c_t
  \nabla{}_p[V{}^q]
  \Big[
    \gamma{}^p_s\nabla{}_r[n{}^tn{}_q]
    +\gamma{}^t_q\nabla{}_r[n{}^pn{}_s]
  \Big],\\
  &= \gamma{}^s_a\gamma{}^s_b\gamma{}^c_t
  \nabla{}_p[V{}^q]
  \Big[
    \gamma{}^p_s
    \big[
      \nabla{}_r[n{}^t]n{}_q + \underbrace{
        \nabla{}_r[n{}_q]n{}^t
      }_{=0}
    \big]
    +
    \gamma{}^t_q
    \big[
      n{}^p\nabla{}_r[n{}_s]
      +\underbrace{n{}_s\nabla{}_r[n{}^p]}_{=0}
    \big]
  \Big],\\
  &=
  \gamma{}^r_a\gamma{}^s_b\gamma{}^c_t
  \nabla{}_p[V{}^q]
  \Big[
    \gamma{}^p_s n{}_q\nabla{}_r[n{}^t]
    +\gamma{}^t_q n{}^p\nabla{}_r[n{}_s]
  \Big],\\
  &=
  -\gamma{}^r_a\gamma{}^s_b\gamma{}^c_t\nabla{}_p[n_q]
  V{}^q\gamma{}^p_s\nabla{}_r[n{}^t]
  +\gamma{}^r_a{}\gamma{}^s_b\gamma{}^c_t
  \nabla{}_p[V{}^q]\gamma{}^t_qn{}^p\nabla{}_r[n{}_s],\\
  &= \gamma{}^r_a\gamma{}^s_b\gamma{}^c_t K{}_{sq} V{}^q
  \nabla{}_r[n{}^t],\\
  &=-K{}_a{}^c K{}_{bq}V{}^q - K{}_{ab}\gamma{}^c_q n{}^p
  \nabla{}_p[V{}^q];
\end{align*}
$$

Thus, we have:

$$
\begin{equation}
  D{}_a[D{}_b[V{}^c]]
  =
  \gamma{}^r_a\gamma{}^c_q\gamma{}^p_b
  \nabla{}_r[\nabla{}_p[V{}^q]]
  -K{}_a{}^c K{}_{bq}V{}^q
  -K{}_{ab}\gamma{}^c_q n{}^p
  \nabla{}_p[V{}^q].
\end{equation}
$$

Recall that for $\omega\in\Omega(\Sigma)$ we have:
$$
\begin{equation}
  {}^{[3]}\mathrm{Riem}{}_{abc}{}^d\omega{}_d=
  [D{}_a,\,D{}_b]\omega{}_c.
\end{equation}
$$

Let $\omega_d=\gamma{}_{ad}V{}^d$ then ${}^{[3]}\mathrm{Riem}{}_{abcd}V{}^d=[D{}_a,\,D{}_b]\omega{}_c$ and ${}^{[3]}\mathrm{Riem}{}_{ab}{}^{cd}\omega{}_d=[D{}_a,\,D{}_b]\omega{}^c$.

We have:

$$
\begin{align*}
  D{}_a[D{}_b[V{}^c]] - D{}_b[D{}_a[V{}^c]]
  &=
  \gamma{}^r_a\gamma{}^c_q \gamma{}^p_b
  \nabla{}_r[\nabla{}_p[V{}^q]]
  -K{}_a{}^c K{}_{bq}V{}^q
  -K{}_{ab}\gamma{}^c_q n{}^p\nabla{}_p[V{}^q]\\
  &\quad
  -\Big[
    \gamma{}^r_b \gamma{}^c_q\gamma{}^p_a
    \nabla{}_r[\nabla{}_p[V{}^q]]
    -K{}_b{}^c K{}_{aq}V{}^q
    -K{}_{ba} \gamma{}^c_q n{}^p
    \nabla{}_p[V{}^q]
  \Big],\\
  &=
  \gamma{}^r_a\gamma{}^c_q\gamma{}^p_b
  [\nabla{}_r,\,\nabla{}_p]V{}^q
  - K{}_a{}^c K{}_{bq}V{}^q
  + K{}_b{}^c K{}_{aq}V{}^q,\\
  &= {}^{[3]}R{}_{ab}{}^c{}_q V{}^q,\\
  &=
  \gamma{}^r_a\gamma{}^c_q\gamma{}^p_b
  {}^{[4]}\mathrm{Riem}{}_{rp}{}^q{}_s V{}^s
  - K{}_a{}^c K{}_{bq} V{}^q
  + K{}_b{}^c K{}_{aq} V{}^q,\\
  &=
  \gamma{}^r_a\gamma{}^c_s\gamma{}^p_b
  {}^{[4]}\mathrm{Riem}{}_{rp}{}^s{}_q V{}^q
  - K{}_a{}^c K{}_{bq}V{}^q
  + K{}_b{}^c K{}_{aq} V{}^q,
\end{align*}
$$
where we relabel dummy indices $s\leftrightarrow q$ on the first term in the last expression - thus:

$$
\begin{align*}
  \Longrightarrow&
  \gamma{}^r_a\gamma{}^s_c\gamma{}^p_b\gamma{}^e_q
  {}^{[4]}\mathrm{Riem}{}_{rpse}
  =
  {}^{[3]}\mathrm{Riem}{}_{abcq}
  + K{}_{ac}K{}_{bq}-K{}_{bc}K{}_{aq}.
\end{align*}
$$

For the contracted result use the metric and argue using ${}^{[3]}\mathrm{Riem}$ intrinsic to $\Sigma$ etc.

### exercise 2.2: derivation of Codazzi equations
The Codazzi equation is the projection of the $4^\d$ Riemann tensor ${}^4R_{abcd}$ 

$$
\begin{equation}
  \gamma_a^p\gamma_b^q\gamma_c^r n^s {}^4R_{pqrs} 
  = D_bK_{ac} - D_aK_{bc},
\end{equation}
$$

expressed in terms of the spatial ($3^\d$) Riemann tensor $R_{abcd}$ and extrinsic curvature $K_{ab}$. Compute the above relation and the contraction

$$
\begin{equation}
  \gamma_a^p n^q {}^4R_{pq} 
  = D_a K - D_s K^s_a.
\end{equation}
$$

### (Soln) 2.2

We show:

$$
\begin{equation}
  \gamma{}^p_a\gamma{}^q_b\gamma{}^r_c
  n{}^s {}^{[4]}\mathrm{Riem}{}_{pqrs}
  = D{}_b[K{}_{ac}] - D{}_a[K{}_{bc}].
\end{equation}
$$

As a preliminary define $\mathcal{T}_1(\Sigma)\ni a{}_b:=n{}^a \nabla{}_a[n{}_b]$ and notice that we can write:

$$
\begin{equation}
  K{}_{ab} = -\gamma{}^p_a
  \gamma{}^q_b \nabla{}_p[n{}_q]
  =-
  \big(
    \delta{}^p_a + n{}^p n{}_a
  \big)
  \big(
    \delta{}^q_b + n{}^q n{}_b
  \big) \nabla{}_p[n{}_q] = -\nabla{}_a[n{}_b]-n{}_a a{}_b.
\end{equation}
$$

Now:

$$
\begin{align}
  D{}_a[K{}_{bc}]
  &=
  \gamma{}^p_a \gamma{}^q_b \gamma{}^r_c
  \nabla{}_p[K{}_{qr}],\\
  &=
  \gamma{}^p_a\gamma{}^q_b\gamma{}^r_c
  \nabla{}_p
  \Big[
    -\gamma{}^s_q \gamma{}^t_r \nabla{}_s[n{}_t]
  \Big],\\
  &=
  \gamma{}^p_a \gamma{}^q_b \gamma{}^r_c \nabla{}_p
  \Big[
    -\nabla{}_q[n{}_r] - n{}_q a{}_r
  \Big],\\
  &=
  -\gamma{}^p_a\gamma{}^q_b\gamma{}^r_c
  \left(
    \nabla{}_p[\nabla{}_q[n{}_r]]
    +\nabla{}_p(n{}_q a{}_r)
  \right),\\
  &=
  -\gamma{}^p_a\gamma{}^q_b\gamma{}^r_c
  \left(
    \nabla{}_p[\nabla{}_q[n{}_r]]
    +a{}_r\nabla{}_p[n{}_q]
  \right) \quad\quad\quad (n\perp\gamma),\\
  &=
  -\gamma{}^p_a\gamma{}^q_b\gamma{}^r_c
  \nabla{}_p[\nabla{}_q[n{}_r]]
  +a{}_c K{}_{ac},
\end{align}
$$

Notice:
$$
\begin{align}
  D{}_a[K{}_{bc}]-D{}_b[K{}_{ac}]&=D{}_{[a}[K{}_{b]c}]
  =-\gamma{}^p_a\gamma{}^q_b\gamma{}^r_c
  \nabla{}_{[p}[\nabla{}_{q]}[n{}_r]],\\
  &=\gamma{}^p_a\gamma{}^q_b\gamma{}^r_c n{}^s
  {}^{[4]}\mathrm{Riem}{}_{pqrs}.
\end{align}
$$

### exercise 2.3: derivation of Ricci equations
The Ricci equation is the spatial projection of the $4^\d$ Riemann tensor ${}^4R_{abcd}$

$$
\begin{equation}
  \gamma_a^p\gamma_b^q n^r n^s {}^4R_{prqs} 
  = \mathcal{L}_m K_{ab} + \alpha^{-1}D_aD_b\alpha + K^d_bK_{ad},
\end{equation}
$$

expressed in terms of the spatial ($3^\d$) Riemann tensor $R_{abcd}$ and extrisinc curvature $K_{ab}$. Above $D_a$ the covariant derivative of $(\Sigma_t,\gamma_{ab})$, and $\mathcal{L}_n$ is the Lie derivative along $n^a$. Derive this equations. The term "$\gamma\gamma n n {}^4R$" appears also in the contracted Ricci equation, 

$$
\begin{equation}
  \gamma_a^p n^q {}^4R_{pq} 
  = D_a K - D_s K^s_a.
\end{equation}
$$

Combine the two equations to obtain 

$$
\begin{equation}
  \gamma_a^p\gamma_b^q {}^4R_{pq} 
  = -\alpha^{-1}\mathcal{L}_m K_{ab} - \alpha^{-1}D_aD_b\alpha +
    R_{ab} + K K_{ab} - 2 K_{ar} K^r_b.
\end{equation}
$$

### (Soln) 2.3

**Preliminaries**:

For this we need $K{}_{ab}=-\nabla{}_a[n{}_b]-n{}_a a{}_b$, $\mathcal{T}_1(\Sigma)\ni a{}_b:=n{}^a\nabla{}_a[n{}_b]$, $a{}_b=D{}_b[\log(\alpha)]$, $D{}_a[a{}_b]=-a{}_a a{}_b+\frac{1}{\alpha}D{}_a[D{}_b[\alpha]]$.

Note: $a{}_b=D{}_b[\log(\alpha)]$ essentially follows from $\nabla{}_a[\nabla{}_b[t]]=\nabla{}_b[\nabla{}_a[t]]$.
Recall: If hypersurfaces $\Sigma$ are level surfaces of coordinate time function $t$. Put $\Omega{}_a:=\nabla{}_a[t]$ and introduce the usual normalisation such that $\Omega{}_a:=\frac{1}{\alpha} n{}_a$ $(n{}^a n{}_a=-1)$.

$$
\begin{align*}
  a{}_b&=n{}^a \nabla{}_a[n{}_b]
  =
  n{}^a\nabla{}_a[\alpha\Omega{}_b]
  =
  n{}^a\nabla{}_a[\alpha\nabla{}_b[t]],\\
  &=
  n{}^a\Big[
    \nabla{}_a[\alpha]\nabla{}_b[t]
    +\alpha\nabla{}_a[\nabla{}_b[t]]
  \Big],\\
  &=
  n{}^a\Big[
  \nabla{}_a[\alpha]\Omega{}_b
  +\alpha \nabla{}_b[\nabla{}_a[t]]
  \Big],\\
  &=
  n{}^a\Big[
    \nabla{}_a[\alpha] n{}_b /\alpha
    +\alpha \nabla{}_b[\Omega{}_a]
  \Big],\\
  &=
  n{}^a\left(
    n{}_b\nabla{}_a[\log(\alpha)]
    +\alpha \nabla{}_b[n{}_a/\alpha]
  \right),\\
  &=
  n{}^a\Big(
    n{}_b\nabla{}_a[\log(\alpha)]
    -\frac{1}{\alpha}
    \nabla{}_b[\alpha]
    +\nabla{}_b[n{}_a]
  \Big)
\end{align*}
$$

Projecting yields: $a{}_b=\frac{1}{\alpha}D{}_a[\alpha]$.

Consider derivative:

$$
\begin{align}
  D{}_a[a{}_b] &= D{}_a\Big[
    \frac{1}{\alpha}D{}_b[\alpha]
  \Big]
  =
  D{}_a[1/\alpha] D{}_b[\alpha]
  +
  \frac{1}{\alpha} D{}_a[D{}_b[\alpha]],\\
  &=-\frac{1}{\alpha{}^2}D{}_a[\alpha]D{}_b[\alpha]
  +\frac{1}{\alpha}D{}_a[D{}_b[\alpha]],\\
  &=
  -\left[\frac{1}{\alpha}D{}_a[\alpha] \right]
  \left[\frac{1}{\alpha}D{}_b[\alpha] \right]
  +\frac{1}{\alpha} D{}_a[D{}_b[\alpha]],\\
  &=-a{}_a a{}_b + \frac{1}{\alpha}D{}_a[D{}_b[\alpha]].
\end{align}
$$

**Derivation of result**:
Consider Lie-derivative along normal direction:

$$
\begin{align}
  \mathcal{L}_{\mathbf{n}}[K{}_{ab}] &=
  n{}^c\nabla{}_c[K{}_{ab}]
  + K{}_{ac}\nabla{}_b[n{}^c]
  + K{}_{bc}\nabla{}_a[n{}^c],\\
  &=
  n{}^c \nabla{}_c[-\nabla{}_a[n{}_b] - n{}_a a{}_b]
  + K{}_{ac}\nabla{}_b[n{}^c] + K{}_{bc}\nabla{}_a[n{}^c],\\
  &=
  n{}^c\nabla{}_c[-\nabla{}_a[n{}_b]-n{}_a a{}_b]
  + K{}_a{}^c\underbrace{\nabla{}_b[n{}_c]}_{
    =-K{}_{bc}-n{}_ba{}_c
  }
  + K{}_b{}^c\underbrace{\nabla{}_a[n{}_c]}_{
    =-K{}_{ac}-n{}_a a{}_c
  },\\
  &=
  -n{}^c \nabla{}_c[\nabla{}_a[n{}_b]]
  -n{}^c\nabla{}_c[n{}_a a{}_b]
  -K{}_a{}^c(K{}_{bc}+n{}_b a{}_c)
  -K{}_b{}^c(K{}_{ac}+n{}_aa{}_c),
\end{align}
$$

The first term may be replaced with:

$$
\begin{align}
  {}^{[4]}\mathrm{Riem}{}_{dbac}n{}^d &=
  2\nabla{}_{[c}[\nabla{}_{a]}[n{}_b]]
  =(\nabla{}_c \nabla{}_a - \nabla{}_a \nabla_c)[n{}_b],\\
  \Longleftrightarrow -{}^{[4]}\mathrm{Riem}{}_{dbac}n{}^d
  +\nabla{}_a[\nabla{}_c[n{}_b]] &= \nabla{}_c[\nabla{}_a[n{}_b]].
\end{align}
$$

It follows then:

$$
\begin{align*}
  \mathcal{L}{}_{\mathbf{n}}[K{}_{ab}]
  &= n{}^c n{}^d {}^{[4]}\mathrm{Riem}{}_{dbac}
  - n{}^c \nabla{}_a[\nabla{}_c[n{}_b]]
  - n{}^c \nabla{}_c[n{}_a] a{}_b
  - n{}^c n{}_a \nabla{}_c[a{}_b],\\
  &\quad
  -K{}_a{}^c(K{}_{bc}+n{}_ba{}_c)
  -K{}_b{}^c(K{}_{ac}+n{}_aa{}_c),\\
  &=
  n{}^c n{}^d {}^{[4]}\mathrm{Riem}{}_{dbac}
  -n{}^c\nabla{}_a[\nabla{}_c[n{}_b]]
  -a{}_a a{}_b
  -n{}^c n{}_a \nabla{}_c[a{}_b],\\
  &\quad
  -K{}_a{}^c(K{}_{bc}+n{}_b a{}_c)
  -K{}_b{}^c(K{}_{ac}+n{}_a a{}_c);
\end{align*}
$$

Note the rewriting:

$$
\begin{align*}
  n{}^c \nabla{}_a[\nabla{}_c[n{}_b]]
  &=
  \nabla{}_a[\underbrace{n{}^c \nabla{}_c[n{}_b]}_{=a{}_b}]
  -\nabla{}_a[n{}^c]\nabla{}_c[n{}_b],\\
  &=
  \nabla{}_a[a{}_b]
  - K{}_a{}^c K{}_{cb}
  - n{}_a a{}^c K{}_{cb}.
\end{align*}
$$

We can therefore cancel terms:

$$
\begin{align*}
  \Longrightarrow
  \mathcal{L}_{\mathbf{n}}[K{}_{ab}]
  =
  -n{}^d n{}^c
  {}^{[4]} R{}_{dbac}
  -\nabla{}_a[a{}_b]
  -n{}^c n{}_a
  \nabla{}_c[a{}_b]
  -a{}_a a{}_b
  -K{}^c{}_b K{}_{ac}
  -K{}_{ca} n{}_b a^c,
\end{align*}
$$

Notice that $\mathcal{L}_{\mathbf{n}}[K{}_{ab}]$ is spatial, i.e.,

$$
\begin{align*}
  n{}^a \mathcal{L}_{\mathbf{n}}[K{}_{ab}]
  &=
  -\underbrace{
  n{}^a n{}^d n{}^c {}^{[4]}\mathrm{Riem}{}_{dbac}
  }_{{}^{[4]}\mathrm{Riem}{}_{db(ac)}=0}
  -n{}^a\nabla{}_a[a{}_b]
  -n{}^c n{}^a n{}_a \nabla{}_c[a{}_b]
  -n{}^a a{}_a a{}_b\\
  &\quad
  -\underbrace{n{}^a K{}_{ac}}_{=0} K{}^c{}_b
  -\underbrace{n{}^a K{}_{ca}}_{=0} n{}_b a{}^c,\\
  &=
  -n{}^a \nabla{}_a[a{}_b] - n{}^c n{}^a
  n{}_a \nabla{}_c[a{}_b]
  = -n{}^a \nabla{}_a[a{}_b]
  + n{}^c \nabla{}_c[a{}_b] =0.
\end{align*}
$$

Therefore we lose no information taking a spatial projection on free indices:

$$
\begin{align*}
  \mathcal{L}_{\mathbf{n}}[K{}_{ab}]
  &=
  -n{}^d n{}^c \gamma{}^q_a \gamma{}^r_b
  {}^{[4]}\mathrm{Riem}{}_{drqc}
  -\underbrace{\gamma{}^q_a\gamma{}^r_b\nabla{}_q[a_r]}_{
    D{}_a[a{}_b]
  }
  -a{}_aa{}_b
  -K{}^c{}_b K{}_{ac},\\
  &= -n{}^d n{}^c \gamma{}^q_a \gamma{}^r_b
  {}^{[4]}\mathrm{Riem}_{drqc}
  -\frac{1}{\alpha} D{}_a[D{}_b[\alpha]]
  -K{}^c{}_b K{}_{ac},
\end{align*}
$$

where we used $D{}_a[a{}_b]=-a{}_a a{}_b + \frac{1}{\alpha} D{}_a[D{}_b[\alpha]]$.