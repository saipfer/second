# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

# for i in range (1, 6):
#     print (i, 0)

# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
# x = 0
# for i in range (10) :
#     y = int(input('введите любое число:'))
#     if y == 5: x +=1
# print('количество введенных цыфр 5: ', x)
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
...
# sum = 0
# for i in range(1,101):
#     sum+=i
#     print(sum)
...
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
# x = 1
# for i in range (1, 11):
#     x *= i
# print(x)
# Задача 5
#Вывести цифры числа на каждой строке.
# integer_number = 1234
#
# #print(integer_number%10, integer_number//10)
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10
...
# Задача 6
# Найти сумму цифр числа.
# i = 0
# sum = 0
# number = input('введите многозначное число:')
# for i in range (0, len(number)):
#     sum = sum + int(number[i])
# print(sum)
...
# Задача 7
# # # Найти произведение цифр числа.
# # # i = 0
# # # p = 1
# # # number = input('введите многозначное число:')
# # # for i in range (0, len(number)):
# # #      p = p * int(number[i])
# # # print(p)
...
#Задача 8
#Дать ответ на вопрос: есть ли среди циф числа 5?
# integer_number = 1234123452345
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#     break
#     integer_number = integer_number//10
# else: print('No')
...
# Задача 9
# Найти максимальную цифру в числе
# '''
# x = int(input('введите многозначное число:'))
# max = 0
# while x != 0:
#     if max < x % 10:
#         max = x % 10
#     x = x // 10
# print(max)
# '''
# Задача 10
# Найти количество цифр 5 в числе
# x = int(input('введите любое число:'))
# y = 0
# while x > 0:
#     if x % 10 == 5:
#         y += 1
#     x = x // 10
# print(y)