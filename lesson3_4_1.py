# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
number_0 = int(input())
number_1 = int(input())
number_2 = int(input())
positive = f'Колличество положительнных: {(number_0 > 0) + (number_1 > 0) + (number_2 > 0)}'
negative = f'Колличество отрицательных:{(number_0 < 0) + (number_1 < 0) + (number_2 < 0)}'
print(positive)
print(negative)
