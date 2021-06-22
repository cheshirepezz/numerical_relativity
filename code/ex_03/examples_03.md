## Brief on Kruskal-Szekeres (KS) diagrams:

This is meant to be a brief refresh on where KS comes from. There is a much more in-depth discussion of this and other matters in Blau's lecture notes on GR. Other good references are Poisson's "A Relativist's toolkit" and as usual Wald.

Write Schwarzschild (standard coordinates) in the form:

$$
\begin{equation}
  \d s^2 = (1 - 2m/r)(-\d t^2 + (1-2m/r)^{-2}\d r^2) +r^2\d \Omega^2.
\end{equation}
$$

It is convenient to introduce a new radial coordinate $r^*$ via :

$$
\begin{equation}
\d r^* = (1-2m/r)^{-1}\d r
= \frac{r}{r-2m}\d r
= \left(1+\frac{2m}{r-2m} \right)\d r,
\end{equation}
$$
leading to:

$$
\begin{equation}
  r^* = r + 2m\log(r/(2m) - 1).
\end{equation}
$$

The coordinate $r^*$ is known as _tortoise coordinate_.

Notice that we may now write:

$$
\begin{equation}
  \d s^2 = (1-2m/r)(-\d t^2 + \d {r^*}^2) + r^2 \d \Omega^2,
\end{equation}
$$

where $r=r(r^*)$.

We may introduce coordinates adapted to _null_ geodesics through the choice of retarded and advanced time coordinates:

$$
\begin{aligned}
  u &= t -r^*, & v = t + r^*;
\end{aligned}
$$

which respectively characterise outgoing and ingoing null geodesics. This provides a neat characterisation as when $u=\mathrm{const}$ we have $\d r^* / \d t=+1$ and similarly for $v$.

This motivates replacing $(t,\,r,\,\vartheta,\varphi)$ with $(v,\,r,\,\vartheta,\,\varphi)$ or $(u,\,r,\,\vartheta,\,\varphi)$; commonly known as Eddington-Finkelstein (EF) coordinates. Thus for ingoing (advanced) and outgoing (retarded) EF coordinates the Schwarzschild metrics reads:

$$
\begin{aligned}
  \d s^2 &= -(1-2m/r)\,\d v^2 + 2 \d v\,\d r + r^2 \d \Omega^2,\\
  \d s^2 &= -(1-2m/r)\,\d u^2 - 2 \d u\,\d r + r^2 \d \Omega^2;
\end{aligned}
$$

respectively. The above provides the idea on how to (partially) extend Schwarzschild in order to investigate $r=2m$ without issues.

For the maximal extension / KS one goes a step further and simultaneously replaces with $(u,\,v)$ such that $(t,\,r,\,\vartheta,\,\varphi)$ becomes $(u,v,\,\vartheta,\,\varphi)$. This yields:

$$
\begin{equation}
  \d s^2 = -(1-2m/r)\,\d u\,\d v + r^2 \d \Omega^2,
\end{equation}
$$

where we take $r=r(u,\,v)$. This is still a bit awkward as the black hole horizon is infinitely far away ($u\rightarrow \infty$ or $v\rightarrow -\infty$, or $2r^*=v-u\rightarrow-\infty$).

We can bring the horizon to a finite location of a new coordinate system $(U,\,V)$, with the mapping:

$$
\begin{aligned}
  U &= -\exp\left(-\frac{u}{4m}\right), &
  V &= \exp\left(\frac{v}{4m}\right);
\end{aligned}
$$

where the choice of factors in the exponential follow from considering $v-u$, its relation to $r^*$ and a rewriting of $1-2m/r$. Using this choice, we arrive at:

$$
\begin{equation}
  \d s^2 = -\frac{32m^3}{r} \exp\left(
  -\frac{r}{2m}
  \right)\, \d U\, \d V + r(U,\,V)^2\,\d\Omega^2,
\end{equation}
$$

with $r$ and $t$ specified implicitly through:

$$
\begin{aligned}
  UV &= -\exp\left(\frac{v-u}{4m} \right)
  = -\exp\left(\frac{r^*}{2m}\right)
  = -\left(\frac{r}{2m}-1 \right) \exp\left(\frac{r}{2m}\right),\\
  U/V &= -\exp\left(-\frac{u+v}{4m}\right)
  = - \exp\left(-\frac{t}{2m}\right).
\end{aligned}
$$

As a final step, we can switch back from the null $(U,\,V)$ to time-like and space-like $(T,\,X)$ by mapping once more:

$$
\begin{aligned}
  U&=T-X, & V&=T+X,
\end{aligned}
$$

wherein:

$$
\begin{equation}
  \tag{$\star$}
  \d s^2 = \frac{32m^3}{r} \exp\left(-\frac{r}{2m}\right)
  \left(-\d T^2 + \d X^2 \right) + r^2 \d\Omega^2.
\end{equation}
$$

Here $r=r(T,\,X)$ is specified in an implicit relation:

$$
\begin{equation}
  X^2-T^2 = \left(
  \frac{r}{2m}-1
  \right)\exp\left(\frac{r}{2m}\right).
\end{equation}
$$

In summary, we chased the sequence of transformations:

$$
\begin{equation}
  (t,\,r)\rightarrow(t,\,r^*)\rightarrow(u,\,v)
  \rightarrow (U,\,V)\rightarrow (T,\,X),
\end{equation}
$$

where the overall mapping explicitly becomes:

$$
\begin{aligned}
  T(t,\,r) &= \frac{1}{2}(U+V) =
  \left(\frac{r}{2m}-1\right)^{1/2}
  \exp\left(\frac{r}{4m}\right)
  \sinh \left(\frac{t}{4m}\right),\\
  X(t,\,r) &= \frac{1}{2}(V-U) =
  \left(\frac{r}{2m}-1\right)^{1/2}
  \exp\left(\frac{r}{4m}\right)
  \cosh \left(\frac{t}{4m}\right).
\end{aligned}
$$

### some interpretation:

- The **main point** of all this:
  We perform a sequences of coordinate mappings to dodge a coordinate issue: In Eq.$(\star)$ for $r\neq 0$ we have a manifestly non-singular form of the Schwarzschild even at the horizon.
- The original "Schwarzschild patch" $r>2m$ corresponds to $U\in(-\infty,0)$ and $V\in(0,\,\infty)$; which in terms of $X$ and $T$ is $X>0$ and $X^2-T^2>0$. In the $T$-$X$ plane this corresponds to the region bounded by $X=\pm T$.
![[_img/2021_05_20_tutorial/Pasted image 20210520104628.png]]
- Null lines are given by $X=\pm T + \mathrm{const}$ whereas surfaces at fixed $r$ live on the hyperbolae $X^2-T^2=\mathrm{const}$.
- The horizon $r=2m$ in terms of $(U,\,V)$ is mapped to $UV=0$ and in terms of $(T,\,X)$ one has $r=2m\Longrightarrow X=\pm T$.

### Kruskal-Szekeres diagram:

We work with $(T,\,X)$, allowing these coordinates to range over all values for which Eq.$(\star)$ is non-singular (i.e. $r\neq 0$). We must exclude only:

$$
\begin{aligned}
  r=0 \Longleftrightarrow T^2-X^2=1
  \Longleftrightarrow T=\pm \sqrt{1+X^2}.
\end{aligned}
$$

The mapping $(t,\,r)\rightarrow(T,\,X)$ splits into quadrants with the usual (exterior) Schwarzschild living in $\mathrm{I}$, and the interior in $\mathrm{II}$. We also have new regions e.g. $\mathrm{III}$ (causally disconnected from $\mathrm{I}$). In each quadrant a suitable set of Schwarzschild-like coordinates may be chosen though they will only cover a (proper) subset of $\mathrm{I}$-$\mathrm{IV}$.

![[_img/2021_05_20_tutorial/Pasted image 20210520110653.png]]

- When thinking about this diagram recall (see above) that null lines are diagonals $X=\pm T + \mathrm{const}$; the horizon lives at $X=\pm T$.
- Lines of constant $r$ are hyperbolas; in particular, the singularity at $r=0$ is represented by $T^2-X^2=1$.
- Lines of constant (Schwarzschild) $t$ are straight lines through the origin. For example in $\mathrm{I}$ we have $X=(\coth(t/(4m)))T$ with (future) horizon $X=T$ corresponding to $t\rightarrow \infty$. 
- EF coordinates (retarded) $(u,\,r,\,\vartheta,\,\varphi)$ cover $\mathrm{I}$ and $\mathrm{II}$ whereas (advanced) $(u,\,r,\,\vartheta,\,\varphi)$ cover $\mathrm{I}$ and $\mathrm{IV}$.
- Isotropic coordinates cover $\mathrm{I}$ and $\mathrm{III}$.