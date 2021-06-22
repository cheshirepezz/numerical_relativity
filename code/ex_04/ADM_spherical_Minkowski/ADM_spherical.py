#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Implementation of ADM system in spherical symmetry
"""
import numpy as np
import operators as op
import grids as gr
import ADM_auxiliaries as ADMa

# -----------------------------------------------------------------------------
# evolution equations

def ADM_sph_sys(alpha, beta_r, gam_1, gam_2, kap_1, kap_2, r, nghost=1):
  # this assumes parity is already suitably imposed on fields

  d1r_alpha = gr.ghost_pad(op.D1(alpha, r, nghost=nghost), nghost=nghost)
  d2r_alpha = gr.ghost_pad(op.D2(alpha, r, nghost=nghost), nghost=nghost)
  d1r_beta_r = gr.ghost_pad(op.D1(beta_r, r, nghost=nghost), nghost=nghost)

  d1r_gam_1 = gr.ghost_pad(op.D1(gam_1, r, nghost=nghost), nghost=nghost)
  d1r_gam_2 = gr.ghost_pad(op.D1(gam_2, r, nghost=nghost), nghost=nghost)
  d2r_gam_2 = gr.ghost_pad(op.D2(gam_2, r, nghost=nghost), nghost=nghost)

  d1r_kap_1 = gr.ghost_pad(op.D1(kap_1, r, nghost=nghost), nghost=nghost)
  d1r_kap_2 = gr.ghost_pad(op.D1(kap_2, r, nghost=nghost), nghost=nghost)

  dt_gam_1 = np.zeros_like(r)
  dt_gam_2 = np.zeros_like(r)
  dt_kap_1 = np.zeros_like(r)
  dt_kap_2 = np.zeros_like(r)

  # term-by-term
  dt_gam_1 -= 2 * alpha * kap_1
  dt_gam_1 += 2 * gam_1 * d1r_beta_r
  dt_gam_1 += beta_r * d1r_gam_1

  dt_gam_2 -= 2 * alpha * kap_2
  dt_gam_2 += beta_r * d1r_gam_2

  dt_kap_1 -= alpha * (kap_1 ** 2) / gam_1
  dt_kap_1 += 2 * alpha * kap_1 * kap_2 / gam_2
  dt_kap_1 += 2 * kap_1 * d1r_beta_r
  dt_kap_1 += d1r_alpha * d1r_gam_1 / (2 * gam_1)
  dt_kap_1 += alpha * d1r_gam_1 * d1r_gam_2 / (2 * gam_1 * gam_2)
  dt_kap_1 += alpha * (d1r_gam_2 ** 2) / (2 * (gam_2 ** 2))
  dt_kap_1 += beta_r * d1r_kap_1
  dt_kap_1 -= d2r_alpha
  dt_kap_1 -= alpha * d2r_gam_2 / gam_2

  dt_kap_2 += alpha
  dt_kap_2 += alpha * kap_1 * kap_2 / gam_1
  dt_kap_2 -= d1r_alpha * d1r_gam_2 / (2 * gam_1)
  dt_kap_2 += alpha * d1r_gam_1 * d1r_gam_2 / (4 * (gam_1 ** 2))
  dt_kap_2 += beta_r * d1r_kap_2
  dt_kap_2 -= alpha * d2r_gam_2 / (2 * gam_1)

  return dt_gam_1, dt_gam_2, dt_kap_1, dt_kap_2

# -----------------------------------------------------------------------------
# gauge conditions

def ADM_sph_geodesic(t, r, nghost=1):
  # geodesic gauge fixes initial alpha=1
  # return np.zeros_like(r), np.zeros_like(r)
  return ADMa.ADM_sph_ini_gauge_geodesic(r)

# -----------------------------------------------------------------------------
# constraint equations

def ADM_sph_con_H(gam_1, gam_2, kap_1, kap_2, r, nghost=1):
  # Hamiltonian constraint

  H = np.zeros_like(gam_1)

  # prepare derivatives
  d1r_gam_1 = gr.ghost_pad(op.D1(gam_1, r, nghost=nghost), nghost=nghost)
  d1r_gam_2 = gr.ghost_pad(op.D1(gam_2, r, nghost=nghost), nghost=nghost)
  d2r_gam_2 = gr.ghost_pad(op.D2(gam_2, r, nghost=nghost), nghost=nghost)

  # do term-by-term
  H += 2 / gam_2
  H += 4 * kap_1 * kap_2 / (gam_1 * gam_2)
  H += 2 * kap_2 ** 2 / gam_2 ** 2
  H += d1r_gam_1 * d1r_gam_2 / (gam_1 ** 2 * gam_2)
  H += d1r_gam_2 ** 2 / (2 * gam_1 * (gam_2 ** 2))
  H -= 2 * d2r_gam_2 / (gam_1 * gam_2)

  return H

def ADM_sph_con_M(gam_1, gam_2, kap_1, kap_2, r, nghost=1):
  # contravariant radial component of momentum constraint is non-trivial

  # prepare derivatives
  d1r_gam_2 = gr.ghost_pad(op.D1(gam_2, r, nghost=nghost), nghost=nghost)
  d1r_kap_2 = gr.ghost_pad(op.D2(kap_2, r, nghost=nghost), nghost=nghost)


  M_r = np.zeros_like(r)

  # do term-by-term
  M_r += kap_1 * d1r_gam_2 / (gam_1 * gam_2)
  M_r += kap_2 * d1r_gam_2 / (gam_2 ** 2)
  M_r -= 2 * d1r_kap_2 / (gam_2)

  return M_r

#
# :D
#
