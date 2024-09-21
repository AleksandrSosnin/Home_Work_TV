# Задача 1
# Даны значения зарплат выпускников. Нужно посчитать среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий.

salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# 1. Среднее арифметическое
mean_salary = sum(salaries) / len(salaries)

# 2. Смещенная дисперсия
variance_biased = sum((x - mean_salary) ** 2 for x in salaries) / len(salaries)

# 3. Несмещенная дисперсия
variance_unbiased = sum((x - mean_salary) ** 2 for x in salaries) / (len(salaries) - 1)

# 4. Среднее квадратичное отклонение
std_dev = variance_unbiased ** 0.5

print(f"Среднее арифметическое: {mean_salary:.2f}")
print(f"Смещенная дисперсия: {variance_biased:.2f}")
print(f"Несмещенная дисперсия: {variance_unbiased:.2f}")
print(f"Среднее квадратичное отклонение: {std_dev:.2f}")
