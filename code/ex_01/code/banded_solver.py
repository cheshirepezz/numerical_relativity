"""
 ,-*
(_)

@author: Boris Daszuta
@function: Collect linear algebraic solvers
"""
import numpy as np
import scipy.linalg as spl

def linalg_tridiagonal(a, b, c, y):
  '''
  Solver for x in Tx=y where T is tridiagonal with structure:

    b_0     c_0      0      ...
    a_0     b_1     c_1      0      ...
     0      a_1     b_2     c_2      0      ...
     .       0       .       .       .       .
             .       0    a_{n-3} b_{n-2} c_{n-2}
                     .       0    a_{n-2} b_{n-1}
  Therefore for P = [nxn]:
    a = [n-1]
    b = [n]
    c = [n-1]

  This uses the Thomas algorithm.

  Inputs are preserved.

  Note
  ----
  No checks are performed as to whether P is invertible.
  '''
  sz = b.size

  # create scratch arrays
  c_star = np.empty(sz-1, dtype=y.dtype)
  d_star = np.empty(sz, dtype=y.dtype)
  x = np.empty(sz, dtype=y.dtype)

  # Forward sweep
  c_star[0] = c[0] / b[0]
  d_star[0] = y[0] / b[0]

  for ix in range(1, sz-1):
    m = 1. / (b[ix] - a[ix-1] * c_star[ix-1])
    c_star[ix] = c[ix] * m
    d_star[ix] = (y[ix] - a[ix-1] * d_star[ix-1]) * m

  m = 1. / (b[sz-1] - a[sz-2] * c_star[sz-2])
  d_star[sz-1] = (y[sz-1] - a[sz-2] * d_star[sz-2]) * m

  # Backward sweep
  x[sz-1] = d_star[sz-1]
  for ix in range(sz-2, -1, -1):
    x[ix] = d_star[ix] - c_star[ix] * x[ix+1]
  return x

if __name__ == '__main__':

  print('Test tridiagonal solver:')

  # specify the bands
  a = np.array([3., 1, -3.7])
  b = np.array([10., 1.2, 7., 4.])
  c = np.array([2.11, 4.3, 5.7])

  # the inhomogeneity
  d = np.array([-3.1,4.7,5.2,6.])

  # dense version
  A = np.diag(c, k=1) + np.diag(b, k=0) + np.diag(a, k=-1)

  print('np: naive inverse')
  iA = np.linalg.inv(A)
  np_sol = np.dot(iA, d)
  print(np_sol)

  print('tridiagonal (Thomas algo.)')
  tdma_sol = linalg_tridiagonal(a, b, c, d)
  print(tdma_sol)

  # massage this according to what scipy documentation requires
  ab = np.zeros((3, b.size))

  ab[0, 1:] = c[:]
  ab[1, :] = b[:]
  ab[2, :-1] = a[:]

  sp_sol = spl.solve_banded((1, 1), ab, d)

  print('scipy.linalg.solve_banded')
  print(sp_sol)

#
# :D
#