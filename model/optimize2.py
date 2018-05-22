from scipy.optimize import minimize, rosen, rosen_der
import numpy as np
from functools import partial

def fun_to_optimize(matrix):
    res = 0
    for row in matrix:
        res += rosen(row)
    return res / matrix.shape[0]


def de_flatten(vec, columns):
    return fun_to_optimize(vec.reshape(-1, columns))


x0 = np.array([[1.3, 0.7, 0.8, 1.9, 1.2],
               [1.3, 0.7, 0.8, 1.9, 1.2],
               [1.3, 0.7, 0.8, 1.9, 1.2]])


bnds = tuple([(1, None) for i in range(x0.shape[0]*x0.shape[1])])

print(bnds)
columns = 5
opt_fun = partial(de_flatten, columns=columns)
res = minimize(opt_fun, x0.flatten(), method='Nelder-Mead', tol=1e-6)
print(res.x.reshape(-1, columns))
res = minimize(opt_fun, x0.flatten(), method='SLSQP', tol=1e-6, bounds=bnds)
print(res.x.reshape(-1, columns))


