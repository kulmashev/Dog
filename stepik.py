# X = int(input())
# H = int(input())
# M = int(input())
# b3 = X + H * 60 + M
# print(b3//60)
# print(b3%60)
# x = int(input())
# if x % 2 == 0:
#     print("Чётное!")
# else:
#     print("Не чётное!")
# a = int(input())
# b = int(input())
# if b != 0:
#     print(a/b)
# else:
#     print("Деление не возможно!")
#     b = int(input("Введите не нулевое значение: "))
#     if b == 0:
#         print("Вы не справились!")
#     else:
#         print(a/b)

# A = int(input())
# B = int(input())
# H = int(input())
# if A > H:
#     print("Недосып")
# elif H > B:
#     print("Пересып")
# else:
#     print("Это нормально")

# year = int(input())
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Високосный")
# else:
#     print("Обычный")
# a = int(input())
# b = int(input())
# c = int(input())
# p = ((a+b+c)*0.5)
# s = (p*(p-a)*(p-b)*(p-c))**0.5
# print(s)

# a = int(input())
# b = float('inf')
# if -15 < a <= 12 or 14 < a < 17 or 19 <= a < b:
#     print("True")
# else:
#     print("False")

# a = float(input())
# b = float(input())
# c = str(input())
# if c == "mod":
#     if b !=0:
#         print(a%b)
#     else:
#         print("Деление на 0!")
#
# elif c == "pow":
#     print(a**b)
# elif c == "div":
#     if b != 0:
#         print(a // b)
#     else:
#         print("Деление на 0!")
# elif c == "*":
#     print(a*b)
# elif c == "/":
#     if b != 0:
#         print(a / b)
#     else:
#         print("Деление на 0!")
# elif c == "-":
#     print(a-b)
# elif c == "+":
#     print(a+b)
# elif c == "**":
#     print(a**b)
# elif c == "%":
#     if b != 0:
#         print(a % b)
#     else:
#         print("Деление на 0!")


# x = input()
# if x == "треугольник":
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = ((a+b+c)*0.5)
#     s = (p*(p-a)*(p-b)*(p-c))**0.5
#     print(s)
# elif x == "прямоугольник":
#     a = int(input())
#     b = int(input())
#     s = a*b
#     print(s)
# elif x == "круг":
#     a = int(input())
#     print((a**2)*3.14)

# a = int(input()) # Ввод первого числа
# b = int(input()) # Ввод второго числа
# c = int(input()) # Ввод третьего числа
#
# # Нахождение максимального числа
# if a >= b and a >= c:
#     max_num = a
# elif b >= a and b >= c:
#     max_num = b
# else:
#     max_num = c
#
# # Нахождение минимального числа
# if a <= b and a <= c:
#     min_num = a
# elif b <= a and b <= c:
#     min_num = b
# else:
#     min_num = c
#
# # Нахождение оставшегося числа
# remaining_num = a + b + c - max_num - min_num
#
# # Вывод максимального, минимального и оставшегося числа
# print(max_num)
# print(min_num)
# print(remaining_num)


# Функция для сложения двух чисел
# def add(x, y):
#     return x + y
#
# # Функция для вычитания двух чисел
# def subtract(x, y):
#     return x - y
#
# # Функция для умножения двух чисел
# def multiply(x, y):
#     return x * y
#
# # Функция для деления двух чисел
# def divide(x, y):
#     return x / y
#
# print("Выберите операцию:")
# print("1. Сложение")
# print("2. Вычитание")
# print("3. Умножение")
# print("4. Деление")
#
# # Запросить ввод пользователя
# choice = input("Введите номер операции (1/2/3/4): ")
#
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))
#
# if choice == '1':
#     print(num1,"+",num2,"=", add(num1,num2))
#
# elif choice == '2':
#     print(num1,"-",num2,"=", subtract(num1,num2))
#
# elif choice == '3':
#     print(num1,"*",num2,"=", multiply(num1,num2))
#
# elif choice == '4':
#     print(num1,"/",num2,"=", divide(num1,num2))
# else:
#     print("Неверный ввод")

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
#

# dna = "sapogi"
# print(dna[1:])

# for i in 2,3,5:
#     print(i*i)

# for i in range(5,10,2):
#         print(i * i)

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print()

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
#
# print(students)

# a = [1, 2, 3]
# b = a
# # значения списка b?
#
# a[1] = 10
# # значения списка b?
#
# b[0] = 20
# # значения списка a?
#
# a = [5, 6]
# # значения списка b?
#
# print(b)

# sum = 0
# num = int(input())
#
#
# print(id(num))

