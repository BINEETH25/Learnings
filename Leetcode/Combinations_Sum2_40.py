def Combinations_Sum(candidates, target):
    result_map = {}
    result_index = [0]
    candidates.sort()
    # Storing results in hashmap
    
    def backtrack(start, path, total):
        
        if total == target:
            result_map[result_index[0]] = path[:]
            result_index[0] += 1
            return
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i+1, path, total + candidates[i])
            path.pop()
            
    backtrack(0, [], 0)
    return result_map
        
candidates = [10,1,2,7,6,1,5]
print(Combinations_Sum(candidates, target = 8))