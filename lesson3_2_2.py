# Ввести 3 числа для определения среднего арифметического
from statistics import mean
# методом statistics.sum
numbers_list = [900, -300, 587]
sum_numbers_list = sum(numbers_list)
results = sum_numbers_list/len(numbers_list)
print("Среднее значение:\n")
print(results)
print("Округление до 3его значения после запятой:\n")
print(round(results, 3))
