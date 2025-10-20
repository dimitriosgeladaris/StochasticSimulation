import numpy as np
import matplotlib.pyplot as plt

def draw_customer(min, max):
    """
    Draw a random number of customers between min and max (inclusive).
    
    Parameters:
    min (int): Minimum number of customers.
    max (int): Maximum number of customers.
    
    Returns:
    int: Randomly drawn number of customers.
    """
    return np.random.randint(min, max + 1)


def draw_bretzel_per_costumer(min, max, customers):
    """
    Draw a random number of bretzels per customer between min and max (inclusive).
    
    Parameters:
    min (int): Minimum number of bretzels per customer.
    max (int): Maximum number of bretzels per customer.
    customers (int): Number of customers.
    
    Returns:
    int: Randomly drawn number of bretzels per customer.
    """
    return np.random.randint(min, max + 1, customers)


def calculate_revenue(sold_bretzels, price_per_bretzel):
    """
    Calculate total revenue from sold bretzels.
    
    Parameters:
    sold_bretzels (int): Total number of sold bretzels.
    price_per_bretzel (float): Price per bretzel.
    
    Returns:
    float: Total revenue.
    """
    return sold_bretzels * price_per_bretzel

def one_day_simulation(num_bretzels_produced, min_customer=0, max_customer=8, min_bretzels_per_customer=1, max_bretzels_per_customer=3, price_per_bretzel=1.5):
    """
    Simulate one day of bretzel sales.

    Parameters:
    num_bretzels_produced (int): Number of bretzels produced.
    min_customer (int): Minimum number of customers.
    max_customer (int): Maximum number of customers.
    min_bretzels_per_customer (int): Minimum number of bretzels per customer.
    max_bretzels_per_customer (int): Maximum number of bretzels per customer.
    price_per_bretzel (float): Price per bretzel.

    Returns:
    float: Total cost/profit for the day.
    """
    num_customers = draw_customer(min_customer, max_customer)
    bretzels_per_customer = draw_bretzel_per_costumer(min_bretzels_per_customer, max_bretzels_per_customer, num_customers)

    sold_bretzels = min(num_bretzels_produced, np.sum(bretzels_per_customer))
    revenue = calculate_revenue(sold_bretzels, price_per_bretzel)
    leftovers = num_bretzels_produced - sold_bretzels
    total_profit = - num_bretzels_produced * 1 + revenue + leftovers * 0.75

    return total_profit


if __name__ == "__main__":
    N = 10000
    max_num_bretzels_produced = 25
    profit_list = []
    for num_bretzels_produced in range(1, max_num_bretzels_produced + 1):
        total_profit = 0    
        for i in range(N):
            total_profit += one_day_simulation(num_bretzels_produced)
        list.append(total_profit / N)

    print(f"Optimal scenario: Producing {np.argmax(list) + 1} bretzels with an average profit of {max(list):.2f} euros.")

    plt.plot(range(1, max_num_bretzels_produced + 1), list)
    plt.xlabel("Number of bretzels produced")
    plt.ylabel("Average Profit")
    plt.title("Average Profit vs Number of Bretzels Produced")
    plt.grid()
    plt.show()