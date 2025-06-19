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
'''
'''
# Insertion Sort : Buils a sorted array each element at a time by taking new element and making it to it's correct position in already sorted array
array = [8, 6, 7, 3, 2, 25, 16, 32, 1]
n = len(array)
for i in range(1, n):
    current_index = i
    current_value = array[current_index]
    for j in range(i-1, -1, -1):
        if current_value < array[j]:
            array[j + 1] = array[j]
            current_index = j
    array[current_index] = current_value
print(array)
'''
'''
# Quick Sort :  It is a divide and Conquer strategy algorithm.
    # partitions using pivot element
    # the <= pivot , elements to left side
    # the > pivot, elements to right side.
    #recursively using same logic to left and right subarrays
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [24, 14, 25, 1, 22, 11, 10, 15]
quicksort(my_array)
print("Sorted array:", my_array)
'''
'''
# Counting Sort
def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)
'''
'''
# Radix Sort :  Sorts numbers digit by digit
def Radixsort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radix_Array = [[] for i in range(10)]
        
        while len(arr) > 0:
            val = arr.pop()
            radix_index = (val // exp) % 10
            radix_Array[radix_index].append(val)
            
        for bucket in radix_Array:
            while len(bucket)>0:
                val = bucket.pop()
                arr.append(val)
        
        exp *= 10
myArray = [170, 45, 75, 90, 802, 24, 2, 66]
Radixsort(myArray)
print(myArray)
'''
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
