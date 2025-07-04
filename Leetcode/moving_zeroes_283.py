'''
283. Move Zeroes
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
'''
'''

nums = [0, 1, 0, 3, 12]
#nums = [0]
n = len(nums)

for i in range(n):
    Swapped = False
    for j in range(n - i - 1):
        if nums[j] == 0:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            Swapped = True
    if not Swapped:
        break
print(nums)
'''

''' Optimized Code
for num in nums:
    if num != 0:
        nums[insert_pos] = num
        insert_pos += 1

# Fill remaining positions with 0
for i in range(insert_pos, len(nums)):
    nums[i] = 0

print(nums)

# Time complexity: O(n)

# Space complexity: O(1)
'''
def movingZeroes(nums):
    right = -1
    n = len(nums)
    for i in range(-1,-n-1, -1):
        if nums[i] != 0:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
    return nums
nums = [3, 12, 5, 6, 7, 8, 9, 11, 12, 14, 0, 1, 0, 0, 0, 0, 6]
print(movingZeroes(nums))