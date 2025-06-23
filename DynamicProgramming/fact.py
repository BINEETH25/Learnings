def fact_dp(n):
    
    dp_array = [1] * (n + 1)
    
    for i in range(2, n+1):
        dp_array[i] = i * dp_array[i - 1]
    
    return dp_array[:]

print(fact_dp(5))