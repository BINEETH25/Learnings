prev = 0
cur = 1

print(prev)
print(cur)

''' fibonacci using for loop
for i in range(10):
    new = prev + cur
    print(new)
    prev = cur
    cur = new
    
'''

count = 2

def fibonacci(previous, current):
    global count
    if count <= 10:
        newf = previous + current
        print(newf)
        previous = current
        current = newf
        count += 1
        fibonacci(previous, current)
    else:
        return

fibonacci(0, 1)


