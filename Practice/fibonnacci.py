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
'''
print("------Insertion Sort------")
array3 = [12, 16, 25, 28, 2, 10, 6]
n = len(array3)
for i in range(1, n):
    insert_index = i
    curr_value = array3[i]
    for j in range(i-1, -1, -1):
        if array3[j] > curr_value:
            array3[j+1] = array3[j]
            insert_index = j
        else:
            break
    array3[insert_index] = curr_value
print(array3)