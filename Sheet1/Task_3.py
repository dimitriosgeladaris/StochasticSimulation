import numpy as np
import matplotlib.pyplot as plt

def middle_square_method(seed):
    squared = str(seed ** 2).zfill(8)  # Square the seed and pad with zeros
    middle_digits = squared[2:6]  # Extract the middle four digits
    return int(middle_digits)

if __name__ == "__main__":
    # Generate random numbers using the Middle Square Method
    seeds = np.linspace(1000, 9999, num=12, dtype=int)  # Generate 5 different 4-digit seeds
    for seed in seeds:
        random_numbers = [seed]
        for _ in range(200):
            seed = middle_square_method(seed)
            random_numbers.append(seed)

        # Plot the random numbers
        plt.figure(figsize=(10, 5))
        plt.plot(random_numbers, marker='o')
        plt.title("Middle Square Method")
        plt.xlabel("Iteration")
        plt.ylabel("Random Number")
        plt.grid()
        plt.show()