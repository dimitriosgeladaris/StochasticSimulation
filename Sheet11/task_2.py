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
    return theta_estimate, variance

def classical_monte_carlo(num_samples=10000):
    x_samples = np.random.uniform(0, 1, num_samples)
    g_values = g(x_samples)
    theta_estimate = np.mean(g_values)
    variance = np.var(g_values) / num_samples
    return theta_estimate, variance

if __name__ == "__main__":
    num_samples = 10000

    theta_classical = classical_monte_carlo(num_samples=num_samples)
    theta_importance_task2 = importance_sampling(num_samples=num_samples, task=2)
    theta_importance_task3 = importance_sampling(num_samples=num_samples, task=3)

    print(f"Classical Monte Carlo estimate: {theta_classical[0]}, Variance: {theta_classical[1]}")
    print(f"Importance Sampling (task 2) estimate: {theta_importance_task2[0]}, Variance: {theta_importance_task2[1]}")
    print(f"Importance Sampling (task 3) estimate: {theta_importance_task3[0]}, Variance: {theta_importance_task3[1]}")

    # Plotting the convergence of estimates
    sample_sizes = np.arange(10, num_samples + 1, 10)
    classical_estimates = []
    importance_estimates_task2 = []
    importance_estimates_task3 = []
    for size in sample_sizes:
        classical_estimates.append(classical_monte_carlo(num_samples=size)[0])
        importance_estimates_task2.append(importance_sampling(num_samples=size, task=2)[0])
        importance_estimates_task3.append(importance_sampling(num_samples=size, task=3)[0])
    plt.plot(sample_sizes, classical_estimates, label='Classical MC', color='blue')
    plt.plot(sample_sizes, importance_estimates_task2, label='Importance Sampling Task 2', color='orange')
    plt.plot(sample_sizes, importance_estimates_task3, label='Importance Sampling Task 3', color='green')
    plt.axhline(y=1.462651745907181, color='red', linestyle='--', label='True Value')
    plt.xlabel('Number of Samples')     
    plt.ylabel('Estimate of θ')
    plt.title('Convergence of Monte Carlo Estimates')
    plt.legend()
    plt.grid()
    plt.show()