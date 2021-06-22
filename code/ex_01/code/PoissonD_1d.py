#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ,-*
(_) Created on <Mon Apr 19 2021>

@author: Boris Daszuta
@function:
Example of Poisson eqn with Dirichlet BC in 1d.

Modified to answer questions of the exercise sheet.
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as spl

def fsource(x):
  return -x * (x + 3) * np.exp(x)

def uexact(x):
  return x * (x - 1) * np.exp(x)

def matrix_D2(N):
  # generate the FD stencil
  l = np.diag(np.ones(N), k=-1)
  d = -2 * np.diag(np.ones(N + 1), k=0)
  u = np.diag(np.ones(N), k=1)
  return (l + d + u)

def matrix_A(N):
  # build the LHS of (**)
  D2 = matrix_D2(N)

  # impose the boundary conditions
  D2[0, :] = 0   # clear first
  D2[-1, :] = 0  # and last rows
  D2[0, 0] = 1
  D2[-1, -1] = 1

  return D2

def solver(N):
  x = np.linspace(0, 1, num=N + 1)
  dx = x[1] - x[0]

  A = matrix_A(N)
  inv_A = np.linalg.inv(A)
  f = - dx ** 2 * fsource(x)

  # ensure that u_0 = u_N = 0 (set the RHS)
  f[0] = f[-1] = 0
  u = np.dot(inv_A, f)
  return x, u

def solver_banded(N):
  x = np.linspace(0, 1, num=N + 1)
  dx = x[1] - x[0]

  d = -2 * np.ones(N+1)
  d[0] = d[-1] = 1

  u = np.ones(N+1)
  l = np.ones(N+1)
  u[:2] = 0
  l[-2:] = 0
  A_banded = np.vstack((u, d, l))

  # A = matrix_A(N)
  # inv_A = np.linalg.inv(A)
  f = - dx ** 2 * fsource(x)

  # ensure that u_0 = u_N = 0 (set the RHS)
  f[0] = f[-1] = 0

  u = spl.solve_banded((1, 1), A_banded, f)
  return x, u


if __name__ == '__main__':
  # construct a solution

  # N = 10
  # x, u_num = solver(N)
  # u_exa = uexact(x)

  # plt.plot(x, u_num, '-r')
  # plt.plot(x, u_exa, '--g')

  # plt.show()

  N = 5  # starting value
  p_num = 11
  N_ran = N * 2 ** np.arange(p_num)

  err_vec = np.zeros_like(N_ran, dtype=np.float64)

  for i in range(p_num):
    N_cur = N_ran[i]
    x, u_num = solver_banded(N_cur)
    u_exa = uexact(x)

    abs_diff_u = np.abs(u_num - u_exa)
    max_abs_diff_u = np.max(abs_diff_u)

    dx = x[1] - x[0]
    print(dx, N_cur, max_abs_diff_u)
    err_vec[i] = max_abs_diff_u


# check that this follows expected second order
log_err_vec = np.log(err_vec)
log_N_ran = np.log(N_ran)

log_sqr_vec = 2 * np.log(N_ran)

plt.loglog(N_ran, err_vec, '-r', label='max|err|')
plt.loglog(N_ran, 1 / N_ran ** (2), '--b', label='1 / N^2 trend')

plt.xlabel('N')
plt.ylabel('max_i|err_i|')
plt.legend()
plt.show()


#
# :D
#
