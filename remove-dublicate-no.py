import math

numbers = [1, 2, 3, 4, 4, 5, 5, 6]
unique_numbers = [x for i, x in enumerate(numbers) if not math.isnan(numbers[i:].index(x))]
print(unique_numbers)

# unique_num = list(set(numbers))
# print(unique_num)