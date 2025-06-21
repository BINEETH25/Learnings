def FourSum(nums, target):
    nums.sort()
    result = []
    n = len(nums)
    
    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a - 1]:
            continue
        for b in range(a+1, n -2):
            if b > a +1 and nums[b] == nums[b - 1]:
                continue
            c, d = b + 1, n - 1
            while c < d:
                s = nums[a] + nums[b] + nums[c] + nums[d]
                if s == target:
                    result.append([nums[a], nums[b], nums[c], nums[d]])
                    while c < d and nums[c] == nums[c+1]:
                        c += 1
                    while c < d and nums[d] == nums[d-1]:
                        d -= 1
                    
                    c += 1
                    d -= 1
                elif s < target:
                    c += 1
                else:
                    d -= 1
    return result

#nums = [1, 0, -1, 0, -2, 2]

print(FourSum(nums=[2, 2, 2, 2, 2], target=8))