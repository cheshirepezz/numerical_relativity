# ADM in spherical symmetry

In spherical symmetry we may take the general form of a spatial metric to be:

$$
\begin{aligned}
  \gamma{}_{ij}\d x{}^i \d x{}^j
  &=
  \gamma{}_1(t,\,r) \d r{}^2
  + r{}^2 \gamma{}_2(t,\,r) \d\Omega{}^2,
  &
  \d\Omega{}^2:=\d\vartheta{}^2 + \sin^2(\vartheta)\,\d\varphi{}^2.
\end{aligned}
$$

More generally, analogous forms may be adopted for any symmetric tensor field $S{}_{(ij)}=S{}_{ij}\in\mathcal{T}_2(\Sigma_t)$.

Define the variables:

$$
\begin{aligned}
  \D{}_{\alpha} &:= \partial{}_r[\log(\alpha)],
   &
   \Gamma{}_1 &:= \partial{}_r[\log(\gamma{}_1)],
   &
   \Gamma{}_2 &:=\partial{}_r[\log(\gamma{}_2)],
\end{aligned}
$$

it can be shown that when working in vacuum and in the absence of spatial shift the standard ADM evolution equations may be re-written as:

$$
\begin{aligned}
  \partial{}_t[\gamma{}_1] 
  &=
  -2\alpha \gamma{}_1 \overline{\kappa}{}_1,\\
  \partial{}_t[\gamma{}_2] 
  &=
  -2\alpha \gamma{}_2 \overline{\kappa}{}_2,\\
  \partial{}_t[\Gamma{}_1]
  &=-2\alpha(\overline{\kappa}{}_1 \D{}_\alpha
  +\partial{}_r[\overline{\kappa}{}_1]),\\
  \partial{}_t[\Gamma{}_2]
  &=
  -2\alpha(\overline{\kappa}{}_2\D{}_\alpha
  +\partial{}_r[\overline{\kappa}{}_2]),\\
  \partial{}_t[\overline{\kappa}{}_1]
  &=
  -\frac{\alpha}{\gamma{}_1}
  \Bigg[
    \partial{}_r[\D{}_\alpha+\Gamma{}_2]
    +\D{}_\alpha^2
    -\frac{\D{}_{\alpha} \Gamma{}_1}{2}
    +\frac{\Gamma_2^2}{2}
    -\frac{\Gamma{}_1\Gamma{}_2}{2}\\
  &
  -\gamma{}_1\overline{\kappa}{}_1(
    \overline{\kappa}{}_1+2\overline{\kappa}{}_2
  ) - \frac{1}{r}(\Gamma{}_1-2\Gamma{}_2)
  \Bigg],\\
  \partial{}_t[\overline{\kappa}_2]
  &=
  -\frac{\alpha}{2\gamma{}_1}
  \Bigg[
    \partial{}_r[\Gamma{}_2]
    +\D{}_{\alpha}\Gamma{}_2
    +\Gamma{}_2^2 - \frac{\Gamma{}_1\Gamma{}_2}{2}
    -\frac{1}{r}(\Gamma{}_1-2\D{}_\alpha-4\Gamma{}_2)\\
    &
    -\frac{2}{\gamma{}_2}\left\{
    \frac{(\gamma{}_1-\gamma{}_2)}{r^2}
    \right\}
  \Bigg] + \alpha\overline{\kappa}{}_2(
  \overline{\kappa}{}_1 + 2 \overline{\kappa}{}_2
  );
\end{aligned}
$$

whereas the constraints may be put in the form:

$$
\begin{aligned}
  \mathcal{H}&:=
  -\partial{}_r[\Gamma{}_2]
  +\left\{
    \frac{\gamma{}_1-\gamma{}_2}{r^2\gamma{}_2}
  \right\}
  +\gamma{}_1 \overline{\kappa}{}_2(2\overline{\kappa}{}_1
  +\overline{\kappa}{}_2)\\
  &
  +\frac{1}{r}(\Gamma{}_1-3\Gamma{}_2)
  +\frac{\Gamma{}_1\Gamma{}_2}{2}
  -\frac{3\Gamma{}_2^2}{4} = 0,\\
  \mathcal{M}{}_r&:=
  -\partial{}_r[\overline{\kappa}{}_2]
  +\left\{
    \frac{\overline{\kappa}{}_1-\overline{\kappa}{}_2}{r}
  \right\}
  +\frac{1}{2}(\overline{\kappa}{}_1-\overline{\kappa}{}_2)\Gamma{}_2 = 0;
\end{aligned}
$$

where $\overline{\kappa}_I:=\kappa{}_I / \gamma{}_I$ (no sum, $I=1,\,2$).

**(I)**: Derive the above system.
**(II)**: Recall that adapted coordinates can carry a downside of having to treat apparent coordinate singularities by regularizing. In the present case we have formal behaviour in the vicinity of $r=0$:

$$
\begin{aligned}
  \gamma{}_I &\sim \gamma{}^0_I + \mathcal{O}(r^2), &
  \overline{\kappa}{}_I & \sim \overline{\kappa}{}^0_I
  +\mathcal{O}(r^2);
\end{aligned}
$$

what are the analogous conditions for $\Gamma{}_I$? These yield us parity conditions that we looked at imposing in the last tutorial through a staggered grid.

**(III)**: If we take into account local flatness (at $r=0$) what additional relations must be simultaneously satisfied? Why does this complicate matters?

**(IV)**: In order to implement the full set of conditions found in the previous part it is useful to introduce a new auxiliary variable:

$$
\begin{equation}
  \lambda:=\frac{1}{r}\left(1-\frac{\gamma{}_1}{\gamma{}_2} \right).
\end{equation}
$$

  - What is the parity condition on $\lambda$?
  - Use this variable to remove the curled brace term in $\partial{}_t[\overline{\kappa}{}_2]$ together with $\mathcal{H}$.
  - Derive a _regular_ evolution equation for $\lambda$. To do this differentiate and make use of the momentum constraint component.

**(V)**: In principle we would like to be able to perform an evolution for some test problem. We could pick (e.g.) Bona-Masso slicing:

$$
\begin{equation}
  \partial{}_t[\alpha] = -\alpha{}^2 f(\alpha) \mathcal{K}
  =-\alpha{}^2 f(\alpha)[\overline{\kappa}{}_1 + 2 \overline{\kappa}{}_2].
\end{equation}
$$

Derive an equation for $\partial{}_t[\D_\alpha]$.

**(VI)**: An immediate question arises as to whether there are any obvious restrictions on $f(\alpha)$. To answer this consider putting $u:=(\alpha,\,\gamma{}_1,\,\gamma{}_1,\,\lambda)$ together with $v=(\D_\alpha,\,\Gamma{}_1,\,\Gamma{}_2,\,\overline{\kappa}{}_1,\,\overline{\kappa}{}_2)$ such that we may generically write our system as:

$$
\begin{aligned}
  \partial{}_t[u{}_i] &= q{}_i(u,\,v),\\
  \partial{}_t[v{}_i] &= M{}^j_i(u) \partial{}_r[v{}_j]
  + p{}_i(u,\,v);
\end{aligned}
$$

where $q$ and $p$ are source terms. Investigate the characteristic structure of $M{}^j_i$ writing down the eigenfields and eigenvalues.

**(VII)**: (Optional) verify that the above steps of regularization significantly mitigate stability issues encountered in the example code of the last tutorial.

**(VIII)**: (Optional) recall that a spatial slice of Schwarzschild may be written in isotropic form as:

$$
\begin{aligned}
  \gamma{}_{ij}\d x^i\d x^j &=
  \psi^4 (\d r^2+r^2\d\Omega^2), &
  \psi &= 1 + M/(2r).
\end{aligned}
$$

In the static puncture evolution technique one extracts analytically the conformal factor through field re-definitions:

$$
\begin{aligned}
  \tilde{\gamma}{}_1 &:= \gamma{}_1 / \psi^4, &
  \tilde{\gamma}{}_2 &:= \gamma{}_2 / \psi^4;\\
  \tilde{\Gamma}{}_1 &:= \Gamma{}_1 - 4 \partial{}_r[\log(\psi)],
  &
  \tilde{\Gamma}{}_2 &:= \Gamma{}_2 - 4 \partial{}_r[\log(\psi)];
\end{aligned}
$$

with other variables left as previously regularized. Modify your regularized example code to perform an evolution for the case that $f=2/\alpha$ and comment on what you observe.

## (soln)

### (I):

See notebook.

### (II):

Collectively, we have behaviour for $r\rightarrow 0$ as:

$$
\begin{aligned}
  \gamma{}_I &\sim \gamma{}^0_I
  + \mathcal{O}(r^2), &
  \Gamma{}_I &\sim \mathcal{O}(r), &
  \overline{\kappa}{}_I &\sim
  \overline{\kappa}{}^0_I
  + \mathcal{O}(r^2);
\end{aligned}
$$

Thus $\gamma{}_I$ and $\overline{\kappa}{}_I$ are _even_ about the origin whereas $\Gamma{}_I$ are _odd_.

### (III):

The main reason matters are complicated is that we want to simultaneously impose more conditions than we have easy access to do.

As the fields $\D_\alpha\sim\mathcal{O}(r)$ and $\Gamma{}_I\sim\mathcal{O}(r)$ near the origin terms such as $\D{}_\alpha/r$ and $\Gamma{}_I/r$ should not cause problems.

On the other hand curled braces terms such as $(\gamma{}_1-\gamma{}_2)/r^2$ and $(\overline{\kappa}{}_1-\overline{\kappa}{}_2)/r$ require differences of terms to precisely follow:

$$
\begin{aligned}
  \gamma{}_1-\gamma{}_2&\sim\mathcal{O}(r^2),
  &
  \overline{\kappa}{}_1-\overline{\kappa}{}_2
  &
  \sim\mathcal{O}(r^2).
\end{aligned}
$$

In other words we must simultaneously also have that (compare behaviour in prior part):

$$
\begin{aligned}
  \gamma{}^0_1=\gamma{}^0_2,
\end{aligned}
$$

and this must hold for all $t$, thus $\overline{\kappa}{}^0_1=\overline{\kappa}{}^0_2$ is also required.

Recall that for local flatness at $r=0$ we noticed that it must be possible to locally write (with $R:=R(r)$):

$$
\begin{aligned}
 \left. \d s^2 \right|_{R\sim 0} &= \d R{}^2+R{}^2 \d\Omega^2,\\
 \Longrightarrow \left.\d s^2\right|_{r\sim0} &=
 \left.\left(\frac{\d R}{\d r} \right)^2\right|_{r=0}
 \left[\d r^2 + r{}^2 \d\Omega^2 \right].
\end{aligned}
$$


or relating this to our initial assumption on $\boldsymbol{\gamma}$ we have (at least analytically) that $\gamma{}_1^0=\gamma{}_2^0$ and similarily $\overline{\kappa}{}_1^0=\overline{\kappa}{}_2^0$.


### (IV):

To impose the additional conditions it is suggested to introduce the auxiliary field $\lambda$.

It can be seen that $\lambda$ is of _odd_ parity. To see this one can write:

$$
\begin{aligned}
  \lambda \sim \frac{1}{r}\left(
    1 - \frac{\gamma{}^0_1 + \gamma{}^2_1 r^2 + \mathcal{O}(r^4)}{\gamma{}^0_1 + \gamma{}^2_2 r^2 + \mathcal{O}(r^4)}
  \right),
\end{aligned}
$$

where notice we have taken $\gamma^0_1=\gamma^0_2$ and peform Taylor expansion in $r$ about $r=0$:

$$
\begin{equation}
  \lambda \sim
  \frac{r}{\gamma{}^0_1}(\gamma{}^2_2-\gamma{}^2_1) + \mathcal{O}(r^3),
\end{equation}
$$

and so this and terms of the form $\lambda / r$ should be safe to evaluate.

Indeed we may rewrite the equation of $\partial{}_t[\overline{\kappa}{}_2]$ and the Hamiltonian constraint immediately in terms of this variable as:

$$
\begin{aligned}
  \partial{}_t[\overline{\kappa}{}_2]
  &=
  -\frac{\alpha}{2\gamma{}_1}
  \Bigg[
    \partial{}_r[\Gamma{}_2]
    +\D_\alpha \Gamma{}_2
    +\Gamma{}_2^2
    -\frac{\Gamma{}_1\Gamma{}_2}{2}
    -\frac{1}{r}(\Gamma{}_1-2\D_\alpha-4\Gamma{}_2)\\
  &+
  \frac{2\lambda}{r}\Bigg]
  +\alpha \overline{\kappa}{}_2(
    \overline{\kappa}{}_1
    + 2 \overline{\kappa}{}_2
  ),
\end{aligned}
$$

and:

$$
\begin{aligned}
  \mathcal{H} &=
  -\partial{}_r[\Gamma{}_2]
  -\frac{\lambda}{r}
  +\gamma{}_1\overline{\kappa}{}_2
  (2\overline{\kappa}{}_1 + \overline{\kappa}{}_2)
  +\frac{1}{r}(\Gamma{}_1-3\Gamma{}_2)
  +\frac{\Gamma{}_1\Gamma{}_2}{2}
  -\frac{3\Gamma{}_2^2}{4}.
\end{aligned}
$$

In order to evolve $\lambda$ itself we can construct a simple expression through direct differentiation and use of the first two ADM evolution equations:

$$
\begin{equation}
  \partial{}_t[\lambda]
  =\frac{2\alpha\gamma{}_1}{\gamma{}_2}
  \left\{\frac{\overline{\kappa}{}_1-\overline{\kappa}{}_2}{r}\right\},
\end{equation}
$$

where the curled brace term may be removed with $\mathcal{M}_r$ to yield:

$$
\begin{equation}
  \partial{}_t[\lambda]
  =
  \frac{2\alpha\gamma{}_1}{\gamma{}_2}
  \left[
  \partial{}_r[\overline{\kappa}{}_2]
  -\frac{\Gamma{}_2}{2}
  (\overline{\kappa}{}_1 - \overline{\kappa}{}_2)
  \right].
\end{equation}
$$

### (V):

Here we just notice that $\partial{}_t[\D_\alpha]=\partial{}_t[\log(\alpha)]=\partial{}_t[\alpha]/\alpha$ and it follows that:

$$
\begin{equation}
  \partial{}_t[\D_\alpha]
  =
  -\partial{}_r[\alpha f(\alpha)(
    \overline{\kappa}{}_1 + 2 \overline{\kappa}{}_2
  )].
\end{equation}
$$

### (VI):

**note**: for a guide to the concept of hyperbolicity see Alcubierre's book $\S5.3$. Important for use here is that the _principal symbol_ of the system of equations has a complete set of eigenvectors (eigenfields), if the eigenvalues are also real and distinct then we have so-called strongly hyperbolic system.


Consider $\boldsymbol{v}:=(\D_\alpha,\,\Gamma{}_1,\,\Gamma{}_2,\,\overline{\kappa}{}_1,\,\overline{\kappa}{}_2)$ then we can investigate the characteristic matrix (principal part of system):

$$
\begin{equation}
M:=
\alpha\begin{bmatrix}
  0 & 0 & 0 & -f(\alpha) & -2 f(\alpha)\\
  0 & 0 & 0 & -2 & 0 \\
  0 & 0 & 0 & 0 & -2 \\
  -1/\gamma{}_1 & 0 & -1/\gamma{}_1 & 0 & 0\\
  0 & 0 & -1/(2\gamma{}_1) & 0 & 0
\end{bmatrix},
\end{equation}
$$

which leads to the collection of eigenvalues:
$$
\begin{equation}
  \boldsymbol{\xi}=
  (\xi^0,\,\xi^l_-,\,\xi^l_+,\,
  \xi^f_-,\,\xi^f_+)
  =
  \left(
    0,\,
    -\frac{\alpha}{\sqrt{\gamma{}_1}},\,
    +\frac{\alpha}{\sqrt{\gamma{}_1}},\,
    -\alpha\sqrt{\frac{f}{\gamma{}_1}},\,
    +\alpha\sqrt{\frac{f}{\gamma{}_1}}
  \right),
\end{equation}
$$

where $\xi^l_\pm$ is the coordinate speed of light whereas $\xi^f_\pm$ are the gauge speeds.

Trouble arises when we look at the eigenfields $\mathbf{w}:=M^{-1}\boldsymbol{v}=(w^0,\,w^l_-,\,w^l_+,\,w^f_-,\,w^f_+)$:

$$
\begin{aligned}
  w_0 &= \frac{\D_\alpha}{f}
  -(\Gamma{}_1+2\Gamma{}_2)/2,\\
  w^l_\pm &=
  \gamma{}_1^{1/2} \overline{\kappa}{}_2
  \mp \Gamma{}_2/2,\\
  w^f_\pm &=
  \gamma{}_1^{1/2}
  \left(
    \overline{\kappa}{}_1
    +2\frac{f+1}{f-1}\overline{\kappa}{}_2
  \right)
  \mp
  \left(
    \frac{\D_\alpha}{f^{1/2}}
    +2\frac{\Gamma{}_2}{f-1}
  \right),
\end{aligned}
$$

where it is clear that as $f\rightarrow 1$ the eigenfields become ill-defined. Thus for a choice of $f=1$ in the gauge our system does not have a (complete) set of eigenfields and can only be weakly-hyperbolic which in turn would mean any numerical evolution would be generally untenable.

### (VII):

See code.

### (VIII):

Under the rescaling:

$$
\begin{aligned}
  \tilde{\gamma}{}_1 &:= \gamma{}_1 / \psi^4, &
  \tilde{\gamma}{}_2 &:= \gamma{}_2 / \psi^4;\\
  \tilde{\Gamma}{}_1 &:= \Gamma{}_1 - 4 \partial{}_r[\log(\psi)],
  &
  \tilde{\Gamma}{}_2 &:= \Gamma{}_2 - 4 \partial{}_r[\log(\psi)];
\end{aligned}
$$

the regularized equations become:

Equations for $\partial{}_t[\gamma{}_I]$ become:
$$
\begin{equation}
  \partial{}_t[\tilde{\gamma}{}_I] =
  - 2\alpha \tilde{\gamma}{}_I \overline{\kappa}{}_I,
\end{equation}
$$

whereas $\partial{}_t[\Gamma{}_I]$ goes to:

$$
\begin{equation}
  \partial{}_t[\tilde{\Gamma}{}_I]
  =-2\alpha
  (
    \overline{\kappa}{}_I\D{}_\alpha
    +\partial{}_r[\overline{\kappa}{}_I]
  ).
\end{equation}
$$

In the case of $\lambda$ and $\partial{}_t[\lambda]$:

$$
\begin{equation}
  \lambda = \frac{1}{r}\left(
    1 - \frac{\tilde{\gamma}{}_1}{\tilde{\gamma}{}_2}
  \right),
\end{equation}
$$

and

$$
\begin{aligned}
  \partial{}_t[\lambda] =
  \frac{2\alpha \tilde{\gamma}{}_1}{\tilde{\gamma}{}_2}
  \left[
    \partial{}_r[\overline{\kappa}{}_2]
    -\left(
      \tilde{\Gamma}{}_2 + 4 \D{}_\psi
    \right)(\overline{\kappa}{}_1-\overline{\kappa}{}_2)/2
  \right],
\end{aligned}
$$

where we have defined $\D{}_\psi:=\partial{}_r[\log(\psi)]$.


Equation for $\partial{}_t[\overline{\kappa}{}_1]$:

$$
\begin{aligned}
\partial{}_t[\overline{\kappa}{}_1]
  &=
  -\frac{\alpha}{\gamma{}_1}
  \Bigg[
    \partial{}_r[\D{}_\alpha+\Gamma{}_2]
    +\D{}_\alpha^2
    -\frac{\D{}_{\alpha} \Gamma{}_1}{2}
    +\frac{\Gamma_2^2}{2}
    -\frac{\Gamma{}_1\Gamma{}_2}{2}\\
  &
  -\gamma{}_1\overline{\kappa}{}_1(
    \overline{\kappa}{}_1+2\overline{\kappa}{}_2
  ) - \frac{1}{r}(\Gamma{}_1-2\Gamma{}_2)
  \Bigg],
\end{aligned}
$$

becomes:

$$
\begin{aligned}
\partial{}_t[\overline{\kappa}{}_1]
  &=
  -\frac{\alpha}{\tilde{\gamma}{}_1\psi^4}
  \Bigg[
    \partial{}_r[\D{}_\alpha+\tilde{\Gamma{}}_2]
    +4\partial{}_r[\D_\psi]
    +\D{}_\alpha^2
    -\frac{\D{}_{\alpha}}{2}(\tilde{\Gamma}{}_1+4\D_\psi)
    +\frac{(\tilde{\Gamma}{}_2+4\D_\psi)^2}{2}\\
  &
  -\frac{(\tilde{\Gamma}{}_1+4\D_\psi)
  (\tilde{\Gamma}{}_2+4\D_\psi)}{2}
   - \frac{1}{r}([\tilde{\Gamma}{}_1+4\D_\psi]
   -2[\tilde{\Gamma}{}_2+4\D_\psi])
  \Bigg]
  +\alpha\overline{\kappa}{}_1(
    \overline{\kappa}{}_1+2\overline{\kappa}{}_2
  ),
\end{aligned}
$$

where we have expanded out a $\propto \gamma{}_1$ term from within the bracket and cancelled.

Equation for $\partial{}_t[\overline{\kappa}{}_2]$:

$$
\begin{aligned}
  \partial{}_t[\overline{\kappa}{}_2]
  &=
  -\frac{\alpha}{2\gamma{}_1}
  \Bigg[
    \partial{}_r[\Gamma{}_2]
    +\D_\alpha \Gamma{}_2
    +\Gamma{}_2^2
    -\frac{\Gamma{}_1\Gamma{}_2}{2}
    -\frac{1}{r}(\Gamma{}_1-2\D_\alpha-4\Gamma{}_2)\\
  &+
  \frac{2\lambda}{r}\Bigg]
  +\alpha \overline{\kappa}{}_2(
    \overline{\kappa}{}_1
    + 2 \overline{\kappa}{}_2
  ).
\end{aligned}
$$

becomes:

$$
\begin{aligned}
  \partial{}_t[\overline{\kappa}{}_2]
  &=
  -\frac{\alpha}{2\tilde{\gamma}{}_1\psi^4}
  \Bigg[
    \partial{}_r[\tilde{\Gamma}{}_2+4\D_\psi]
    +\D_\alpha (\tilde{\Gamma}{}_2+4\D_\psi)
    +(\tilde{\Gamma}{}_2+4\D_\psi)^2
    -\frac{(\tilde{\Gamma}{}_1+4\D_\psi)
    (\tilde{\Gamma}{}_2+4\D_\psi)}{2}\\
  &
  -\frac{1}{r}([\tilde{\Gamma}{}_1+4\D_\psi]
  -2\D_\alpha-4[\tilde{\Gamma}{}_2+4\D_\psi])
  +\frac{2\lambda}{r}\Bigg]
  +\alpha \overline{\kappa}{}_2(
    \overline{\kappa}{}_1
    + 2 \overline{\kappa}{}_2
  ).
\end{aligned}
$$

For the lapse (with Bona-Masso):

$$
\begin{aligned}
  \partial{}_t[\alpha] &=
  -\alpha{}^2 f(\alpha)
  [\overline{\kappa}{}_1 + 2 \overline{\kappa}{}_2], &
  \partial{}_t[\D{}_\alpha] &=
  -\partial{}_r\left[
    \alpha f(\alpha)[\overline{\kappa}{}_1+2\overline{\kappa}{}_2]
  \right];
\end{aligned}
$$

which with $f(\alpha):=2/\alpha$ translates into:

$$
\begin{aligned}
  \partial{}_t[\alpha] &=
  -2\alpha{}
  [\overline{\kappa}{}_1 + 2 \overline{\kappa}{}_2], &
  \partial{}_t[\D{}_\alpha] &=
  -\partial{}_r\left[\overline{\kappa}{}_1+2\overline{\kappa}{}_2
  \right].
\end{aligned}
$$

**Should terms be further regrouped in these expressions?**

For Schwarzschild in our choice of isotropic coordinates we have:

$$
\begin{aligned}
  \D_\psi &= -\frac{M}{r(M+2r)},\\
  \partial{}_r[\D_\psi] &=
  \frac{1}{r^2}-\frac{4}{(M+2r)^2}.
\end{aligned}
$$

Thus, as $r\rightarrow 0$ we have:

$$
\begin{equation}
  \psi^{-4} = \frac{16 r^4}{M^4} + \mathcal{O}(r^5),
\end{equation}
$$

and so poses no issue. On the other hand:

$$
\begin{aligned}
  \D_\psi & =
  -\frac{1}{r} + \frac{2}{M} - \frac{4r}{M^2}
  + \mathcal{O}(r^2),\\
  \partial{}_r[\D_\psi] &=
  \frac{1}{r^2} - \frac{4}{M^2} + \frac{16r}{M^3}
  + \mathcal{O}(r^2).
\end{aligned}
$$

It may therefore be helpful to further group terms of the form:

$$
\begin{equation}
  \psi^{-4}\D_\psi = -\frac{16 r^3}{M} + \mathcal{O}(r^4).
\end{equation}
$$

The $\lambda$ term (its evolution equation in particular) may need to be rescaled also - we have however sufficient powers of $r$ to achieve this too.

**note**: During numerical implementation, one can first start with the adapted lapse:

$$
\begin{equation}
  \alpha = \frac{1-M/(2r)}{1+M/(2r)},
\end{equation}
$$

before investigating non-trivial gauge-dynamics.