'''
print("---Fibonacci---")
prev2 = 0
prev1 = 1
num = 10
lis = [0, 1]

for fibo in range(num):
    next = prev2 + prev1
    lis.append(next)
    prev2 = prev1
    prev1 = next

print(lis)

def F(n):
    if n <=1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(10))
print("---Finding Lowest value in array---")
# Finding Lowest value in array
array = [12, 16, 25, 28, 2, 10, 6]
lowest_num = array[0]
for i in range(len(array)):
    if array[i] < lowest_num:
        lowest_num = array[i]

print(lowest_num)

print("--Bubble Sort--")
array1 = [12, 16, 25, 28, 2, 10, 6]
n = len(array1)
for i in range(n-1):
    Swapped = False
    for j in range(n - i -1):
        if array1[j] > array1[j+1]:
            array1[j], array1[j+1] = array1[j+1], array1[j]
            Swapped = True
    if not Swapped:
        break
print(array1)

print("----Selection SOrt----")
array2 = [12, 16, 25, 28, 2, 10, 6]
n = len(array2)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if array2[j] < array2[min_index]:
            min_index = j
    array2[i], array2[min_index] = array2[min_index], array2[i]
print(array2)

print("------Insertion Sort------")
array3 = [12, 16, 25, 28, 2, 10, 6]
n = len(array3)
for i in range(1, n):
    insert_index = i
    curr_val = array3[insert_index]
    for j in range(i-1, -1, -1):
        if array3[j] > curr_val:
            array3[j+1] = array3[j]
            insert_index = j
        else:
            break
    array3[insert_index] = curr_val
print(array3)
'''
'''
print("------Quick Sort------")
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

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
'''
'''
print("-----Counting Sort-----")

def coutingsort(myArray):
    max_val = max(myArray)
    count = [0] * (max_val + 1)
    while len(myArray) > 0:
        num = myArray.pop(0)
        count[num] += 1
    for i in range(len(count)):
        while count[i] > 0:
            myArray.append(i)
            count[i] -= 1
    return myArray

myArray = [2,3,0,2,3,2]
sortedarr = coutingsort(myArray)
print(sortedarr)
'''
print("-----Radix Sort-----")

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
RadixArray = [[] for i in range(10)]
max_val = max(myArray)
exp = 1

while max_val // exp > 0:
    
    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        RadixArray[radixIndex].append(val)
    
    for bucket in RadixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)
    
    exp *= 10

print(myArray)