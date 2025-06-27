from collections import deque
from typing import List

class SlidingWindowMax:
    def SlidingWindow(self, nums : List[int] , k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        result = [] # Result List
        q = deque() # stores indexes not values
        
        for i in range(len(nums)):
            # first remove indexes that out of the window
            while q and q[0] < i - k + 1:
                q.popleft()
            
            # Lets maintain Decreasing Order in Queue, By Storing Max Value to left.
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            
            # Adding Current index
            q.append(i)
            
            # Adding max value to first of index, once queue is formed.
            if i >= k - 1:
                result.append(nums[q[0]])
        
        return result

Windowmax = SlidingWindowMax()


nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(Windowmax.SlidingWindow(nums, k))