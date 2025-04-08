my_array = [25, 28, 10, 16, 17, 38, 24, 6, 29, 41]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    #cur_value = my_array.pop(i)
    cur_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > cur_value:
            # optimizing by swapping the value from sorted value with index
            my_array[j + 1] = my_array[j]
            insert_index = j
        else:
            break
    #my_array.insert(insert_index, cur_value)
    my_array[insert_index] = cur_value

print(my_array)