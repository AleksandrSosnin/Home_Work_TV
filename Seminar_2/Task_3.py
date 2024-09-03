from math import comb

# Определяем функцию для расчета биномиальной вероятности
def binomial_probability(n, k, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Задача 3: Вероятность, что орел выпадет ровно 70 раз
n = 144
k = 70
p = 0.5
prob_70_heads = binomial_probability(n, k, p)
print(f"Задача 3: Вероятность, что орел выпадет ровно 70 раз: {prob_70_heads:.6f}")
