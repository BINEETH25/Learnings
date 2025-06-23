'''
def lengthOfLIS_n2(nums):
    n = len(nums)
    dp = [1] * n  # Each element is at least a subsequence of length 1

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lengthOfLIS_n2(nums=[0, 1, 0, 3, 2, 3]))
'''

def lengthOfLIS_with_sequence(nums):
    n = len(nums)
    dp = [1] * n            # Stores length of LIS ending at each i
    prev = [-1] * n         # Stores previous index in LIS for each i

    max_len = 1
    max_index = 0

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i

    # Now reconstruct the sequence
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]

    lis.reverse()
    return max_len, lis

print(lengthOfLIS_with_sequence(nums=[0, 1, 0, 3, 2, 3, 2]))