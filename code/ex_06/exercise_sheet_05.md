# Providing initial data

In the conformal transverse-traceless approach one considers splitting the
conformal traceless extrinsic curvature $\hat{A}{}^{ij}$ into longitudinal (L) 
and transverse-traceless (TT) parts:

$$
\begin{equation*}
  \hat{A}{}^{ij} := \hat{A}_{\mathrm{L}}{}^{ij}
  + \hat{A}{}^{ij}{}_{\mathrm{TT}}
  = \mathbb{L}_{\tilde{\gamma}}[X]{}^{ij} + \hat{A}_{\mathrm{TT}}{}^{ij},
\end{equation*}
$$
where $\tilde{\gamma}{}_{ij} \hat{A}_{\mathrm{TT}}{}^{ij}{} = 0 =%
\tilde{D}{}_j[\hat{A}_{\mathrm{TT}}{}^{ij}{}]$ and $X{}^k$ is a vector  potential.
We have also introduced the (symmetric and traceless) __conformal Killing operator__:

$$
\begin{equation*}
  \mathbb{L}_{\tilde{\gamma}}[X]{}^{ij}:=
  \tilde{D}{}^i[X{}^j] + \tilde{D}{}^j[X{}^i]
  -\frac{2}{3}\tilde{D}{}_k X{}^k \tilde{\gamma}{}^{ij},
\end{equation*}
$$

and will also make use of the __vector Laplacian__:

$$
\begin{equation*}
  \tilde{D}{}_j[\hat{A}{}^{ij}]
  = \tilde{D}{}_j [\mathbb{L}_{\tilde{\gamma}}[X]{}^{ij}]
  = \tilde{D}{}_j [\tilde{D}{}^j[X{}^i]]
  + \frac{1}{3} \tilde{D}{}^i[\tilde{D}{}_j[X{}^j]]
  + \tilde{R}{}^i_j X{}^j =: \Delta{}_{\tilde{\gamma}}[X{}^i].
\end{equation*}
$$

Under this decomposition the constraints become:

$$
\begin{align}
  \tag{eq:CTTMom}
  \Delta{}_{\tilde{\gamma}}[X{}^i] - \frac{2}{3} \tilde{D}{}^i[K]\Psi{}^6
  -8\pi\tilde{P}{}^i &=0,\\
  \tag{eq:CTTHam}
  \tilde{D}{}_i[\tilde{D}{}^i[\Psi]]
  - \frac{1}{8}\tilde{R}\Psi
  + \frac{1}{8}\hat{A}{}_{ij} \hat{A}{}^{ij} \Psi{}^{-7}
  - \frac{1}{12}K^2 \Psi^5 + 2\pi \tilde{E}\Psi{}^{-3} &= 0;
\end{align}
$$

where $(\tilde{\gamma},\,\hat{A}_{\mathrm{TT}}{}^{ij},\,K,\,E,\,P{}^i)$ may be  freely prescribed and $(\Psi,\,X{}^i)$ are to be solved for.

Our goal here is to solve Eq.(eq:CTTMom) and approximate
a solution to Eq.(eq:CTTHam) from scratch.

  - Consider working in vacuum and assume the maximal slicing condition. Verify the constraints decouple, and that if we further impose conformal flatness while working with Cartesian coordinates the momentum constraint becomes:
$$
\begin{equation}\tag{eq:BowenYorkProto}
    \partial{}^j[\partial{}_j[X{}^i]]
    +\frac{1}{3} \partial{}^i [\partial{}_j X{}^j] = 0.
\end{equation}
$$

- Solutions to Eq.(eq:BowenYorkProto) are known as "Bowen-York" solutions. By further decomposing the vector potential as $X{}_i=Y{}_i+\partial{}_i[Z]$ and making a suitable choice for $Z$ show that Eq.(eq:BowenYorkProto) may be rewritten as the coupled scalar Poisson equations:
$$
\begin{alignat}{2}
     \partial{}^j[\partial{}_j[Z]] &= -\frac{1}{4}\partial{}_j[Y{}^j], \quad
     \partial{}^j[\partial{}_j[Y{}_i]] &= 0.
\end{alignat}
$$

  Impose spherical symmetry and find a simple solution for $Z$, $Y{}_i$ and
   hence $X{}^i$.

- Define the normal vector $n{}^i:=x{}^i/r$ where $r^2=x^2+y^2+z^2$. Verify that another solution to the momentum constraint, assuming conformal flatness is given by:
$$
\begin{equation}\tag{eq:BYrotSoln}
  X{}^i = \tilde{\varepsilon}{}^{ijk}n{}_j J{}_k / r,
\end{equation}
$$
where $J{}^i$ satisfies $\tilde{D}{}_i[J{}_j]=0$ and $\tilde{\varepsilon}{}^{ijk}$ is the Levi-Civita tensor associated with $\tilde{\gamma}{}_{ij}$ such that $\tilde{D}{}_i[\tilde{\varepsilon}{}^{jkl}]=0$. Verify that substitution of Eq.(eq:BYrotSoln) into the conformal Killing operator allows us to write:
$$
\begin{equation}
  \mathbb{L}_{\tilde{\gamma}}[X]{}^{ij} =
  \frac{6}{r^3} n{}^{(i} \tilde{\varepsilon}{}^{j)kl} J{}_k n{}_l =
  \hat{A}_{\mathrm{L}}{}^{ij}.
\end{equation}
$$
- Show that in spherical polar coordinates the non-vanishing components (up to symmetries) of $X{}^i$ and $\hat{A}_{\mathrm{L}}{}^{ij}$ are given by:
$$
\begin{alignat}{2}\tag{eq:BYrotSolnSphPol}
  X{}^\phi &= -\frac{J}{r^3}, \quad
  \hat{A}^{\mathrm{L}}{}_{r\phi} &= \frac{3J}{r^2}\sin{}^2\theta,
\end{alignat}
$$
where $J$ is the magnitude of the vector $J{}^i$ aligned with the polar axis.
- Consider the rotating black hole solution of Eq.(eq:BYrotSolnSphPol) and assume $\hat{A}{}^{ij}{}_{\mathrm{TT}}=0$. This furnishes us a solution for the traceless extrinsic curvature. To complete an initial data specification we also need to provide $\Psi$. Thus, the Hamiltonian constraint must be solved which is non-linear in general and typically requires a numerical approach. Here we construct an approximate expansion.
   Given our $\hat{A}{}^{ij}$ and prior assumptions notice that the only non-vanishing source term in Eq.(eq:CTTHam) arises from:
$$
\begin{equation}
  \hat{A}{}_{ij} \hat{A}{}^{ij} = \frac{18J^2}{r^6} \sin^2\theta.
\end{equation}
$$
Furthermore as $J\rightarrow 0$ the Hamiltonian becomes the Laplace equation and hence, formally, $\Psi\rightarrow1+ \mathcal{M} / (2r)=:{}^{(0)}\Psi$. This suggests we write:
$$
\begin{gather}\tag{eq:PsiApprExpa}
\begin{aligned}
  \Psi &= {}^{(0)}\Psi + \frac{J^2}{\mathcal{M}^4} {}^{(2)}\Psi
  +\mathcal{O}(J^4),\\
  &= 1 + \frac{\mathcal{M}}{2r} + \frac{J^2}{\mathcal{M}^4} {}^{(2)}\Psi
  +\mathcal{O}(J^4).
\end{aligned}
\end{gather}
$$
Show that subtitution of Eq.(eq:PsiApprExpa) into Eq.(eq:CTTHam) leads to:
$$
\begin{equation}\tag{eq:HamCorrection}
  \tilde{D}^2\left[{}^{(2)}\Psi\right] =
  -\frac{9}{4}\frac{\mathcal{M}^4r}{(r+\mathcal{M}/2)^7}\sin^2\theta.
\end{equation}
$$
- To find the first correction offered by Eq.(eq:HamCorrection) split the angular dependence of ${}^{(2)}\Psi$ using the Legendre polynomials:
$$
\begin{alignat}{2}
  P_0(\cos\theta) &= 1, \quad
  P_2(\cos\theta) &= (3\cos^2\theta-1)/2;
\end{alignat}
$$
such that:
$$
\begin{equation}
  {}^{(2)}\Psi(r,\,\theta) = {}^{(2)}\Psi_0(r) P_0(\cos\theta)
  + {}^{(2)}\Psi_2(r) P_2(\cos\theta).
\end{equation}
$$
  
  Show that the resulting equations are solved by:
  $$
  \begin{equation}
   {}^{(2)}\Psi_0(r) =
     -\left(1 + \frac{\mathcal{M}}{2r} \right)^{-5} \frac{\mathcal{M}}{5r}
     \left(
       5\left(\frac{\mathcal{M}}{2r} \right)^3
       + 4\left(\frac{\mathcal{M}}{2r} \right)^4
       + \left(\frac{\mathcal{M}}{2r} \right)^5
     \right),
   \end{equation}
  $$
  
  and
  $$
   \begin{equation}
     {}^{(2)}\Psi_2(r) =
     -\frac{1}{10} \left(1 + \frac{\mathcal{M}}{2r} \right)^{-5}
     \left(\frac{\mathcal{M}}{r}\right)^3.
   \end{equation}
$$
**Remarks**:
The interpretation of the the data $(\hat{A}{}^{ij}, \Psi)$ is that of a rotating black hole. A similar approach can also be used to construct a boosted black hole. A natural question to ask is whether following the Bowen-York solution scheme can lead us to initial data describing a spatial slice of Kerr. Unfortunately this turns out not to be the case (see also Remark $8.2.2$ of the lecture notes).

## (soln)
  - We assume vacuum; maximal slicing; conformal flatness - therefore $(\tilde{P}{}^i,\,\tilde{E};\,K;\,\tilde{R})=0$.
   The constraints Eq.(eq:CTTMom) and Eq.(eq:CTTHam) become:
$$
\begin{align}
  \tag{eq:CTTMomD}
  \Delta{}_{\tilde{\gamma}}[X{}^i]&=0,\\
  \tag{eq:CTTHamD}
  \tilde{D}{}_i[\tilde{D}{}^i[\Psi]] + \frac{1}{8}\hat{A}{}_{ij} \hat{A}{}^{ij} \Psi{}^{-7}&= 0.
\end{align}
$$
 We further have:
 $$
\begin{align*}
     \Delta{}_{\tilde{\gamma}}[X{}^i] =0 &= \tilde{D}{}_j[\hat{A}{}^{ij}] = \tilde{D}{}_j[\mathbb{L}{}_{\tilde{\gamma}}[X]{}^{ij}],\\
     &=\tilde{D}{}_j[\tilde{D}{}^j[X{}^i]] + \frac{1}{3}\tilde{D}{}^i[\tilde{D}{}_j[X{}^j]] + \underbrace{\tilde{R}{}^i_j}_{=0} X{}^j;
\end{align*}
$$
and for Cartesian coordinates we find the momentum constraint reduces to:
$$
\begin{equation*}
  \partial{}^j[\partial{}_j[X{}^i]] + \frac{1}{3}\partial{}^i[\partial{}_j[X{}^j]]=0.
\end{equation*}
$$
- Introduce a 'scalar potential' by setting $X{}^i=Y{}^i + \partial{}^i[Z]$. Substitution into the momentum constraint:
$$
   \begin{equation}
     \partial{}_j\partial{}^jY{}^i + \partial{}_j \partial{}^j \partial{}^i Z
     + \frac{1}{3} \partial{}^i \partial{}_j Y{}^j + \frac{1}{3} \partial{}^i \partial{}_j \partial{}^j Z = 0,
   \end{equation}
$$
notice that if we make the choice $\partial{}_j\partial{}^j Z = -\partial{}_j Y{}^j / 4$ terms cancel:
$$
\begin{equation}
     0=\partial{}_j \partial{}^j Y{}^i
     + \left\{
     \partial{}^i\left[-\frac{1}{4}\partial{}_j Y{}^j \right]
     + \frac{1}{3} \partial{}^i\partial{}_j Y{}^j
     + \frac{1}{3} \partial{}^i\left[-\frac{1}{4}\partial{}_j Y{}^j \right]
     \right\}_{=0},
   \end{equation}
$$
and we find the coupled system:
$$
\begin{equation}
   \begin{cases}
    &\partial{}_j \partial{}^j Z = -\frac{1}{4} \partial{}_j Y{}^j,\\
    &\partial{}_j \partial{}^j Y{}^i =0.
   \end{cases}
\end{equation}
$$
Suppose we make the choice $Y{}_i=0$ then we only need to consider the Laplace equation $\partial{}^j\partial{}_j[Z]=0$. It is well-known that __harmonic functions__ satisfy this equation. One possible (spherically symmetric) solution (selected by choice of boundary conditions) is given by:
$$
\begin{equation*}
  Z = a + \frac{b}{r}.
\end{equation*}
$$
Note that:
$$
\begin{equation*}
  \partial{}_i[r] = \partial{}_i\left[(x^2+y^2+z^2)^{1/2}\right] = \frac{x{}_i}{r},\quad
  \partial{}_i[r^{-1}] = -\frac{x{}_i}{r^3}.
\end{equation*}
$$
It follows that $X{}_i = Y{}_i + \partial{}_i[Z] = -x{}_i/r^3$.

- Recall:
$$
\begin{equation}
  X{}^i = \tilde{\varepsilon}{}^{ijk}n{}_j J{}_k / r^2.
\end{equation}
$$
If we assume conformal flatness and adopt Cartesian coordinates then the momentum constraint reduces to the form of Part I. Consider:
$$
\begin{align}
     \partial{}_m\partial{}_j[n{}_k/r^2] &= \partial{}_m[\partial{}_j[x{}_k/r^3]],\\
     &= \partial{}_m \left[
       x{}_k \partial{}_j\left[\frac{1}{r^3}\right]
       +\frac{1}{r^3}\partial{}_j[x{}_k]
     \right],\\
     &= \partial{}_m\left[
     -\frac{3}{r^5}x{}_k x{}_j + \frac{1}{r^3}\delta{}_{jk}
     \right],\\
     &= -\frac{3}{r{}^5} \partial{}_m[x{}_k x{}_j]
     -3x{}_k x{}_j \partial{}_m\left[\frac{1}{r^5}\right]
     +\delta{}_{jk}\partial{}_m\left[\frac{1}{r^3}\right],\\
    &= -\frac{3}{r^5}\left(
    \delta{}_{mk}x{}_j + x{}_k \delta{}_{mj}
    \right)
    +\frac{15}{r^7} x{}_m x{}_k x{}_j
    -\frac{3}{r^5} \delta{}_{jk} x{}_m.
\end{align}
$$
Further, notice that (by assumption):
$$
\begin{equation}
  \partial{}_m\left[\varepsilon{}^{jkl}n{}_k J{}_l f(r) \right] =
  \varepsilon{}^{jkl} J{}_l \partial{}_m \left[n{}_k f(r)\right];
\end{equation}
$$
Thus:
$$
\begin{align}
   \delta{}^{jm}\partial{}_m [n{}_k/r^2] &=
   -\frac{3}{r^5} \left(x{}_k + 3x{}_k\right) + 15 \underbrace{x{}_m x{}^m x{}_k / r^7}_{x{}_m x{}^m=r^2}
   -\frac{3}{r^5}x{}_k,\\
   &=
   -\frac{12}{r^5}x{}_k +\frac{15}{r^5} x{}_k -\frac{3}{r^5} x{}_k=0.
\end{align}
$$
Similarly:
$$
\begin{align}
  \varepsilon{}^{jkl} \partial{}_m \partial{}_j [n{}_k/r^2]
  &=
  -\frac{3}{r^5} \left(\delta{}_{mk} x{}_j + x{}_k \delta{}_{mj}\right)\varepsilon{}^{jkl}
  +\underbrace{0 + 0}_{\mbox{sym/antisym contr.}},\\
  &=0;
\end{align}
$$
where the last line follows by relabelling dummy indices antisymmetry of $\varepsilon{}^{jkl}$ once more.
In a similar fashion we verify the conformal Killing operator satisfies:
$$
\begin{equation*}
  \mathbb{L}_{\tilde{\gamma}}[X]{}^{ij} =
  \frac{6}{r^3} n{}^{(i} \tilde{\varepsilon}{}^{j)kl}J{}_k n{}_l;
\end{equation*}
$$
Substituting:
$$
\begin{align*}
     \Longrightarrow&\partial{}^i[\varepsilon{}^{jkl}n{}_k J{}_l /r^2]
     + \partial{}^j[\varepsilon{}^{ikl}n{}_k J{}_l /r^2]
     -\frac{2}{3} \partial{}_k [\varepsilon{}^{kmn}n{}_m J{}_n /r^2]\delta{}^{ij},\\
     =& \varepsilon{}^{jkl} J{}_l \partial{}^i[n{}_k/r^2] + \varepsilon{}^{ikl}J{}_l
     \partial{}^j[n_k/r^2]
     -\frac{2}{3}\varepsilon{}^{kmn}J{}_n \delta{}^{ij} \partial{}_k[n{}_m/r^2]=(\star).
\end{align*}
$$
Note that:
$$
\begin{align}
     \partial{}^i[n{}_k/r^2] &=
     \partial{}^i[x{}_k/r^3] = \partial{}^i[x{}_k]/r^3 + x{}_k \partial{}^i[1/r^3],\\
     &=\delta{}^i_k/r^3 - 3x{}_k x{}^i/r^5,\\
     &=\delta{}^i_k/r^3 - 3n{}_k n{}^i /r^3,\\
     &=\frac{1}{r^3}\left(\delta{}^i_k -3n{}_k n{}^i \right);
\end{align}
$$
Thus:
$$
\begin{align}
     \Longrightarrow (\star) =& \varepsilon{}^{jkl} J{}_l\left(
     \delta{}^i_k - 3n{}_k n{}^i
     \right)/r^3
     +\varepsilon{}^{ikl} J{}_l \left(\delta{}^j_k - 3n{}_k n{}^j \right)/r^3
     -\frac{2}{3}\varepsilon{}^{kmn} J{}_n \delta{}^{ij}
     (
       \underbrace{\delta{}_{km}}_{=0} - \underbrace{3n{}_k n{}_m}_{=0}
     )/r^3,
\end{align}
$$
where the last brace follows from $\varepsilon$ antisymmetry, then:
$$
\begin{align}
     (\star) =&
     \frac{1}{r^3} J{}_l\left(
     \underbrace{\left[ 
     \varepsilon{}^{jkl} \delta{}^i_k +\varepsilon{}^{ikl}\delta{}^j_k
     \right]}_{=0}
     -3n{}_k \underbrace{(\varepsilon{}^{jkl}n{}^i + \varepsilon{}^{ikl}n{}^j)}_{=2n{}^{(i}\varepsilon{}^{j)kl}}
     \right),\\
     =& 6 n{}^{(i}\varepsilon{}^{j)kl} J{}_k n{}_l/r^3.
   \end{align}
$$
- One (mechanical) way to compute this result is to transform Eq.(5) and Eq.(6) to spherical problems...
- A an aside/preliminary we compute the (Laplace-Beltrami) operator in spherical coordinates; note that:
$$
\begin{equation*}
     \tilde{\gamma}{}_{ij} = \mathrm{diag}(1,\,r^2,\,r^2\sin^2\theta),\quad \sqrt{\tilde{\gamma}} = r^2\sin\theta.
\end{equation*}
$$
We have:
$$
\begin{align}
     \Delta{}_{\tilde{\gamma}}[\Psi]
     &= \frac{1}{\sqrt{\tilde{\gamma}}} \tilde{\partial}{}_i[\sqrt{\tilde{\gamma}} \tilde{\gamma}^{ij}\tilde{\partial}{}_j \Psi],\\
     &=\frac{1}{\sqrt{\tilde{\gamma}}}\left[
     \left(\tilde{\partial}{}_i \sqrt{\tilde{\gamma}}\right)\tilde{\gamma}{}^{ij} \tilde{\partial}_j\Psi
     + \sqrt{\tilde{\gamma}} \tilde{\partial}{}_i \left[
     \tilde{\gamma}{}^{ij} \tilde{\partial}{}_j\Psi
     \right]
     \right],
\end{align}
$$
Considering terms in parts:
$$
\begin{align*}
  \tilde{\partial}{}_i[\sqrt{\tilde{\gamma}}] \tilde{\gamma}{}^{ij} \tilde{\partial}{}_j \Psi
  &=
  \tilde{\partial}_r[\sqrt{\tilde{\gamma}}] \tilde{\gamma}{}^{rj} \tilde{\partial}_j \Psi\\
  &+\tilde{\partial}_\theta[\sqrt{\tilde{\gamma}}] \tilde{\gamma}{}^{\theta j} \tilde{\partial}_j \Psi\\
  &+\tilde{\partial}_\phi[\sqrt{\tilde{\gamma}}] \tilde{\gamma}{}^{\phi j} \tilde{\partial}_j \Psi,\\
  &= 2r\sin\theta\,\tilde{\gamma}{}^{rr} \tilde{\partial}{}_r\Psi 
  +r^2 \cos\theta\,\tilde{\gamma}{}^{\theta\theta} \tilde{\partial}_\theta\Psi,\\
  &= 2r\sin\theta\,\tilde{\partial}{}_r \Psi + \cos\theta\,\tilde{\partial}{}_{\theta}\Psi;
\end{align*}
$$
where off-diagonal inverse metric terms are zero.
$$
\begin{align*}
  \tilde{\partial}{}_i\left[
  \tilde{\gamma}{}^{ij} \tilde{\partial}{}_j\Psi
  \right] = \tilde{\partial}{}^2_r \Psi + \frac{1}{r^2} \tilde{\partial}{}^2_r \Psi
  + \frac{1}{r^2\sin^2\theta} \tilde{\partial}^2_\phi \Psi,
\end{align*}
$$
which may be combined to give the usual expression:
$$
\begin{equation}
  \Delta{}_{\tilde{\gamma}}[\Psi] =
  \frac{1}{r^2}\tilde{\partial}_r \left[
  r^2 \tilde{\partial}{}_r\Psi
  \right]
  + \frac{1}{r^2\sin\theta}\tilde{\partial}_\theta
  \left[
  \sin\theta\,\tilde{\partial}_\theta\Psi
  \right]
  +\frac{1}{r^2\sin^2\theta} \tilde{\partial}^2_\phi \Psi.
\end{equation}
$$
Additionally it is worthwhile noticing that:
$$
\begin{equation}
  \Delta{}_{\tilde{\gamma}}[\Psi] = \frac{1}{r^2}\tilde{\partial}_r[r^2\tilde{\partial}_r[\Psi]]
  +\frac{1}{r^2}\Delta{}_{\mathbb{S}^2}[\Psi].
\end{equation}
$$
For the question we can however do things without this expression directly:
$$
\begin{equation*}
  \Psi = 1 + \frac{\mathcal{M}}{2r} + \frac{J^2}{\mathcal{M}} {}^{(2)}\Psi + \mathcal{O}(J^4),
\end{equation*}
$$
and solve for ${}^{(2)}\Psi$ using:
$$
\begin{equation*}
  \Delta{}_{\tilde{\gamma}} [\Psi] = - \frac{1}{8} \hat{A}{}_{ij}\hat{A}{}^{ij} \Psi^{-7},
\end{equation*}
$$
where it follows:
 $$
 \begin{align*}
 \Delta{}_{\tilde{\gamma}} [\Psi] &= \Delta{}_{\tilde{\gamma}} \left[
 {}^{(0)}\Psi + \frac{J^2}{\mathcal{M}} {}^{(2)}\Psi + \mathcal{O}(J^4)
 \right],\\
 &=\underbrace{\Delta{}_{\tilde{\gamma}}[{}^{(0)}\Psi]}_{=0}
 +\frac{J^2}{\mathcal{M}^4}\Delta{}_{\tilde{\gamma}}[{}^{(2)}\Psi] + \mathcal{O}(J^4),
\end{align*}
$$
and if we match powers of $J$ then:
$$
\begin{equation*}
  \Delta{}_{\tilde{\gamma}}[{}^{(2)}\Psi] =
  \mathcal{I}(r) \sin^2\theta,
\end{equation*}
$$
where:
$$
\begin{equation*}
  \mathcal{I}(r):=-\frac{9}{4} \frac{\mathcal{M}^4 r}{(r+\mathcal{M}/2)^7}
\end{equation*}
$$
- For this final part we need to construct / verify the correction. To assist in this notice that we can decompose:
$$
\begin{equation}
  \sin^2\theta = 2 (P_0(\cos\theta) - P_2(\cos\theta))/3,
\end{equation}
$$
Furthermore the Legendre polynomials form the $\theta$ part of the spherical harmonics and we recall the eigenfunction property:
$$
\begin{equation}
  \Delta{}_{\mathbb{S}^2}[P_l(\cos\theta)] = -l(l+1) P_l(\cos\theta).
\end{equation}
$$
It follows that:
$$
\begin{equation}
  \Delta_{\tilde{\gamma}}[f(r) P_l(\cos\theta)] = \left(
  \frac{1}{r^2}\tilde{\partial}_r[r^2 \tilde{\partial}_r[f(r)]]
  -\frac{l(l+1)}{r^2} f(r)
  \right) P_l(\cos\theta)
\end{equation}
$$
which implies that the relations to check / solve are:
$$
\begin{equation}
  \frac{1}{r^2}\tilde{\partial}_r[r^2 \tilde{\partial}_r[{}^{(2)}\Psi_l(r)]]
  -\frac{l(l+1)}{r^2} {}^{(2)}\Psi_l(r)
  = \frac{2}{3} \mathcal{I}(r)
  \times
  \begin{cases}
  1 & l=0,\\
  -1 & l=2
  \end{cases}.
\end{equation}
$$
There is a reference that may be of interest here (concerned with approximate evolution) 'arXiv:gr-qc/9710096'.
One way to verify (`Mathematica`):
![[_img/2020_07_02_tutorial/20200702-140229.png|500]]

**Note**: With regard to the remark on the exercise sheet "Nonexistence of conformally flat slices of the Kerr spacetime" by Garat & Price may be of interest; see also the paper of Kroon 'arxiv:gr-qc/0310048'