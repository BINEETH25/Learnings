def removeDuplicates(nums):
    n = len(nums)
    left = 0
    for j in range(n):
        if nums[j] != nums[left]:
            left += 1
            nums[left] = nums[j]
    
    return left+1, nums[:left +1]
nums = [0,0,1,1,1,2,2,3,3,4]
k, nums = removeDuplicates(nums)
print(k, nums)