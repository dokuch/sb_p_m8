print('Задача 9. Выражение')


# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

x = int(input('x: '))

if 1 <= x <= 64:
    if x % 2 == 0:
        print('error: division by zero')
    else:
        print('result: 0')
else:
    numerator = 1
    denominator = 1

    for index in range(1, 65):
        if index % 2 == 0:
            denominator *= (x - index)
            print('index', index, 'znam', denominator)
        else:
            numerator *= (x - index)
            print('index', index, 'chis', numerator)

    if denominator == 0:
        print('error: division by zero')
    else:
        print('result:', numerator / denominator)
