import numpy as np
import matplotlib.pyplot as plt


## Script to estimate theta = int_0^1 exp(x^2) dx = E(g(x)), where g(x) = exp(x^2) and x ~ U(0,1)

def g(x):
    return np.exp(x**2)
    
def tilted_density(x, t):
    return t / (np.exp(t) - 1) * np.exp(t * x)

def F_tilde_inv_tilted(u, t):
    return (1 / t) * np.log(u * (np.exp(t) - 1) + 1)
    
def importance_sampling(num_samples=10000, t=1):
    u_samples = np.random.uniform(0, 1, num_samples)
    x_samples = F_tilde_inv_tilted(u_samples, t)
    weights = g(x_samples) / tilted_density(x_samples, t)
    theta_estimate = np.mean(weights)

    # Variance
    variance = np.var(weights) / num_samples

    # Running mean
    running_mean = np.cumsum(weights) / np.arange(1, num_samples + 1)
    return theta_estimate, variance, running_mean

def classical_monte_carlo(num_samples=10000):
    x_samples = np.random.uniform(0, 1, num_samples)
    g_values = g(x_samples)
    theta_estimate = np.mean(g_values)
    variance = np.var(g_values) / num_samples
    running_mean = np.cumsum(g_values) / np.arange(1, num_samples + 1)
    return theta_estimate, variance, running_mean

if __name__ == "__main__":
    num_samples = 10000
    t_list = np.linspace(-2, 3, 50)
    variance_list = []
    for t in t_list:

        # theta_classical = classical_monte_carlo(num_samples=num_samples)
        theta_importance = importance_sampling(num_samples=num_samples, t=t)
        variance_list.append(theta_importance[1])

        # print(f"Classical Monte Carlo estimate (t = {t}): {theta_classical[0]}, Variance: {theta_classical[1]}")
        print(f"Importance Sampling estimate (t = {t}): {theta_importance[0]}, Variance: {theta_importance[1]}")

    # Plot variance vs t
    plt.figure(figsize=(10, 5))
    plt.plot(t_list, variance_list, marker='o')
    plt.xlabel('t parameter')
    plt.ylabel('Variance of Importance Sampling Estimate')
    plt.title('Variance of Importance Sampling Estimate vs t parameter')
    plt.grid()
    plt.show()

    # Plot best t
    best_t = t_list[np.argmin(variance_list)]
    print(f"Best t value minimizing variance: {best_t}")
    theta_importance = importance_sampling(num_samples=num_samples, t=best_t)



    # Plotting of the running means
    plt.figure(figsize=(12, 6))
    # plt.plot(theta_classical[2], label='Classical MC', alpha=0.7)
    plt.plot(theta_importance[2], label='Importance Sampling', alpha=0.7)
    plt.axhline(y=1.46265, color='r', linestyle='--', label='True Value')
    plt.xlabel('Number of Samples')
    plt.ylabel('Running Mean Estimate of θ')
    plt.title('Running Mean Estimates of θ using Different Methods')
    plt.legend()
    plt.grid()
    plt.show()
