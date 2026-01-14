import numpy as np
import matplotlib.pyplot as plt


def draw_exponential_distribution(lam, size=1000):
    """
    Draw samples from an exponential distribution and plot the histogram.

    Parameters:
    lam (float): The rate parameter (lambda) of the exponential distribution.
    size (int): The number of samples to draw.
    """
    samples = np.random.exponential(1/lam, size)

    return samples


if __name__ == "__main__":
    z_n = 5
    lam = 1.0

    n = 10000  # number of samples should be dividable by 5
    Y_z_list = []
    for z in range(1, z_n + 1):
        X_z = draw_exponential_distribution(lam, size=n//5)
        Y_z_list.append(z * X_z)

    y_values = np.linspace(0, 30, 1000)
    estimator = np.empty_like(y_values, dtype=float)
    for i, y in enumerate(y_values):
        estimator[i] = sum(np.sum(Y_z <= y) for Y_z in Y_z_list) / n

    plt.plot(y_values, estimator, label='Empirical CDF', color='blue')
    plt.title('Empirical CDF of Mixture of Exponential Distributions')
    plt.xlabel('y')
    plt.ylabel('F_Y(y)')
    plt.legend()
    plt.grid()
    plt.show()
