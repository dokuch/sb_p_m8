print('Задача 7. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('стипендия студента: '))
expenses = int(input('расходы на проживание: '))

summ = expenses

for index in range(1, 10):
    expenses *= 1.03
    summ += expenses

print('необходимо получить у родителей: ', summ - 10 * educational_grant)
