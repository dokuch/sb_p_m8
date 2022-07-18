print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

packed_size = 12

letter_size = int(input('input letter size: '))

if letter_size > packed_size:
    count = letter_size / (2 * packed_size)
else:
    count = 0

if count % 1 > 0:
    count = (count // 1 + 1)

print('result:', count * 2)
