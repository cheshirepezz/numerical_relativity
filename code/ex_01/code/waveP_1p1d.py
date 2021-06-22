#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Mon Apr 19 2021>

@author: Boris Daszuta
@function:
Some potentially useful functions for solution of the Wave equation in 1+1d.
"""
import numpy as np
import functools as ft
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------

def gr_P(N, nghost=0):
  # make a periodic grid, optionally extend by a number of ghosts
  a, b = 0, 2 * np.pi
  dx = (b - a) / N
  Num_wg = (N + 1 + 2 * nghost)
  ix_i = (np.arange(0, Num_wg) - nghost)
  return ix_i * dx

def extend_to_ghosts(fcn, nghost=0):
  # given function data sampled on [0, 2pi] periodically extend to ghosts zones
  if nghost == 0:
    return fcn

  sz = fcn.size
  ext_fcn = np.zeros(sz + 2 * nghost)
  ext_fcn[nghost:-nghost] = fcn[:]
  ext_fcn[:nghost] = fcn[-(nghost + 1):-1]
  ext_fcn[-nghost:] = fcn[1:(nghost + 1)]

  return ext_fcn

def trim_ghosts(ext_fcn, nghost=0):
  # given extended function data trim to physical nodes
  if nghost == 0:
    return ext_fcn

  return ext_fcn[nghost:-nghost]

def D2(ext_fcn, nghost=1):
  # compute second derivative
  N = ext_fcn.size - 2 * nghost - 1 # identify based on number of ghosts
  a, b = 0, 2 * np.pi
  dx = (b - a) / N

  out_fcn = np.zeros_like(ext_fcn)

  if nghost == 1:
    fcn_im1 = ext_fcn[nghost-1:-(nghost+1)]
    fcn_i = ext_fcn[nghost:-nghost]
    fcn_ip1 = ext_fcn[nghost+1:]
    out_fcn[nghost:-nghost] = (fcn_im1 - 2 * fcn_i + fcn_ip1) / dx ** 2

  # # or equivalently something like:
  # for i in range(nghost, N+1+nghost):
  #   out[i] = (ext_fcn[i-1] - 2 * ext_fcn[i] + ext_fcn[i+1]) / dx ** 2

  elif nghost == 2:
    fcn_im2 = ext_fcn[nghost-2:-(nghost+2)]
    fcn_im1 = ext_fcn[nghost-1:-(nghost+1)]
    fcn_i = ext_fcn[nghost:-nghost]
    fcn_ip1 = ext_fcn[nghost+1:-1]
    fcn_ip2 = ext_fcn[nghost+2:]

    out_fcn[nghost:-nghost] = (
      -1/12 * (fcn_im2 + fcn_ip2)
      + 4/3 * (fcn_im1 + fcn_ip1) - 5/2 * fcn_i) / dx ** 2

  return out_fcn

def ev_step_midpoint(t, u, dt, sys_fcn=None):
  # perform a time-step using mid-point method
  if sys_fcn is None:
    raise ValueError('sys_fcn must be provided!')

  # prepare stages
  v_1 = sys_fcn(t, u)
  v_2 = sys_fcn(t + dt / 2, u + 1 / 2 * dt * v_1)

  # collect
  return u + dt * v_2

def ev_step_RK4(t, u, dt, sys_fcn=None):
  # perform a time-step using Runge-Kutta 4 method
  if sys_fcn is None:
    raise ValueError('sys_fcn must be provided!')

  # prepare stages
  v_1 = sys_fcn(t, u)
  v_2 = sys_fcn(t + dt / 2, u + 1 / 2 * dt * v_1)
  v_3 = sys_fcn(t + dt / 2, u + 1 / 2 * dt * v_2)
  v_4 = sys_fcn(t + dt, u + dt * v_3)

  # collect
  return u + dt * (v_1 / 6 + v_2 / 3 + v_3 / 3 + v_4 / 6)

def example_system(t, u):
  # Testing 2x2 system:
  #
  # u_0'[t] = -u_1[t] + t, u_1'[t] = u_0[t]
  #
  rhs = np.zeros_like(u)
  rhs[0] = -u[1] + t
  rhs[1] = u[0]
  return rhs

# -----------------------------------------------------------------------------

# functions of 1.

def fcn_A(m, x):
  return np.sin(m * x)

def fcn_B(x):
  return np.sqrt(x)

def fcn_C(x):
  return np.exp(-np.sin(x))

# their derivatives

def D2_fcn_A(m, x):
  return -(m ** 2) * np.sin(m * x)

def D2_fcn_B(x):
  return -1 / (4 * x ** (3 / 2))

def D2_fcn_C(x):
  return np.exp(-np.sin(x)) * (np.cos(x) ** 2 + np.sin(x))

# inspect errors of functions
def c_err(N, nghost=1):
  x_ng = gr_P(N)

  nf_A = extend_to_ghosts(fcn_A(1, x_ng), nghost=nghost)
  nf_B = extend_to_ghosts(fcn_B(x_ng), nghost=nghost)
  nf_C = extend_to_ghosts(fcn_C(x_ng), nghost=nghost)

  nD2f_A = D2(nf_A, nghost=nghost)
  nD2f_B = D2(nf_B, nghost=nghost)
  nD2f_C = D2(nf_C, nghost=nghost)

  aD2f_A = extend_to_ghosts(D2_fcn_A(1, x_ng), nghost=nghost)
  aD2f_B = extend_to_ghosts(D2_fcn_B(x_ng), nghost=nghost)
  aD2f_C = extend_to_ghosts(D2_fcn_C(x_ng), nghost=nghost)

  dx = x_ng[1] - x_ng[0]
  err_max_abs = lambda A, B: np.max(np.abs((A - B)[nghost:-nghost]))
  err_L2 = lambda A, B, dx: dx * np.sqrt(np.sum(((A-B)[nghost:-nghost]) ** 2))

  e_MA_A = err_max_abs(nD2f_A, aD2f_A)
  e_L2_A = err_L2(nD2f_A, aD2f_A, dx)

  e_MA_B = err_max_abs(nD2f_B, aD2f_B)
  e_L2_B = err_L2(nD2f_B, aD2f_B, dx)

  e_MA_C = err_max_abs(nD2f_C, aD2f_C)
  e_L2_C = err_L2(nD2f_C, aD2f_C, dx)

  return (e_MA_A, e_MA_B, e_MA_C), (e_L2_A, e_L2_B, e_L2_C)

# -----------------------------------------------------------------------------

# utility functions

def N_t_from_CFL(CFL, dx, ti, tf, v=1):
  return int(np.ceil(v * ((tf - ti) / CFL) / dx))

def CFL_from_N_t(N_t, dx, ti, tf, v=1):
  return v * (tf - ti) / (dx * N_t)

def wave_state2fields(u, N, nghost=1):
  # u -> (phi_i, pi_i)

  phi_i = u[:((N+1)+2*nghost), 0]
  pi_i = u[((N+1)+2*nghost):, 0]
  return phi_i, pi_i

def wave_fields2state(field_1, field_2):
  # flat (field_1, field_2) -> stacked column u
  return np.vstack((field_1[:, None], field_2[:, None]))

def wave_state2fields_physical(u, N, nghost=1):
  # extract physical (non-ghost) nodes from stacked state-vector
  phi_i, pi_i = wave_state2fields(u, N, nghost=nghost)
  return phi_i[nghost:-nghost], pi_i[nghost:-nghost]

# implementation of wave equation system

def wave_system(t, u, N=16, nghost=1):
  # MOL wave equation
  #
  # state vector is stacked as:
  # u = [phi_i; pi_i]
  #
  # Note:
  # phi_i.size = (N + 1) + 2 * nghost

  # extract fields and compute derivative
  phi_i, pi_i = wave_state2fields(u, N, nghost=nghost)

  # compute derivative on extended grid, clip, recycle extension function
  D2_phi_i = D2(phi_i, nghost=nghost)[nghost:-nghost]
  ext_D2_phi_i = extend_to_ghosts(D2_phi_i, nghost=nghost)

  # assemble state-vec and return
  return wave_fields2state(pi_i, ext_D2_phi_i)


# -----------------------------------------------------------------------------


# rename to __main__ to run relevant portion
if __name__ == '__main__provided':

  # Examples on a fixed grid --------------------------------------------------
  N = 16
  nghost = 1

  # grid with no ghosts (notice this is the default)
  x_ng = gr_P(N)

  # grid with ghosts
  x_wg = gr_P(N, nghost=nghost)

  # evaluate a function and periodically extend it to ghost zones -------------
  fcn = np.cos(x_ng) + 2
  ext_fcn = extend_to_ghosts(fcn, nghost=nghost)

  # compute derivative of the function based on exercise sheet ----------------
  ddfcn = -np.cos(x_ng)
  num_ddfcn = D2(ext_fcn, nghost=nghost)

  # example of using the mid-point integrator ---------------------------------
  # For u_0'[t] = -u_1[t] + t, u_1'[t] = u_0[t]
  # Subject to: u_0(0) = 1/2 and u_1(0) = 0
  #
  # Solution
  # u_0(t) = (-cos(t) + 2 cos(t)^2 + 2 sin(t)^2) / 2
  # u_1(t) = (2 t cos(t)^2 - sin(t) + 2 t sin(t) ^ 2) / 2

  # pick temporal range and sampling
  t_i, t_f, N_t = 0, 10, 100
  # pick initial condition
  u_ini = np.array([[1/2], [0]])
  # prepare storage space for (full) output
  num_u_sol = np.zeros((2, N_t + 1))
  num_u_sol[:, 0] = u_ini[:, 0]

  t = t_i
  for ix_t in range(1, N_t + 1):
    dt = (t_f - t_i) / N_t
    num_u_sol[:, ix_t] = ev_step_midpoint(t, num_u_sol[:, ix_t-1], dt,
                                          sys_fcn=example_system)
    t += dt

  # prepare also analytical solution for comparison
  t = np.linspace(t_i, t_f, num=N_t + 1)

  C_t, S_t = np.cos(t), np.sin(t)

  u_sol = np.vstack(
    ((-C_t + 2 * C_t ** 2 + 2 * S_t ** 2) / 2,
     (2 * t * C_t ** 2 - S_t + 2 * t * S_t ** 2) / 2)
  )
  # ---------------------------------------------------------------------------


  # plotting ------------------------------------------------------------------
  plt.figure(1)
  plt.plot(x_wg, ext_fcn, '-sg', markersize=5)
  plt.plot(x_ng, fcn, '-or', markersize=2.8)

  plt.xlabel('x')
  plt.ylabel("fcn(x)")

  plt.figure(2)
  plt.plot(x_wg, num_ddfcn, '-sg', markersize=5, label='approximated')
  plt.plot(x_ng, ddfcn, '-or', markersize=2.8, label='analytical')
  plt.xlabel('x')
  plt.ylabel('d^2/dx^2[fcn(x)]')
  plt.legend()

  plt.figure(3)
  plt.plot(t, num_u_sol[0, :], '-sg', markersize=5, label='approximated')
  plt.plot(t, u_sol[0, :], '-or', markersize=2.8, label='analytical')
  plt.xlabel('t')
  plt.ylabel('u_0(t)')
  plt.legend()

  plt.show()

if __name__ == '__main__':

  N = 64
  nghost = 1

  # grid with no ghosts (notice this is the default)
  x_ng = gr_P(N)

  # grid with ghosts
  x_wg = gr_P(N, nghost=nghost)

  # examine the (extended) functions
  nf_A = extend_to_ghosts(fcn_A(1, x_ng), nghost=nghost)
  nf_B = extend_to_ghosts(fcn_B(x_ng), nghost=nghost)
  nf_C = extend_to_ghosts(fcn_C(x_ng), nghost=nghost)

  # build numerical derivatives
  nD2f_A = D2(nf_A, nghost=nghost)
  nD2f_B = D2(nf_B, nghost=nghost)
  nD2f_C = D2(nf_C, nghost=nghost)

  # analytical
  aD2f_A = extend_to_ghosts(D2_fcn_A(1, x_ng), nghost=nghost)
  aD2f_B = extend_to_ghosts(D2_fcn_B(x_ng), nghost=nghost)
  aD2f_C = extend_to_ghosts(D2_fcn_C(x_ng), nghost=nghost)

  # inspect
  plt.plot(x_ng, nD2f_A[nghost:-nghost], '-g', label='D^2_x[sin(x)]')
  plt.plot(x_ng, nD2f_B[nghost:-nghost], '-b', label='D^2_x[sqrt(x)]')
  plt.plot(x_ng, nD2f_C[nghost:-nghost], '-r', label='D^2_x[exp(-sin(x))]')

  plt.plot(x_ng, aD2f_A[nghost:-nghost], '--g', label='-sin(x)')
  plt.plot(x_ng, aD2f_B[nghost:-nghost], '--b', label='-1 / (4 * x ^ (3 / 2))')
  plt.plot(x_ng, aD2f_C[nghost:-nghost], '--r', label='exp(-sin(x)) * (cos(x) ^ 2 + sin(x))')

  plt.ylim([-4, 4])
  plt.xlabel('x')
  plt.ylabel('s_m(x), f(x), g(x)')
  plt.legend()
  plt.show()

  # fcn = fcn_A(1, x_wg)
  # D2_fcn = D2_fcn_A(1, x_wg)

  # nD2_fcn = D2(fcn, nghost=nghost)

  # # compare over physical grid
  # err = (D2_fcn - nD2_fcn)[nghost:-nghost]
  # mae = np.max(np.abs(err))


if __name__ == '__main__1c':

  nghost = 2
  N = 5  # starting value
  p_num = 10
  N_ran = N * 2 ** np.arange(p_num)

  err_vec = np.zeros((2, N_ran.size), dtype=np.float64)

  for i in range(p_num):
    e_MA, e_L2 = c_err(N_ran[i], nghost)
    err_vec[0, i] = e_MA[0]
    err_vec[1, i] = e_MA[2]

  plt.loglog(N_ran, err_vec[0], '-g', label='max|err(sin(x))|')
  plt.loglog(N_ran, err_vec[1], '-r', label='max|err(exp(-sin(x)))|')

  plt.loglog(N_ran, 1 / N_ran ** (2 * nghost), '--k', label='1 / N^({fac}) trend'.format(
    fac=2 * nghost
  ))

  plt.xlabel('N')
  plt.ylabel('max_i|err_i|')
  plt.legend()
  plt.show()


if __name__ == '__main__2':

  # Solution on fixed grid ----------------------------------------------------
  N_x = 64
  N_t = 200
  ti, tf = 0, 1

  nghost = 2

  # grid with no ghosts (notice this is the default)
  x_ng = gr_P(N_x)

  # grid with ghosts
  x_wg = gr_P(N_x, nghost=nghost)

  # prepare initial conditions and assemble initial state vector
  # these are immediately on the extended grid
  m = 1

  phi_0 = -np.sin(m * x_wg)
  pi_0 = m * np.cos(m * x_wg)

  u_0 = np.vstack((phi_0[:, None], pi_0[:, None]))

  # buffer for current time-step
  u_c = u_0.copy()

  # RK4 -----------------------------------------------------------------------
  sys_fcn = ft.partial(wave_system, N=N_x, nghost=nghost)

  dt = (tf - ti) / N_t
  t = ti

  for t_idx in range(int(N_t)):
    u_c = ev_step_RK4(t, u_c, dt, sys_fcn=sys_fcn)
    t = t + dt
  # ---------------------------------------------------------------------------

  # reference solution
  ext_phi_t = np.sin(m * (t - x_wg))
  ext_pi_t = np.cos(m * (t - x_wg))

  u_t = np.vstack((ext_phi_t[:, None], ext_pi_t[:, None]))

  # extract numerical and analytical (physical node) components
  phi_c, pi_c = wave_state2fields_physical(u_c, N_x, nghost=nghost)
  phi_t, pi_t = wave_state2fields_physical(u_t, N_x, nghost=nghost)

  # examine directly the difference for this choice
  plt.plot(x_ng, phi_c-phi_t, '-r', label='phi_c - phi_t @ t={t}'.format(t=tf))
  plt.plot(x_ng, pi_c-pi_t, '-g', label='pi_c - pi_t @ t={t}'.format(t=tf))
  plt.xlabel('x_ng')
  plt.ylabel('|an-num|')
  plt.legend()
  plt.show()

if __name__ == '__main__4':

  # N_x = 32
  # N_t = 40

  N_x = 64
  N_t = 80

  ti, tf = 0, 10

  nghost = 2

  # grid with no ghosts (notice this is the default)
  x_ng = gr_P(N_x)

  # grid with ghosts
  x_wg = gr_P(N_x, nghost=nghost)

  # prepare initial conditions and assemble initial state vector
  # these are immediately on the extended grid
  m = 1

  phi_0 = -np.sin(m * x_wg)
  pi_0 = m * np.cos(m * x_wg)

  u_0 = np.vstack((phi_0[:, None], pi_0[:, None]))

  # convergence in time -------------------------------------------------------
  p_num = 10
  N_t_ran = N_t * 2 ** np.arange(p_num)

  err_vec = np.zeros_like(N_t_ran, dtype=np.float64)

  for i in range(p_num):
    N_t_cur = N_t_ran[i]

    # buffer for current time-step
    u_c = u_0.copy()

    # RK4 -----------------------------------------------------------------------
    sys_fcn = ft.partial(wave_system, N=N_x, nghost=nghost)

    dt = (tf - ti) / N_t_cur
    t = ti

    for t_idx in range(int(N_t_cur)):
      u_c = ev_step_RK4(t, u_c, dt, sys_fcn=sys_fcn)
      t = t + dt
    # ---------------------------------------------------------------------------

    # reference solution
    ext_phi_t = np.sin(m * (t - x_wg))
    ext_pi_t = np.cos(m * (t - x_wg))

    u_t = np.vstack((ext_phi_t[:, None], ext_pi_t[:, None]))

    # extract numerical and analytical (physical node) components
    phi_c, pi_c = wave_state2fields_physical(u_c, N_x, nghost=nghost)
    phi_t, pi_t = wave_state2fields_physical(u_t, N_x, nghost=nghost)

    err_vec[i] = np.sum((phi_c - phi_t) ** 2) / phi_c.size


  plt.loglog(N_t_ran, err_vec, '-r', label='max|err|')
  plt.loglog(N_t_ran, 1 / N_t_ran ** (4), '--b', label='1 / N^4 trend')

  plt.xlabel('N')
  plt.ylabel('max_i|err_i|')
  plt.legend()
  plt.show()


#
# :D
#
