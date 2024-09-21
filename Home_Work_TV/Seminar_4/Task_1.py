import numpy as np
import scipy.stats as stats

# Задача 1: Найти среднее значение и дисперсию для случайной величины A с равномерным распределением на (200, 800]
a_A = 200
b_A = 800

# Среднее значение
mean_A = (a_A + b_A) / 2

# Дисперсия
var_A = ((b_A - a_A) ** 2) / 12

print(f"Задача 1: Среднее значение A = {mean_A}, Дисперсия A = {var_A}")

# Задача 2: Найти правую границу величины B и ее среднее значение
a_B = 0.5
var_B = 0.2

# Дисперсия для равномерного распределения: (b - a)^2 / 12 = var_B
b_B = np.sqrt(12 * var_B) + a_B

# Среднее значение
mean_B = (a_B + b_B) / 2

print(f"Задача 2: Правая граница B = {b_B}, Среднее значение B = {mean_B}")

# Задача 3: Найти M(X), D(X), std(X) для нормального распределения X
# Плотность распределения f(x) = (1 / (4 * sqrt(2pi))) * exp((-(x+2)**2) / 32)
# Стандартная форма нормального распределения f(x) = (1 / (sigma * sqrt(2pi))) * exp(-(x - mu)**2 / (2 * sigma^2))
mu_X = -2  # M(X)
sigma_X = 4  # std(X)

# M(X), D(X), std(X)
mean_X = mu_X
var_X = sigma_X ** 2
std_X = sigma_X

print(f"Задача 3: M(X) = {mean_X}, D(X) = {var_X}, std(X) = {std_X}")

# Задача 4: Рост населения города X имеет нормальное распределение с M=174 см и std=8 см
mu_height = 174
std_height = 8

# а) Вероятность, что рост > 182 см
p_more_182 = 1 - stats.norm.cdf(182, mu_height, std_height)

# б) Вероятность, что рост > 190 см
p_more_190 = 1 - stats.norm.cdf(190, mu_height, std_height)

# в) Вероятность, что рост от 166 см до 190 см
p_166_to_190 = stats.norm.cdf(190, mu_height, std_height) - stats.norm.cdf(166, mu_height, std_height)

# г) Вероятность, что рост от 166 см до 182 см
p_166_to_182 = stats.norm.cdf(182, mu_height, std_height) - stats.norm.cdf(166, mu_height, std_height)

# д) Вероятность, что рост от 158 см до 190 см
p_158_to_190 = stats.norm.cdf(190, mu_height, std_height) - stats.norm.cdf(158, mu_height, std_height)

# е) Вероятность, что рост не выше 150 см или не ниже 190 см
p_not_150_or_more_190 = stats.norm.cdf(150, mu_height, std_height) + (1 - stats.norm.cdf(190, mu_height, std_height))

# ё) Вероятность, что рост не выше 150 см или не ниже 198 см
p_not_150_or_more_198 = stats.norm.cdf(150, mu_height, std_height) + (1 - stats.norm.cdf(198, mu_height, std_height))

# ж) Вероятность, что рост ниже 166 см
p_less_166 = stats.norm.cdf(166, mu_height, std_height)

print(f"Задача 4а: Вероятность, что рост > 182 см: {p_more_182}")
print(f"Задача 4б: Вероятность, что рост > 190 см: {p_more_190}")
print(f"Задача 4в: Вероятность, что рост от 166 см до 190 см: {p_166_to_190}")
print(f"Задача 4г: Вероятность, что рост от 166 см до 182 см: {p_166_to_182}")
print(f"Задача 4д: Вероятность, что рост от 158 см до 190 см: {p_158_to_190}")
print(f"Задача 4е: Вероятность, что рост не выше 150 см или не ниже 190 см: {p_not_150_or_more_190}")
print(f"Задача 4ё: Вероятность, что рост не выше 150 см или не ниже 198 см: {p_not_150_or_more_198}")
print(f"Задача 4ж: Вероятность, что рост ниже 166 см: {p_less_166}")

# Задача 5: На сколько сигм отклоняется рост 190 см от математического ожидания M(X) = 178 см и D(X) = 25
mu_population = 178
std_population = np.sqrt(25)  # std = sqrt(D)

# Отклонение в сигмах
sigma_deviation = (190 - mu_population) / std_population

print(f"Задача 5: Отклонение в сигмах = {sigma_deviation}")
