my_array = [25, 28, 10, 16, 17, 38, 24, 6, 29, 41]

n = len(my_array)
print(n)

for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
print(my_array)

