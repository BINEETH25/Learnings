def Combinations(n, k):
    
    if not (1 <= n <= 20) or not (1 <= k <= n):
        raise ValueError("Invalid input: Make sure 1 <= k <= n <= 20")
    
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path) # moving forward to avoid repeats
            path.pop()
    
    backtrack(1, [])
    return result

print(Combinations(4, 5))