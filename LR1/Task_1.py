numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = 0
unique_numbers = set(numbers)
sum_of_unique_numbers = sum(unique_numbers)
count_of_unique_numbers = len(unique_numbers)
average_of_unique_numbers = sum_of_unique_numbers / count_of_unique_numbers
numbers[4] = average_of_unique_numbers
print("Измененный список:", numbers)
