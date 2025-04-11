def LinearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

my_array = [25, 28, 10, 16, 17, 38, 24, 6, 29, 41]
targetVal = 6

result = LinearSearch(my_array, targetVal)

if result != -1:
    print("Value", targetVal, "found at index : ", result)
else:
    print("Value", targetVal, "not found in array")


