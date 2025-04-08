my_array = [25, 28, 10, 16, 17, 38, 24, 6, 29, 41]

n = len(my_array)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    #min_value = my_array.pop(min_index)
    #my_array.insert(i, min_value)
    # Insteading popping the lowest value from the array and inserting to the front.
    # Lets swap with first value with lowest value index.
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print(my_array)