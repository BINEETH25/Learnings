'''
def print_nums(n):
    if n == 0:
        return
    print_nums(n - 1)
    print(n)

# Output: 1 2 3 4 5 for input n = 5
print(print_nums(n=5))
'''
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(n=5))
'''
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(n=6))
'''
'''
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]
print(reverse_string('abc'))
'''

def Binary_Search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return Binary_Search(arr, target, low, mid - 1)
    else:
        return Binary_Search(arr, target, mid+1, high)

arr=[1,2,3,4,5,6,7,8,9]
print(Binary_Search(arr,3, 0, len(arr)-1))