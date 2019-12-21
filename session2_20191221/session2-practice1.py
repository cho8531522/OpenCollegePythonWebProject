numbers = [1, 100, -1, 30, 5, 99, 45, 30, -2, -10]

max = numbers[0]
min = numbers[0]

for i in numbers:
    if i > max:
        max = i

    if i < min:
        min = i
print(max)
print(min)