numbers = [1, 2, 3, 4]
numbers_double = []

for a in numbers:
    numbers_double.append(a * 2)

print(numbers_double)

numbers_double2 = [number * 2 for number in numbers]
print(numbers_double2)