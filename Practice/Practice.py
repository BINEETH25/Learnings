'''
# Bubble Sort --> Adaptive, Stable.
array = [8, 8, 7, 3, 2]
n = len(array)
for i in range(n-1):
    Swapped = False
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            Swapped = True
    if not Swapped:
        break
print(array)
# Time Complexity :
#       Best Case : O(n)
#       Worst Case: O(n^2)
'''
# Selection Sort : repeatedly finding the minimum element from the unsorted part to moving it to the sorted part.
array = [8, 6, 7, 3, 2, 25, 16, 32, 1]
n = len(array)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)
# Time Complexity : O(n^2)
