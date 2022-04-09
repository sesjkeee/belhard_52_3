# Ввести 3 числа для определения среднего арифметического
import numpy
# метод через numpy
numbers_list = [900, -300, 587]
results = numpy.average(numbers_list)
print("Среднее значение:\n")
print(results)
print("Округление до 3его значения после запятой:\n")
print(round(results, 3))
