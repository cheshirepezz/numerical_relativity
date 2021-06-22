## A look at numerical evolution: Spherical ADM
We have some experience with numerically solving elliptic and hyperbolic PDE from the first assignment and have now seen how the ADM formulation provides a description of the Einstein equations posed as an evolution problem.

Our goal here is to consider a simple situation in order to perform some numerical experiments with the ADM formulation. To make it more manageable we will restrict attention to _spherically symmetric_, _vacuum space-time_. Already here we will see that the problem is non-trivial.

Recall that in the ADM formalism the space-time metric is decomposed as:

$$

\begin{equation}
	\d s^2 = -\alpha{}^2 \,\d t{}^2
	+\gamma{}_{ij}
	\big(
		\d x{}^i + \beta{}^i \d t
	\big)
	\big(
		\d x{}^j + \beta{}^j \d t
	\big);
\end{equation}

$$

and one works with (here vacuum) evolution equations:

$$
\begin{aligned}
	\partial{}_\perp[\gamma{}_{ij}]
	&=
	-2\alpha K{}_{ij},\\
	\nonumber
	\partial{}_\perp[K{}_{ij}]
	&=
	-\D{}_i[\D{}_j[\alpha]]
	+\alpha
	\Big[
		\mathrm{Ric}{}_{ij}+\mathcal{K} K{}_{ij}-2K{}_{ik}K{}^k{}_j
	\Big];
\end{aligned}
$$

where dynamical variables must satisfy the constraints:

$$
\begin{align}
	\mathcal{H} &:=
	\frac{1}{2}(\mathcal{R}[\gamma]
	+\mathcal{K}^2-K{}_{ij}K{}^{ij})= 0,\\
	\mathcal{M}^i &:=
	\D{}_j(K{}^{ij} - \gamma{}^{ij} \mathcal{K})=0.
\end{align}
$$

Let us particularize to adapted coordinates $x{}^\mu\dot{=}(t,\,r,\,\vartheta,\,\varphi)$. In spherical symmetry the space-time metric may be written as:

$$
\begin{equation}
  \d s{}^2=-(\alpha^2+\beta{}_i\beta{}^i)\d t{}^2
  +2\beta{}_r \d t \d r + \gamma{}_{rr} \d r^2
  + \gamma{}_{\vartheta\vartheta} \d \Omega^2,
\end{equation}
$$

where $\d \Omega^2 := \d\vartheta{}^2+\sin^2\vartheta\,\d\varphi^2$ and $\beta{}^i\dot{=}(\beta{}^r,\,0,\,0)$.

Suppose $t$ is fixed. Under this assumption a spatial symmetric $2$-tensor $\mathcal{S}{}_{ij}=\mathcal{S}{}_{(ij)}\in\mathcal{T}_2(\Sigma)$ may be written in the form:

$$
\begin{equation}
  \mathcal{S}{}_{ij} \d x{}^i \d x{}^j=
  s{}_1(r)\d r{}^2
  + s{}_2(r) \d \vartheta{}^2
  + s{}_2(r) \sin^2(\vartheta) \d \varphi^2.
\end{equation}
$$

We therefore put $\gamma{}_{ij}\dot{=}\mathrm{diag}(\gamma{}_1(r),\,\gamma{}_2(r),\, \gamma{}_2(r)\sin^2(\vartheta))$, $K{}_{ij}\dot{=}\mathrm{diag}(\kappa{}_1(r),\,\kappa{}_2(r),\, \kappa{}_2(r)\sin^2(\vartheta))$ and take $\beta{}^r=\beta{}^r(r)$. This general form holds for all $t$ thus we immediately allow for coefficient functions to pick up a $t$ dependence in addition to $r$. Inserting into the above leads to:

$$
\begin{aligned}
  \partial{}_t[\gamma{}_1]
  &=
  -2\alpha \kappa{}_1 + 2 \gamma{}_1 \partial_r[\beta{}^r]
  +\beta{}^r \partial_r[\gamma{}_1],\\
  \partial{}_t[\gamma_2]
  &=
  -2\alpha\kappa{}_2 + \beta{}^r \partial_r[\gamma{}_2],\\
  \partial{}_t[\kappa{}_1]
  &=
  -\frac{\alpha \kappa{}_1^2}{\gamma{}_1}
  +\frac{2\alpha\kappa{}_1\kappa{}_2}{\gamma{}_2}
  +2\kappa{}_1\partial{}_r[\beta{}^r]
  +\frac{\partial{}_r[\alpha]\partial{}_r[\gamma{}_1]}{2\gamma{}_1}
  +\frac{\alpha\partial{}_r[\gamma{}_1]\partial{}_r[\gamma{}_2]}{2\gamma{}_1\gamma{}_2}
  +\frac{\alpha(\partial{}_r[\gamma{}_2]^2)}{2\gamma{}_2^2}
  +\beta{}^r\partial{}_r[\kappa{}_1]
  -\partial{}_{rr}[\alpha]
  -\frac{\alpha\partial{}_{rr}[\gamma{}_2]}{\gamma{}_2},\\
  \partial{}_t[\kappa{}_2]
  &=
  \alpha
  +\frac{\alpha\kappa{}_1\kappa{}_2}{\gamma{}_1}
  -\frac{\partial{}_r[\alpha]\partial{}_r[\gamma{}_2]}{2\gamma{}_1}
  +\frac{\alpha\partial{}_r[\gamma{}_1]\partial{}_r[\gamma{}_2]}{4\gamma{}_1^2}
  +\beta{}^r\partial{}_r[\kappa{}_2]
  -\frac{\alpha \partial{}_{rr}[\gamma{}_2]}{2\gamma{}_1};
\end{aligned}
$$

for the evolution equations, whereas constraints become:

$$
\begin{aligned}
  \mathcal{H} &:=
  \frac{1}{2\gamma{}_1^2\gamma{}_2^2}
  \left[
  4\gamma{}_1^2(\gamma{}_2+\kappa{}_2^2)
  +2\gamma{}_2 \partial{}_r[\gamma{}_1]\partial{}_r[\gamma{}_2]
  +\gamma{}_1\left(
    \partial{}_r[\gamma{}_2]^2
    +\gamma{}_2\left[
      8\kappa{}_1\kappa{}_2 - 4\partial{}_{rr}[\gamma{}_2]
    \right]
  \right)
  \right]=0,\\
  \mathcal{M}{}^r &:=
  \frac{1}{\gamma{}_1 \gamma{}_2^2}
  \left[
    (\gamma{}_2\kappa{}_1+\gamma{}_1\kappa{}_2)\partial{}_r[\gamma{}_2]
    -2\gamma{}_1\gamma{}_2\partial{}_r[\kappa{}_2]
  \right]=0.
\end{aligned}
$$

An example of deriving these is provided in the accompanying `xTensor`/`xCoba` notebook.


We have a system but **many choices** remain: initial data, gauge, domain, boundary conditions, choice of discretization etc.

**Gauge choice**:

Many options exist with their own (dis)advantages. Here are a few well-known / explored variants:
- Gaussian normal coordinates (geodesic slicing)
$$
\begin{aligned}
  \alpha &= 1, & \beta{}^i=0.
\end{aligned}
$$
- "$1+\log$" slicing with zero shift:
$$
\begin{aligned}
  \partial{}_t[\alpha] &= \beta{}^r \partial{}_r[\alpha]-2\alpha \mathcal{K}
  , & \beta{}^i=0.
\end{aligned}
$$
- Bona-Masso family of slicings:
$$
\begin{aligned}
  \partial{}_t[\alpha] = \beta{}^r\partial{}_r[\alpha]-\alpha{}^2f[\alpha]\mathcal{K}.
\end{aligned}
$$
- Maximal slicing (see exercise).


**Domain**:

In order to keep matters simple we will be interested in evolution on a finite spatial domain $r\in[0,\,R]$. Interesting alternatives such as spatial compactification out to $i{}^0$ could also be explored...

**Boundary conditions** (outer):

It turns out that this is actually a rather intricate problem in GR both conceptually and to deal with rigorously in full generality. For our purposes here we will take a heuristic view where we assume either _outflow_ or _Sommerfeld_ conditions. In the first case we have:
- $1^\mathrm{st}$ order extrapolation: $f{}_{N+1}=f{}_{N}$.
- $2^\mathrm{nd}$ order extrapolation: $f{}_{N+1}=2f{}_{N}-f{}_{N-1}$.

**Boundary conditions** (inner):

Due to our coordinate choice, we also need to deal with conditions at $r=0$. As short-hand call scalars (S), vectors (V) and tensors (T).

- **(I) parity**: from Taylor expansion it follows that about $r=0$ under $r\rightarrow -r$:
  - (S,T) are **even** as they satisfy $f(r)=f(0)+\frac{1}{2}f'(0)r^2+\mathcal{O}(r^4)$.
  - (V) are **odd** as they satisfy $f(r)=f'(0)r+\frac{1}{6}f'''(0)r^3+\mathcal{O}(r^5)$.

- **(II) local flatness**: One can always pick coordinates (**locally**) where the metric takes Minkowskian form and first derivatives vanish. This means that at $r=0$ we should be able to write (with $R:=R(r)$):
$$
\begin{aligned}
 \left. \d s^2 \right|_{R\sim 0} &= \d R{}^2+R{}^2 \d\Omega^2,\\
 \Longrightarrow \left.\d s^2\right|_{r\sim0} &=
 \left.\left(\frac{\d R}{\d r} \right)^2\right|_{r=0}
 \left[\d r^2 + r{}^2 \d\Omega^2 \right];
\end{aligned}
$$
or relating this to our initial assumption on $\boldsymbol{\gamma}$ we require $\gamma{}_1=\gamma{}_2/r^2$ as $r\rightarrow 0$; this is not so trivial to impose.

**Discretization**:

Here we fortunately have already done the work in a previous assignment. We can recycle the approach of constructing discretized derivative operators and Runge-Kutta based time integration via method of lines.

On account of needing to impose parity, we will take the approach of using a staggered (sometimes called cell-centered) grid. This means that the first physical node does not begin at $r=0$ but instead lives at $r=\Delta r/2$.

**Other things to consider**:

In addition to having made these choices many additional considerations remain:
- What are the asymptotics - can we make a better ansatz?
- Is this system actually well-posed?
- What sort of **toy-problem** should we pick?

**Toy problem**:

As a first problem we consider whether we can set up the evolution problem (with geodesic gauge) to reproduce Minkowski space.

On the inner boundary we impose parity conditions as above whereas on the outer boundary we impose an extrapolation condition; together this lets us populate data in ghost-zones and compute derivatives. We use standard MOL for the time-evolution.

**Potential extensions**:

- Higher spatial order
- Better treatment of regularity at the origin / external BC
- Investigate other gauge choices
- Incorporate asymptotic flatness conditions / conformal conditions:

Suppose that we map:

$$
\begin{aligned}
  \gamma{}_1 \mapsto\tilde{\gamma}{}_1 &= \gamma{}_1 \psi^{-4},\\
  \gamma{}_2 \mapsto\tilde{\gamma}{}_2 &= \gamma{}_2 r^{-2}\psi^{-4},\\
  \kappa{}_1 \mapsto\tilde{\kappa}{}_1 &= \kappa{}_1,\\
  \kappa{}_2 \mapsto\tilde{\kappa}{}_2 &= \kappa{}_2 r^{-2}.
\end{aligned}
$$

then in geodesic gauge (with $\psi(r)=1$) we see that as $\tilde{\gamma{}}_1,\,\tilde{\gamma{}}_2\rightarrow 1$ then $\d s^2\rightarrow \boldsymbol{\eta}$; i.e. we approach Minkowski form. Allowing $\psi(r)$ to be non-trivial also opens the door to exploring (e.g.) Schwarzschild etc..