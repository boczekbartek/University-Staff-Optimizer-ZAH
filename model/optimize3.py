import cvxpy as cp
import numpy as np

from enumy import *
from input_data import *

from scipy.optimize import minimize
from model.Solution import *

weights = np.array([
    # ZAH_LAB ZAH_WYKLAD SOI_LAB SOI_WYKKLAD
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],  # ograniczenie
])

import scipy.optimize as spo

cov_matrix = np.array([[1, 1, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1],
                      [1, 1, 1, 1]])


def portfolio_vol(w):
    # compute porfolio volatility
    portfolio_volatility = np.sqrt(w.T.dot(cov_matrix).dot(w))
    return portfolio_volatility


def find_optimal_allocations():
    bnds = tuple((0.00, 0.02) for x in weights)
    cons = ({'type': 'eq', 'fun': lambda x: 1 - sum(x)}, {'type': 'ineq', 'fun': lambda x: sum(x ** 2) - 0.02})
    result = spo.minimize(portfolio_vol, weights, method='SLSQP', bounds=bnds, constraints=cons, options={'disp' : True})
    return result.x

find_optimal_allocations()
