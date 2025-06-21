def kSum(nums, target, k, start):
    res = []
    if k == 2:
        # Base case: two pointers
        left, right = start, len(nums) - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr < target:
                left += 1
            else:
                right -= 1
    else:
        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            for subset in kSum(nums, target - nums[i], k - 1, i + 1):
                res.append([nums[i]] + subset)
    return res

def fiveSum(nums, target):
    nums.sort()
    return kSum(nums, target, 5, 0)

# Example:
print(fiveSum([1, 0, -1, 0, -2, 2, 3], target=3))
