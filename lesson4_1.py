number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(input())
number_5 = int(input())
number_6 = int(input())
number_list_1 = [number_1, number_2, number_3]
number_list_2 = [number_4, number_5, number_6]
number_list_3 = []
for item in number_list_1:
    if item in number_list_2:
        number_list_3.append(item)
print(number_list_3)
