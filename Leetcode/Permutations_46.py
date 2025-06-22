def Permutations(nums):
    result = []
    used = [False] * len(nums)
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue  # skip already-used elements

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False  # backtrack

    backtrack([])
    return result

print(Permutations([1, 2]))
