# Ввести 3 числа для определения среднего арифметического
from statistics import mean
# в numbers_list вводить свои значения
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

numbers_list = [number_1, number_2, number_3]
Results = mean(numbers_list)
print ("Результат:\n")
print(Results)
# Округление через round
print("Результат округления:\n")
print(round(Results, 3))
