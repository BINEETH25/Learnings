def removeElement(nums, val):
    n = len(nums)
    left = 0
    for j in range(n):
        if nums[j] != val:
            nums[left] = nums[j]
            left += 1
    return left, nums[:left]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = 2
k, nums = removeElement(nums, k)
print(k, nums)