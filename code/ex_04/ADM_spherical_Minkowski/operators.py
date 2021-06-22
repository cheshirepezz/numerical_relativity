#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Collect discretized operators here.
"""
import numpy as np

# -----------------------------------------------------------------------------
# derivative operators

def D1(ext_fcn, gr, nghost=1):
  # discretized, centered first order derivative operator
  dx = gr[1] - gr[0]

  if nghost == 1:
    return (-1 / 2 * ext_fcn[0:-2, ...] + 1 / 2 * ext_fcn[2:, ...]) / dx
  elif nghost == 2:
    return (1 / 12 * ext_fcn[0:-4] - 2 / 3 * ext_fcn[1:-3]
      + 2 / 3 * ext_fcn[3:-1] - 1 / 12 * ext_fcn[4:]) / dx

def D2(ext_fcn, gr, nghost=1):
  # discretized, centered second order derivative operator
  dx = gr[1] - gr[0]

  if nghost == 1:
    return (1 * ext_fcn[0:-2, ...] - 2 * ext_fcn[1:-1, ...]
      + 1 * ext_fcn[2:, ...]) / (dx ** 2)
  elif nghost == 2:
    return (-1 / 12 * ext_fcn[0:-4] + 4 / 3 * ext_fcn[1:-3]
      - 5 / 2 * ext_fcn[2:-2]
      + 4 / 3 * ext_fcn[3:-1] - 1 / 12 * ext_fcn[4:]) / (dx ** 2)

#
# :D
#
