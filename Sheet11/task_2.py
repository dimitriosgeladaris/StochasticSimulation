import numpy as np
import matplotlib.pyplot as plt


## Script to estimate theta = int_0^1 exp(x^2) dx = E(g(x)), where g(x) = exp(x^2) and x ~ U(0,1)

def g(x):
    return np.exp(x**2)

def f_tilde(x, task=2):
    if task == 2:
        return 2 * x
    elif task == 3:
        return np.exp(x)/(np.exp(1)-1)
    else:
        raise ValueError("Invalid task number. Use 2 or 3.")
    
def F_tilde_inv(u, task=2):
    if task == 2:
        return np.sqrt(u)
    elif task == 3:
        return np.log(u * (np.exp(1)-1) + 1)
    else:
        raise ValueError("Invalid task number. Use 2 or 3.")
    
def importance_sampling(num_samples=10000, task=2):
    u_samples = np.random.uniform(0, 1, num_samples)
    x_samples = F_tilde_inv(u_samples, task=task)
    weights = g(x_samples) / f_tilde(x_samples, task=task)
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

    theta_classical = classical_monte_carlo(num_samples=num_samples)
    theta_importance_task2 = importance_sampling(num_samples=num_samples, task=2)
    theta_importance_task3 = importance_sampling(num_samples=num_samples, task=3)

    print(f"Classical Monte Carlo estimate: {theta_classical[0]}, Variance: {theta_classical[1]}")
    print(f"Importance Sampling (task 2) estimate: {theta_importance_task2[0]}, Variance: {theta_importance_task2[1]}")
    print(f"Importance Sampling (task 3) estimate: {theta_importance_task3[0]}, Variance: {theta_importance_task3[1]}")

    # Plotting of the running means
    plt.figure(figsize=(12, 6))
    plt.plot(theta_classical[2], label='Classical MC', alpha=0.7)
    plt.plot(theta_importance_task2[2], label='Importance Sampling Task 2', alpha=0.7)
    plt.plot(theta_importance_task3[2], label='Importance Sampling Task 3', alpha=0.7)
    plt.axhline(y=1.46265, color='r', linestyle='--', label='True Value')
    plt.xlabel('Number of Samples')
    plt.ylabel('Running Mean Estimate of θ')
    plt.title('Running Mean Estimates of θ using Different Methods')
    plt.legend()
    plt.grid()
    plt.show()
