'''Нужно проверить, все ли числа в последовательности уникальны.'''

def my_first_function():
# при помощи этого модуля мы получаем рандомное число.
    from random import randint
# создаем два пустых списка с исходными элементами и список с повторяющимися элементами.
    list_number1 = []
    list_coppy_number = []
# создаем генератор случайных чисел и помещаем их в список = 50 элементам.
    while len(list_number1) < 50:
        list_number1.append(randint(1, 1000))
# проходимся по элементам сгенерированного списка и ищем повторяющиеся элементы
    for num in list_number1:
        if list_number1.count(num) >= 2:
# если мы нашли повт.элементы и их еще нет в списке list_coppy_number то мы их туда добавляем.
            if num not in list_coppy_number:
                list_coppy_number.append(num)
# далее прохолимся по элементам списка копий и выводим их на экран.
    for nums in list_coppy_number:
        print('найден повторяющийся элемент: ' + str(nums))
# если наш список с повтор.элементами остался пустым, то выводим print. В противном случае - else.
    if len(list_coppy_number) < 1:
        print('Повторяющиеся числа не найдены.')
    else:
        print('Числа в последовательности не уникальны.')
        print('\nСписок повторяющихся элементов: ' + str(list_coppy_number))
# выводим список исходных элементов на экран.
    print('Список исходных элементов: ' + str(list_number1))
# перед следующим запуском функции отчищаем списки.
    list_number1.clear
    list_coppy_number.clear
# inpat для того, что бы файл exe не закрывался после завершения программы.
    input()

my_first_function()