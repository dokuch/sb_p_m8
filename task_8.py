print('Задача 8. Сумма ряда')

# Дано натуральное число n.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 

n = int(input('input N: '))
result = 1
pre = 1

for index in range(1, n + 1):
    pre *= -0.5
    result += pre

print(result)
