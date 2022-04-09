# Ввести 3 числа для определения среднего арифметического
from statistics import mean
# в numbers_list вводить свои значения
numbers_list = [16, 150, 91]
Results = mean(numbers_list)
print ("Результат:\n")
print(Results)
# Округление через round
print("Результат округления:\n")
print(round(Results, 3))
