my_array = [25, 28, 10, 16, 17, 38, 24, 6, 29, 41]

n = len(my_array)
print(n)
''' Bubble Sort Algorithm
for i in range(n - 1):
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
print(my_array)
'''
# if array is sorted and not swapping values anymore, lets optimize code to break out of loop.

for i in range(n - 1):
    Swapped = False
    for j in range(n - i - 1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]
            Swapped = True
    if not Swapped:
        break
        
print(my_array)