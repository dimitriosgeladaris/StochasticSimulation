import numpy as np
import matplotlib.pyplot as plt

def lcg_random(x0, a, c, m):
    """
    Linear Congruential Generator (LCG) to produce pseudo-random numbers.
    
    Parameters:
    seed (int): Initial seed value.
    a (int): Multiplier.
    c (int): Increment.
    m (int): Modulus.
    
    Returns:
    int: Next pseudo-random number.
    """
    return (a * x0 + c) % m

if __name__ == "__main__":
    fig, ax = plt.subplots(2, 2)
    
    param_list = [[0, 133, 7, 432], [1, 109, 5, 216], [0, 4, 2, 243], [1, 41, 11, 1000]] # Form [seed, a, c, m]
    for axis, params in zip(ax.flatten(), param_list):
        x0, a, c, m = params
        random_numbers = []
        for i in range(m):
            x0 = lcg_random(x0, a, c, m) 
            random_numbers.append(x0/m)
        plot_vectors = [(random_numbers[i], random_numbers[i+1]) for i in range(len(random_numbers)-1)]
        axis.scatter(*zip(*plot_vectors), s=1)
        axis.set_title(f"LCG with a={a}, c={c}, m={m}")
    plt.tight_layout()
    plt.show()