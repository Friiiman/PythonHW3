def task1():
    # Задайте список из нескольких чисел. 
    # Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

    my_list = [6, 55, 4, 73, 18, 22]
    my_sum = 0
    for i in range(1, len(my_list), 2):
        my_sum += my_list[i]
    print(my_sum)

def task2():
    # Напишите программу, которая найдёт произведение пар чисел списка. 
    # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

    from random import randint
    my_list = list()
    my_range = int(input("Введите длину списка: "))
    for _ in range(my_range):
        my_list.append(randint(-10, 10))
    print('Сформированный список: ', my_list)

    my_list_reverse = my_list[::-1]
    if len(my_list) % 2 == 0:
        my_list_first = my_list[:int(len(my_list) / 2)]
        my_list_second = my_list_reverse[:int(len(my_list) / 2)]
    else:
        my_list_first = my_list[:int(len(my_list) / 2 + 1)]
        my_list_second = my_list_reverse[:int(len(my_list) / 2 + 1)]

    my_list_mult = list()
    for index in range(len(my_list_first)):
        my_list_mult.append(int(my_list_first[index] * my_list_second[index]))
    print('Произведение пар чисел из списка: ', my_list_mult)
    
def task3():
    # Задайте список из вещественных чисел. 
    # Напишите программу, которая найдёт разницу 
    # между максимальным и минимальным значением дробной части элементов.

    from random import uniform
    my_range = int(input("Введите длину списка: "))
    my_list = [round(uniform(0, value), 2) for value in range(1, my_range + 1)]
    print('Сформированный список: ', my_list)

    max_value = 0
    min_value = 1
    for value in my_list:
        value = round(value % 1, 2)
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    print(
        'Разница между максимальным и минимальным '\
        'значением дробной части элементов: ', 
        round(max_value - min_value, 2))

def task4():
    # Напишите программу, которая будет преобразовывать десятичное число в двоичное.

    number = int(input("Введите число: "))
    print(bin(number)[2:])

def task5():
    # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

    number = int(input("Введите число: "))
    fibonacci = list()
    number_first = 1
    number_second = 1
    for _ in range(number):
        fibonacci.append(number_first)
        number_first, number_second = number_second, number_first + number_second
    number_first = 0
    number_second = 1
    for _ in range(number + 1):
        fibonacci.insert(0, number_first)
        number_first, number_second = number_second, number_first - number_second
    print(fibonacci)
        

task1()
# task2()
# task3()
# task4()
# task5()