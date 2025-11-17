import numpy as np
import math
import matplotlib.pyplot as plt
def find_lowest_index_greater_zero(Q):
    Q = np.asarray(Q)
    pos = Q > 0
    if not pos.any():
        raise ValueError("no positive entries > 0")
    i1 = int(np.argmin(np.where(pos, Q, np.inf)))
    return i1

def find_highest_index_greater_zero(Q):
    Q = np.asarray(Q)
    pos = Q > 0
    if not pos.any():
        raise ValueError("no positive entries > 0")
    j1 = int(np.argmax(np.where(pos, Q, -np.inf)))
    return j1


def alias_method_decomposition(P):
    m = np.size(P)
    q_list = []
    P_list = []
    ik_indexes = []
    jk_indexes = []
    k = 1
    q1 = np.zeros_like(P)
    i1 = find_lowest_index_greater_zero(P)
    j1 = find_highest_index_greater_zero(P)
    q1[i1] = (m - 1) * P[i1] 
    q1[j1] = 1 - q1[i1]
    q_list.append(q1)
    P_list.append((m - 1) / (m - 2) *(P - 1 / (m - 1) * q1))
    ik_indexes.append(i1)
    jk_indexes.append(j1)

    while (k < m - 2 and int(np.count_nonzero(P_list[-1])) > 2):
        k += 1
        P_last = P_list[-1]
        ik = find_lowest_index_greater_zero(P_last)
        ik_indexes.append(ik)
        jk = find_highest_index_greater_zero(P_last)
        jk_indexes.append(jk)
        q_new = np.zeros_like(P)
        q_new[ik] = (m - k) * P_list[-1][ik]
        q_new[jk] = 1 - q_new[ik]
        q_list.append(q_new)
        P_list.append((m - k) / (m - k - 1) *(P_list[-1] - 1 / (m - k) * q_new))
    
    q_list.append(P_list[-1])
    ik_indexes.append(find_lowest_index_greater_zero(P_list[-1]))
    jk_indexes.append(find_highest_index_greater_zero(P_list[-1]))

    if not np.allclose(np.asarray(P), 1 / (m - 1) * np.sum(q_list, axis=0)):
        raise ValueError("Decomposition error")
    

    return q_list, ik_indexes, jk_indexes

def sample_from_decomposition(P):
    q_list, ik_indexes, jk_indexes = alias_method_decomposition(P)
    u1 = np.random.uniform(0, 1)
    u2 = np.random.uniform(0, 1)
    m = np.size(q_list[0])
    k = np.ceil(u1 * (m - 1)).astype(int) - 1 
    ik = ik_indexes[k]
    jk = jk_indexes[k]

    if (u2 <= q_list[k][ik]):
        return ik
    else:
        return jk



if __name__ == "__main__":
    # sample a binomial(n, p) probability vector (support 0..n)
    n = 100
    p = 0.6
    k = np.arange(n + 1)
    P = np.array([math.comb(n, kk) * p**kk * (1 - p)**(n - kk) for kk in k])
    x_list = []

    for _ in range(10000):
        x_list.append(sample_from_decomposition(P))

    plt.hist(x_list, bins=range(n + 2), density=True, alpha=0.7, color='purple', edgecolor='black')
    plt.title(f'Histogram of Binomial Distribution Samples via Alias Method (n={n}, p={p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    


        