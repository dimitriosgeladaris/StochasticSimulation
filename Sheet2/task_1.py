import numpy as np
import matplotlib.pyplot as plt


def draw_pareto(n, alpha, sigma):
    u = np.random.uniform(0, 1, n)
    return sigma * (u ** (-1 / alpha) - 1)


def mean_process(data):
    cumsum = np.cumsum(data)
    counts = np.arange(1, data.size + 1)
    return cumsum / counts


if __name__ == "__main__":
    n = 1000000
    alphas = [1, 2]
    sigma = 2
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    for a, alpha in zip(ax, alphas):
        pareto_data = draw_pareto(n, alpha, sigma)
        mean_pareto = mean_process(pareto_data)
        if alpha == 1:
            expected_value = np.inf  # for alpha <= 1
        else:
            expected_value = (sigma / (alpha - 1))  # for alpha > 1
        a.plot(mean_pareto)
        a.axhline(expected_value, color='r', linestyle='--')
        a.set_title(f'Mean Process of Pareto Distribution (alpha={alpha})')
    plt.show()
