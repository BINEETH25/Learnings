def TSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # skipping duplicate fixed elements
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # two pointer Search
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                # skip dupplicates for left and right
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # move both points inward
                left += 1
                right -= 1
            
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result
nums =  [-1, 0, 1, 2, -1, 1]
print(TSum(nums))