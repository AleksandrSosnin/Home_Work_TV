from math import comb

def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Задача 1: Вероятность попадания ровно 85 раз
n = 100
k = 85
p = 0.8
prob_85_hits = binomial_probability(n, k, p)
print(f"Задача 1: Вероятность попасть ровно 85 раз: {prob_85_hits:.6f}")
