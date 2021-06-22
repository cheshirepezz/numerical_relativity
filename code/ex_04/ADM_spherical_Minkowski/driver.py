#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Driver script to control calculation.
"""
import functools as ft
import numpy as np
import matplotlib.pyplot as plt

import grids as gr
import operators as op
import field_conditions as fc
import integrators as it
import ADM_spherical as ADMs
import ADM_auxiliaries as ADMa


# -----------------------------------------------------------------------------
# specify system to evolve
def ADM_system(t, u, r=None, nghost=1):
  # unpack state vector [6 x r.size]
  alpha, beta_r, gam_1, gam_2, kap_1, kap_2 = u

  # prepare gauge
  dt_alpha, dt_beta_r = ADMs.ADM_sph_geodesic(t, r, nghost=nghost)

  # # impose parity conditions
  # fc.BC_parity(dt_alpha, is_even=True, left_side=True, nghost=nghost)
  # fc.BC_parity(dt_beta_r, is_even=False, left_side=True, nghost=nghost)

  # eval. system
  dt_gam_1, dt_gam_2, dt_kap_1, dt_kap_2 = ADMs.ADM_sph_sys(
    dt_alpha, dt_beta_r,
    gam_1, gam_2, kap_1, kap_2, r, nghost=nghost)

  # impose parity conditions on field components
  fc.BC_parity(dt_gam_1, is_even=True, left_side=True, nghost=nghost)
  fc.BC_parity(dt_gam_2, is_even=True, left_side=True, nghost=nghost)
  fc.BC_parity(dt_kap_1, is_even=True, left_side=True, nghost=nghost)
  fc.BC_parity(dt_kap_2, is_even=True, left_side=True, nghost=nghost)

  # impose extrapolation (outflow) conditions
  fc.BC_outflow(dt_gam_1, nghost=nghost, order=1)
  fc.BC_outflow(dt_gam_2, nghost=nghost, order=1)
  fc.BC_outflow(dt_kap_1, nghost=nghost, order=1)
  fc.BC_outflow(dt_kap_2, nghost=nghost, order=1)

  # return updated state vector
  res = (0 * dt_alpha, 0 * dt_beta_r, dt_gam_1, dt_gam_2, dt_kap_1, dt_kap_2)

  return np.vstack(res)

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# calculation parameters
nghost = 2
N_r = 100
r_a, r_b = 0, 200
t_i, t_f = 0, 10
CFL = 0.5

# prepare grid
r = gr.gr_CC(N_r, a=r_a, b=r_b, nghost=nghost)
# number of time-steps
N_t = it.N_t_from_CFL(CFL, r[1]-r[0], t_i, t_f, v=1)

# prepare Minkowkian initial data with geodesic gauge
ini_gam_1, ini_gam_2, ini_kap_1, ini_kap_2 = ADMa.ADM_sph_ini_Minkowski(r)
ini_alpha, ini_beta_r = ADMa.ADM_sph_ini_gauge_geodesic(r)

# check constraints initially
ini_H = ADMs.ADM_sph_con_H(ini_gam_1, ini_gam_2, ini_kap_1, ini_kap_2,
  r, nghost=nghost)

ini_M_r = ADMs.ADM_sph_con_M(ini_gam_1, ini_gam_2, ini_kap_1, ini_kap_2,
  r, nghost=nghost)


# attempt evolution
dt = (t_f - t_i) / N_t
t = t_i
sys_fcn = ft.partial(ADM_system, r=r, nghost=nghost)

# prepare initial state vector
vars = (ini_alpha, ini_beta_r, ini_gam_1, ini_gam_2, ini_kap_1, ini_kap_2)
u_c = np.vstack(vars)

for t_idx in range(int(N_t)):
  u_c = it.ev_step_RK4(t, u_c, dt, sys_fcn=sys_fcn)
  t = t + dt


# check constraints at final time
fin_alpha, fin_beta_r, fin_gam_1, fin_gam_2, fin_kap_1, fin_kap_2 = u_c

fin_H = ADMs.ADM_sph_con_H(fin_gam_1, fin_gam_2, fin_kap_1, fin_kap_2,
  r, nghost=nghost)

fin_M_r = ADMs.ADM_sph_con_M(fin_gam_1, fin_gam_2, fin_kap_1, fin_kap_2,
  r, nghost=nghost)


#
# :D
#
