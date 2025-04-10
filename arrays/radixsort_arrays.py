
myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)

radixArray = [[], [], [], [], [], [], [], [], [], []]
max_val = max(myArray)
exp = 1

while max_val // exp > 0:
    
    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)
    
    exp *= 10
    
print(myArray)

''' 
#Radix Sort With Bubble Sort Sorting Implementation

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:
            if len(bucket) > 1:
                bubbleSort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixSortWithBubbleSort(myArray)
print("Sorted array:", myArray)
'''