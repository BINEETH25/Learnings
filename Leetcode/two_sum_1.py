'''
def Solution(arr, tar):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] == tar:
            return [left, right]
        right -= 1
    return [-1, -1]

arr = [3, 2, 4]
tar = 6

print(Solution(arr, tar))
'''

def twoSum(nums, target):
    hasc = {}
    n = len(nums)
    if len(nums) < 2 or len(nums) > 10**4:
        raise ValueError("Invalid input size")

    for i in range(n):
        complement = target - nums[i]
        if complement in hasc:
            return [hasc[complement], i]
        hasc[nums[i]] = i
        
nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
