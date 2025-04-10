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