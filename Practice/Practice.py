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