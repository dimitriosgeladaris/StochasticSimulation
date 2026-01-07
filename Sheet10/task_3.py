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

def exponential_CDF(y, lam):
    """
    Compute the CDF of an exponential distribution at value y.
    
    Parameters:
    y (float): The value at which to compute the CDF.
    lam (float): The rate parameter (lambda) of the exponential distribution.
    
    Returns:
    float: The CDF value at y.
    """
    if y < 0:
        return 0.0
    return 1 - np.exp(-lam * y)

if __name__ == "__main__":
    lam_z = 1/3

    n = 1000 # number of samples for z should be dividable by 5
    Y_z_list = []
    z_list = draw_exponential_distribution(lam_z, size=n)
    
    y_values = np.linspace(0, 30, 1000)
    estimator = np.empty_like(y_values, dtype=float)
    for i,y in enumerate(y_values):
        estimator_value = 0.0
        for z in z_list:
            estimator_value += exponential_CDF(y, lam=1/z)
        estimator_value /= n
        estimator[i] = estimator_value


    plt.plot(y_values, estimator, label='Empirical CDF', color='blue')
    plt.title('Empirical CDF of Mixture of Exponential Distributions')
    plt.xlabel('y')
    plt.ylabel('F_Y(y)')
    plt.legend()
    plt.grid()
    plt.show()