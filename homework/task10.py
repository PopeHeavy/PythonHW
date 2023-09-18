# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input("Количество монеток: "))
coins = [random.randint(0, 1) for i in range(n)]
print(coins)
heads, tails = 0, 0
for i in coins:
    if i == 1:
        heads += 1
    else:
        tails += 1
if heads >= tails:
    print(tails)
else:
    print(heads)