print('Задача 9. Выражение')


# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

x = int(input('x: '))

numerator = 1
denominator = 1

for index in range(1, 8):
    k = 2 ** index
    denominator *= x - k
    numerator *= x - (k - 1)
    if numerator == 0:
        print('result = 0')
        break
    if denominator == 0:
        print('error: division by zero')
        break
else:
    print('result:', numerator / denominator)
