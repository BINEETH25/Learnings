my_array = [25, 28, 10, 25, 16, 17, 38, 24, 6, 29, 41]

lowestvalue = my_array[0]
for i in my_array:
    if i < lowestvalue:
        lowestvalue = i

print(lowestvalue)