print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры два числа a, b и c,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

count = 0
summ = 0

for index in range(a, b + 1):
    if index % c == 0:
        summ += index
        count += 1

if count == 0:
    print('Error. Division by zero')
else:
    print('avg:', summ / count)
