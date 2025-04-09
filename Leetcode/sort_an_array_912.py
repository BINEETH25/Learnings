'''
912. Sort an Array
Medium
Topics
Companies
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''
def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        
    nums[i+1], nums[high] = nums[high], nums[i + 1]
    return i+1

def quicksort(nums, low = 0, high = None):
    if high is None:
        high = len(nums) - 1
    
    if low < high:
        pivot_index = partition(nums, low, high)
        quicksort(nums, low, pivot_index-1)
        quicksort(nums, pivot_index+1, high)

nums = [5,1,1,2,0,0]

quicksort(nums)
print(nums)

''' Leetcode Solution, but not passed all testcases
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums, low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i + 1]
            return i+1

        def quicksort(nums, low = 0, high = None):
            if high is None:
                high = len(nums) - 1
            
            if low < high:
                pivot_index = partition(nums, low, high)
                quicksort(nums, low, pivot_index-1)
                quicksort(nums, pivot_index+1, high)

        quicksort(nums)
        return nums

'''