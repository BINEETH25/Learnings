
def Combination_sum(candidates, target):
    result = []
    
    def backtrack(start, path, total):
        
        if total == target:
            result.append(path[:])
            return []
        if total > target:
            return # Pruning Path
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()
    
    backtrack(0, [], 0)
    return result

candidates = [2, 2, 3, 5]
print(Combination_sum(candidates, target = 8))

'''
def combinationSum(candidates, target):
        res = []

        def rec(start, cur, target):
            if target == 0:
                res.append(cur[::])
                return

            for choice in range(start, len(candidates)):
                if candidates[choice] <= target:
                    cur.append(candidates[choice])
                    rec(choice, cur, target - candidates[choice])
                    cur.pop()
        rec(0, [], target)
        return res
candidates = [2, 5, 6]
print(combinationSum(candidates, target=4))
'''