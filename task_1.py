numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
miss_index = 4
miss_number = (sum(numbers[:miss_index]) + sum(numbers[miss_index + 1:])) / len(numbers)
numbers[miss_index] = miss_number

print("Измененный список:", numbers)


