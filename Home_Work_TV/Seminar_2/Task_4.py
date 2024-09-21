from math import comb  # Импортируем функцию для вычисления комбинаций

# Задача 4: Вероятности для мячей

# Вероятности для первого ящика
prob_1_all_white = comb(7, 2) / comb(10, 2)  # Все белые из первого ящика
prob_1_not_white = comb(3, 2) / comb(10, 2)  # Все не белые из первого ящика

# Вероятности для второго ящика
prob_2_all_white = comb(9, 2) / comb(11, 2)  # Все белые из второго ящика
prob_2_not_white = comb(2, 2) / comb(11, 2)  # Все не белые из второго ящика

# 1. Вероятность того, что все мячи белые
prob_all_white = prob_1_all_white * prob_2_all_white

# 2. Вероятность, что ровно два мяча белые
prob_two_white = (
    prob_1_all_white * (1 - prob_2_all_white) +  # оба белые из первого, ни одного из второго
    (1 - prob_1_all_white) * prob_2_all_white +  # оба белые из второго, ни одного из первого
    prob_1_all_white * prob_2_all_white          # оба белые из обоих ящиков
)

# 3. Вероятность, что хотя бы один мяч белый
prob_at_least_one_white = 1 - (prob_1_not_white * prob_2_not_white)

print(f"Задача 4: Вероятность, что все мячи белые: {prob_all_white:.6f}")
print(f"Задача 4: Вероятность, что ровно два мяча белые: {prob_two_white:.6f}")
print(f"Задача 4: Вероятность, что хотя бы один мяч белый: {prob_at_least_one_white:.6f}")
