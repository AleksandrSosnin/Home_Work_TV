# Задача 4
# На факультеты A, B и C поступило разное количество студентов. Нужно найти вероятность того, что студент учится на факультете A, B или C, если он сдал первую сессию.

# Вероятности того, что студент учится на факультетах A, B или C
P_A = 1/4  # Вероятность, что студент с факультета A
P_B = 1/4  # Вероятность, что студент с факультета B
P_C = 1/2  # Вероятность, что студент с факультета C

# Условные вероятности сдачи сессии
P_S_A = 0.8  # Вероятность сдачи для факультета A
P_S_B = 0.7  # Вероятность сдачи для факультета B
P_S_C = 0.9  # Вероятность сдачи для факультета C

# Полная вероятность сдачи сессии
P_S = P_A * P_S_A + P_B * P_S_B + P_C * P_S_C

# Байесовские вероятности
P_A_S = (P_S_A * P_A) / P_S
P_B_S = (P_S_B * P_B) / P_S
P_C_S = (P_S_C * P_C) / P_S

print(f"Вероятность, что студент учится на факультете A: {P_A_S:.6f}")
print(f"Вероятность, что студент учится на факультете B: {P_B_S:.6f}")
print(f"Вероятность, что студент учится на факультете C: {P_C_S:.6f}")
