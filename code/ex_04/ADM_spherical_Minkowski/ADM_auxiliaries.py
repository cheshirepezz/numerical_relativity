#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Initial data / gauge specification
"""
import numpy as np
import operators as op

# -----------------------------------------------------------------------------
# initial data and gauge selection

def ADM_sph_ini_Minkowski(gr):
  # initial (naive) Minkowskian data
  gam_1 = 1 + np.zeros_like(gr)
  gam_2 = gr ** 2
  kap_1 = kap_2 = np.zeros_like(gr)

  return gam_1, gam_2, kap_1, kap_2

def ADM_sph_ini_gauge_geodesic(gr):
  # specify gauge
  alpha = np.ones_like(gr)
  beta_r = np.zeros_like(gr)

  return alpha, beta_r


#
# :D
#
