'''
1365. How Many Numbers Are Smaller Than the Current Number
Easy
Topics
Companies
Hint
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
'''
def counting(nums):
    new_arr = [0] * len(nums)
    for i in range(len(nums)):
        count = 0
        num = nums[i]
        for j in range(len(nums)):
            if nums[j] < num:
                count += 1
        new_arr[i] = count
    return new_arr

nums = [8, 1, 2, 2, 3]
print(counting(nums))


'''  Optimized  Solution
def counting(nums):
    count = [0] * 101  # Frequency array

    for num in nums:
        count[num] += 1

    # Prefix sum: count[i] = number of elements < i
    for i in range(1, 101):
        count[i] += count[i - 1]

    result = []
    for num in nums:
        result.append(0 if num == 0 else count[num - 1])

    return result

'''

'''My Solution in Leetcode 

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_arr = [0] * len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            new_arr[i] = count
        return new_arr


'''

'''Best Solution with Optimization with consideration of Constraints
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 101  # since 0 <= nums[i] <= 100
        for num in nums:
            count[num] += 1
        
        # compute prefix sum
        for i in range(1, 101):
            count[i] += count[i - 1]
        
        result = []
        for num in nums:
            result.append(0 if num == 0 else count[num - 1])
        
        return result

'''