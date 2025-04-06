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
''' Fibonacci Using Recursion
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

'''

# Finding N th Fibonacci Number

def F(n):
    if n <= 1 :
        return 1
    else:
        return F(n - 1) + F(n - 2)

print(F(7))