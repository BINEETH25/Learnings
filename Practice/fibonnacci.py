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