import math

def combinations(n, k):
    return math.comb(n, k)

# Задача 1а: Все карты - крести
prob_all_clubs = combinations(13, 4) / combinations(52, 4)
print(f"Задача 1а: Вероятность того, что все карты крести: {prob_all_clubs:.6f}")

# Задача 1б: Хотя бы один туз
prob_no_aces = combinations(48, 4) / combinations(52, 4)
prob_at_least_one_ace = 1 - prob_no_aces
print(f"Задача 1б: Вероятность того, что хотя бы один туз: {prob_at_least_one_ace:.6f}")

# Задача 2: Открыть дверь с первой попытки
prob_open_door = 1 / combinations(10, 3)
print(f"Задача 2: Вероятность открыть дверь с первой попытки: {prob_open_door:.6f}")

# Задача 3: Все детали окрашены
prob_all_colored = combinations(9, 3) / combinations(15, 3)
print(f"Задача 3: Вероятность того, что все извлеченные детали окрашены: {prob_all_colored:.6f}")

# Задача 4: Оба билета выигрышные
prob_both_win = combinations(2, 2) / combinations(100, 2)
print(f"Задача 4: Вероятность того, что оба билета выигрышные: {prob_both_win:.6f}")
