#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Tue May 25 2021>

@author: Boris Daszuta
@function:
Collect integrators and associated functions here.
"""
import numpy as np

# -----------------------------------------------------------------------------
# utility functions
def N_t_from_CFL(CFL, dx, ti, tf, v=1):
  return int(np.ceil(v * ((tf - ti) / CFL) / dx))

def CFL_from_N_t(N_t, dx, ti, tf, v=1):
  return v * (tf - ti) / (dx * N_t)

# -----------------------------------------------------------------------------
# integrators
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


#
# :D
#
