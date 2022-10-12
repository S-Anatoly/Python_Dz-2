# -Task_1-
print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр'
      'Пример: - 6782 -> 23'
      '- 0,56 -> 11')
number = input('Введите число: ')
summ = 0
for i in range(len(number)):
    if number[i] == '.' or number[i] == ',':
        continue
    summ += int(number[i]) % 10
print(f'Сумма цифр числа {number} равна -> {summ}')

# -Task_2-
print('Напишите программу, которая принимает на вход число N '
      'и выдает набор произведений чисел от 1 до N.'
      'Пример: - пусть N = 4,'
      'тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)')
number = int(input('Введите число: '))
arr_list = []
pr_num=1
for i in range(1, number+1):
    pr_num*=i
    arr_list.append(pr_num)
print(f'Список произведений всех чисел до {number} равен -> {arr_list}')

#  -Task_3-
print('Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.'
      'Пример:'
      '- Для n = 4: {1: 2, 2: 25, 3: 2.37, 4: 2.44}, Сумма равна = 9.06')

N = int(input('Введите число: '))
arr_list = []
sum = 0
for i in range(1, N+1):
    arr_list.append(round((1+1/i)**i, 2))
for j in range(len(arr_list)):
    sum += arr_list[j]
print(f'Список -> {arr_list}, Сумма элементов -> {sum}')

# -Task_Dop-1-
print('Задайте список из N элементов, заполненных числами из промежутка [-N, N].'
      'Найдите произведение элементов на указанных позициях. '
      'Позиции хранятся в файле file.txt в одной строке одно число.')

n = int(input('Введите число: '))
list_number = []
for i in range(-n, n):
    list_number.append(i)
print(f'Список -> {list_number}')

file = open('C:\\Users\\Onotole\\Desktop\\Python =_Dz-2\\Python_Dz_2\\file.txt')
list_file = []
for line in file:
    list_file.append(int(line))
print(f'Индексы из файла -> {list_file}')
file.close()

pr_num=1
for i in range(len(list_file)):       #находим произведение
    pr_num *= list_number[list_file[i]]
print(f'Сумма произведений списка -> {list_number}, с индексами -> {list_file} равна -> {pr_num}')

# Task_Dop-2-

from random import randint

print('Перемешать список')
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Исходный список - {list}')

for i in range(len(list)):
    index_rand = randint(0, len(list)-1)
    n = list[i]
    list[i] = list[index_rand]
    list[index_rand] = n
print(f'Перемешанный список - {list}')

# Dop_Task_Work
print('Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2].'
'Надо вернуть их пересечение - [1, 2, 2, 3]'
'(порядок не важен)')
list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(f'Пересечение списков -> {list3}')