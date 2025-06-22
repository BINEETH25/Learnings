def subsets(nums):
    
    if not (1 <= len(nums) <= 10) or not all(-10 <=num <=10 for num in nums):
        raise ValueError("Invalid")
    
    result = []
    nums.sort()
    
    def backtrack(start, path):
        result.append(path[:])  # add current subset

        for i in range(start, len(nums)):
            # Choose
            if i > start and nums[i] == nums[i - 1]:
                continue
            
            path.append(nums[i])
            # Explore
            backtrack(i+1 , path)
            # Un-choose
            path.pop()
    
    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))