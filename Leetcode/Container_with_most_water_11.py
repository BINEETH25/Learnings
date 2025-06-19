def mostWater(nums):
    max_area = 0
    left = 0
    right = len(nums) - 1
    while left < right:
        width = right - left
        area = min(nums[left], nums[right]) * width
        max_area = max(max_area, area)
        
        if nums[left] < nums[right]:
            left += 1
        else:
            right -=1
    return max_area
nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(mostWater(nums))

