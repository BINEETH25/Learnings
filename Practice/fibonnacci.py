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
'''
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
