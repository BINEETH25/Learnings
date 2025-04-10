'''
164. Maximum Gap
Medium
Topics
Companies
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.


Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''

def radix(nums):
    max_val = max(nums)
    exp = 1
    radixArray = [[], [], [], [], [], [], [], [], [], []]

    while max_val // exp > 0:
        
        while len(nums) > 0:
            val = nums.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)
        
        for bucket in radixArray:
            while(len(bucket)) >= 1:
                val = bucket.pop()
                nums.append(val)
        
        exp *= 10 
    return nums

def diff(nums):
    n = len(nums)
    if n > 2:
        cur_array = []
        for i in range(n-1):
            cur_val = nums[i+1] - nums[i]
            cur_array.append(cur_val)
        return max(cur_array)
    else : 
        return 0

nums = [3, 6, 9, 1]
radix(nums)
print(diff(nums))
