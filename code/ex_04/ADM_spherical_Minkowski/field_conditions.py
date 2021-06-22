#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Boundary and regularity conditions
"""
import numpy as np
import operators as op

def BC_parity(ext_fcn, is_even=True, left_side=True, nghost=1):
  # apply parity condition to input field

  sign = 1 if is_even else -1

  if left_side:
    ext_fcn[:nghost, ...] = sign * ext_fcn[nghost:2*nghost, ...][::-1, ...]
  else:
    ext_fcn[-nghost:, ...] = sign * ext_fcn[-2*nghost:-nghost, ...][::-1, ...]


def BC_outflow(ext_fcn, order=1, nghost=1):
  for nix in range(-nghost, 0):
    if order == 1:
      ext_fcn[nix, ...] = ext_fcn[nix-1, ...]
    else:
      ext_fcn[nix, ...] = 2 * ext_fcn[nix-1, ...] - ext_fcn[nix-2, ...]

#
# :D
#
