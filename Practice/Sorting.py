class SortingAlgorithms:
    def __init__(self) -> None:
        pass
    
    # Bubble Sort : Compares next value and swaps, if it is lower than the current value
    def bubblesort(self, arr):
        n = len(arr)
        for i in range(n):
            Swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[i]
                    Swapped = True
            if not Swapped:
                break
        return arr
    
    # Selection Sort : Finds lowest value and swaps to starting side
    def selectionsort(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    
    # Quick Sort : divides the array by pivot index and sorts left side values and right side values
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
    
    def quicksort(self, arr, low = 0, high = None):
        n = len(arr) - 1
        for i in range(n):
            if high is None:
                high = len(arr) - 1
            if low < high:
                pivot_index = self.partition(arr, low, high)
                self.quicksort(arr, low, pivot_index - 1)
                self.quicksort(arr, pivot_index +1, high)
        
        return arr
    
    def countingsort(self, arr):
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
    
    def radixsort(self, arr):
        
        max_val = max(arr)
        exp = 1
        radixArray = [[] for i in range(10)]
        while max_val // exp > 0:
            
            while len(arr) > 0:
                val = arr.pop()
                radixIndex = (val // exp) % 10
                radixArray[radixIndex].append(val)
                
            for bucket in radixArray:
                while len(bucket) > 0:
                    val = bucket.pop()
                    arr.append(val)
                    
            exp *= 10
        return arr
    
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        
        sortedLeft = self.mergesort(leftHalf)
        sortedRight = self.mergesort(rightHalf)
        return self.merge(sortedLeft, sortedRight)
    
    def merge(self, left, right):
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
    

def linearSearch(arr, target_val):
    
    for i in range(len(arr)):
        if arr[i] == target_val:
            return i
    return -1

def binarysearch(arr, target_val):
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target_val:
            return mid
        if arr[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1
    return -1


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
array1 = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
myArray1 = [170, 45, 75, 90, 802, 24, 2, 66]
arraysorting = SortingAlgorithms()
#print(arraysorting.bubblesort(my_array))       # O(n^2)
#print(arraysorting.selectionsort(my_array))    # O(n^2)
#print(arraysorting.quicksort(my_array))    # O(nlogn)
#print(arraysorting.countingsort(array1))   # O(n + k) k --> no.of repeating numbers
#print(arraysorting.radixsort(myArray1))    # O(n.k)  k --> no.of digits in highest value
print(arraysorting.mergesort(myArray1))     # O(n.logn)


result = linearSearch(my_array, target_val=11)    # O(n)

if result != -1:
    print('found')
else:
    print('not found')


search = [2, 24, 45, 66, 75, 90, 170, 802]
binary  = binarysearch(search, target_val = 24)
print(binary)


