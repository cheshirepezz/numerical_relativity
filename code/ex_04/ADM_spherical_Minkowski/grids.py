#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Collect grid generation and related functions here.
"""
import numpy as np

# -----------------------------------------------------------------------------
# grid generation

def gr_P(N, nghost=0):
  # make a periodic grid, optionally extend by a number of ghosts
  a, b = 0, 2 * np.pi
  dx = (b - a) / N
  Num_wg = (N + 1 + 2 * nghost)
  ix_i = (np.arange(0, Num_wg) - nghost)
  return ix_i * dx

def gr_CC(N, a=-1, b=1, nghost=0):
  # make a cell-centered grid.
  N_ext = N + 2 * nghost
  dx = (b - a) / N

  return a + dx / 2 + dx * np.arange(-nghost, N + nghost)

def gr_VC(N, a=-1, b=1, nghost=0):
  # make a vertex-centered grid.

  N_ext = (N + 1) + 2 * nghost
  dx = (b - a) / N
  return a + dx * np.arange(-nghost, N + 1 + nghost)

# -----------------------------------------------------------------------------
# convenience function for ghost extensions / restrictions

def ghost_pad(fcn, nghost=0):
  # given a sampled function pad with (zeroed) ghosts
  if nghost == 0:
    return fcn

  sz = fcn.size
  ext_fcn = np.zeros(sz + 2 * nghost)
  ext_fcn[nghost:-nghost] = fcn[:]
  return ext_fcn

def ghost_trim(ext_fcn, nghost=0):
  # given extended function data trim to physical nodes
  if nghost == 0:
    return ext_fcn

  return ext_fcn[nghost:-nghost, ...]


#
# :D
#
