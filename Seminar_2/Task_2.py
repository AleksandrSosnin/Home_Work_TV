import math

def poisson_probability(lmbda, k):
    return (lmbda ** k) * math.exp(-lmbda) / math.factorial(k)

# Задача 2: Расчет вероятностей для лампочек
n = 5000
p = 0.0004
lmbda = n * p

# Вероятность, что ни одна лампочка не перегорит
prob_no_burnouts = poisson_probability(lmbda, 0)

# Вероятность, что перегорят ровно 2 лампочки
prob_two_burnouts = poisson_probability(lmbda, 2)

print(f"Задача 2: Вероятность, что ни одна лампочка не перегорит: {prob_no_burnouts:.6f}")
print(f"Задача 2: Вероятность, что перегорят ровно две лампочки: {prob_two_burnouts:.6f}")
