import numpy as np
import matplotlib.pyplot as plt

def draw_customer(min, max):
    return np.random.randint(min, max + 1)


def draw_bretzel_per_costumer(min, max, customers):
    return np.random.randint(min, max + 1, customers)


def calculate_revenue(sold_bretzels, price_per_bretzel):
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


def pdf_bretzels_per_day(k, pdf0, pdf1, pdf2):
    # recursively calculate the pdf of bretzels sold per day through P(X=k) = 1/3 * P(X=k-1) + 1/3 * P(X=k-2) + 1/3 * P(X=k-3)
    if k == 0:
        return pdf0
    elif k == 1:
        return pdf1
    elif k == 2:
        return pdf2
    else:
        return (pdf_bretzels_per_day(k - 1, pdf0, pdf1, pdf2) +
                pdf_bretzels_per_day(k - 2, pdf0, pdf1, pdf2) +
                pdf_bretzels_per_day(k - 3, pdf0, pdf1, pdf2)) / 3
    
def compute_cdf(pdf_values):
    cdf_values = np.cumsum(pdf_values)
    return cdf_values

if __name__ == "__main__":
    N = 10000
    max_num_bretzels_produced = 24
    profit_list = []
    # for num_bretzels_produced in range(1, max_num_bretzels_produced + 1):
    #     total_profit = 0    
    #     for i in range(N):
    #         total_profit += one_day_simulation(num_bretzels_produced)
    #     list.append(total_profit / N)

    # print(f"Optimal scenario: Producing {np.argmax(list) + 1} bretzels with an average profit of {max(list):.2f} euros.")

    # plt.plot(range(1, max_num_bretzels_produced + 1), list)
    # plt.xlabel("Number of bretzels produced")
    # plt.ylabel("Average Profit")
    # plt.title("Average Profit vs Number of Bretzels Produced")
    # plt.grid()
    # plt.show()

    # PDF calculation
    pdf_values = []
    for k in range(0, max_num_bretzels_produced + 1):
        pdf_k = pdf_bretzels_per_day(k, 1/9, 1/27, 4/81)
        pdf_values.append(pdf_k)
    
    print(np.sum(pdf_values))  # should be 1
    plt.bar(range(0, max_num_bretzels_produced + 1), pdf_values)
    plt.xlabel("Number of Bretzels Sold")
    plt.ylabel("Probability")
    plt.title("PDF of Bretzels Sold per Day")
    plt.grid()
    plt.show()

    cdf_values = compute_cdf(pdf_values)
    plt.plot(range(0, max_num_bretzels_produced + 1),
                cdf_values, marker='o')
    plt.xlabel("Number of Bretzels Sold")
    plt.ylabel("Cumulative Probability")
    plt.title("CDF of Bretzels Sold per Day")
    plt.grid()
    plt.show()

