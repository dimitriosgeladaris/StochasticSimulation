import numpy as np
import scipy.special as scipy
import matplotlib.pyplot as plt

def binomial_distribution(n, p, k):
    """
    Calculate the probability of getting exactly k successes in n independent Bernoulli trials
    with success probability p using the binomial distribution formula.
    """
    return scipy.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def inverse_transform_binomial(n, p, u):
    """
    Perform inverse transform sampling to generate a binomially distributed random variable.
    Given a uniform random variable u in [0, 1), return the corresponding binomial random variable.
    """
    cumulative_probability = 0.0
    for k in range(n + 1):
        cumulative_probability += binomial_distribution(n, p, k)
        if cumulative_probability >= u:
            return k
    return n  # In case u is very close to 1

def recursion_binomial_distribution(n, p, k):
    if k == 0:
        return (1 - p) ** n
    elif k == n:
        return p ** n
    else:
        return (n - k + 1) * p / (k * (1 - p)) * recursion_binomial_distribution(n, p, k - 1)
    
def recursion_inverse_transform_binomial(n, p, u):
    k = 0
    p0 = (1 - p) ** n
    F = p0
    while F < u and k < n:
        k += 1
        pk = (n - k + 1) * p / (k * (1 - p)) * p0
        F += pk
        p0 = pk
    return k

def negative_binomial_distribution(r, p, k):
    """
    Calculate the probability of getting k failures before r successes in a sequence of independent Bernoulli trials
    with success probability p using the negative binomial distribution formula.
    """
    return scipy.comb(k + r - 1, r - 1) * (p ** r) * ((1 - p) ** k)

def inverse_transform_negative_binomial(r, p, u):
    """
    Perform inverse transform sampling to generate a negative binomially distributed random variable.
    Given a uniform random variable u in [0, 1), return the corresponding negative binomial random variable.
    """
    cumulative_probability = 0.0
    k = 0
    while True:
        cumulative_probability += negative_binomial_distribution(r, p, k)
        if cumulative_probability >= u:
            return k
        k += 1
    return n

def recursion_negative_binomial_distribution(r, p, k):
    if k == 0:
        return p ** r
    else:
        return (k + r - 1) / k * (1 - p) * recursion_negative_binomial_distribution(r, p, k - 1)
    
def recursion_inverse_transform_negative_binomial(r, p, u):
    k = 0
    p0 = p ** r
    F = p0
    while F < u:
        k += 1
        pk = (k + r - 1) / k * (1 - p) * p0
        F += pk
        p0 = pk
    return k



if __name__ == "__main__":

    sample_size = 10000
    n = 100
    p = 0.6

    ## Generate binomial random samples using inverse transform sampling
    uniform_random_samples = np.random.uniform(0, 1, sample_size)
    binomial_random_samples = [inverse_transform_binomial(n, p, u) for u in uniform_random_samples]
    plt.hist(binomial_random_samples, bins=range(n + 2), density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'Histogram of Binomial Distribution Samples (n={n}, p={p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    recursive_binomial_random_samples = [recursion_inverse_transform_binomial(n, p, u) for u in uniform_random_samples]
    plt.hist(recursive_binomial_random_samples, bins=range(n + 2), density=True, alpha=0.7, color='green', edgecolor='black')
    plt.title(f'Histogram of Binomial Distribution Samples (Recursive) (n={n}, p={p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    r = 2
    p = 0.7
    uniform_random_samples = np.random.uniform(0, 1, sample_size)
    negative_binomial_random_samples = [inverse_transform_negative_binomial(5, p, u) for u in uniform_random_samples]
    plt.hist(negative_binomial_random_samples, bins=range(max(negative_binomial_random_samples) + 2), density=True, alpha=0.7, color='red', edgecolor='black')
    plt.title(f'Histogram of Negative Binomial Distribution Samples (r=5, p={p})')
    plt.xlabel('Number of Failures')
    plt.ylabel('Probability')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    recursive_negative_binomial_random_samples = [recursion_inverse_transform_negative_binomial(5, p, u) for u in uniform_random_samples]
    plt.hist(recursive_negative_binomial_random_samples, bins=range(max(recursive_negative_binomial_random_samples) + 2), density=True, alpha=0.7, color='orange', edgecolor='black')
    plt.title(f'Histogram of Negative Binomial Distribution Samples (Recursive) (r=5, p={p})')
    plt.xlabel('Number of Failures')
    plt.ylabel('Probability')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
