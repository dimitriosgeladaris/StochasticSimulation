import numpy as np
import scipy.special
import time
from itertools import product

def h(u):
    """Indicator for unit ball after transformation"""
    x = 2*u - 1
    return np.sum(x**2) <= 1

def monte_carlo_volume(d, m, seed=0):
    np.random.seed(seed)
    n = m**d
    start = time.time()
    U = np.random.rand(n, d)
    values = np.sum((2*U - 1)**2, axis=1) <= 1
    estimate = (2**d) * np.mean(values)
    runtime = time.time() - start
    return estimate, runtime

def anithetic_variates_volume(d, m, seed=0):
    np.random.seed(seed)
    n = m**d // 2
    start = time.time()
    U = np.random.rand(n, d)
    U_anti = 1 - U
    values = np.sum((2*U - 1)**2, axis=1) <= 1
    values_anti = np.sum((2*U_anti - 1)**2, axis=1) <= 1
    estimate = (2**d) * np.mean((values + values_anti) / 2)
    runtime = time.time() - start
    return estimate, runtime

def riemann_volume(d, m):
    start = time.time()
    grid_1d = (np.arange(m) + 0.5) / m
    count = 0
    for u in product(grid_1d, repeat=d):
        count += h(np.array(u))
    estimate = (2**d) * count / (m**d)
    runtime = time.time() - start
    return estimate, runtime

def exact_volume(d):
    # Unit ball volume formula
    return (np.pi**(d/2)) / scipy.special.gamma(d/2 + 1)

m = 400
for d in [2, 3]:
    exact_volume_val = exact_volume(d)
    mc_est, mc_time = monte_carlo_volume(d, m)
    av_est, av_time = anithetic_variates_volume(d, m)
    ri_est, ri_time = riemann_volume(d, m)
    print(f"\nd = {d}")
    print(f"Exact volume:        {exact_volume_val:.6f}")
    print(f"Monte Carlo:         {mc_est:.6f} (time {mc_time:.2f}s)")
    print(f"Antithetic Variates: {av_est:.6f} (time {av_time:.2f}s)")
    print(f"Riemann sum:         {ri_est:.6f} (time {ri_time:.2f}s)")
    print(f"Monte Carlo error:   {abs(mc_est - exact_volume_val):.6f}")
    print(f"Antithetic Variates error: {abs(av_est - exact_volume_val):.6f}")
    print(f"Riemann sum error:   {abs(ri_est - exact_volume_val):.6f}")