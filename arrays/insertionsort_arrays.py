my_array = [25, 28, 10, 16, 17, 38, 24, 6, 29, 41]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    cur_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > cur_value:
            insert_index = j
    my_array.insert(insert_index, cur_value)

print(my_array)