def lengthOfLongestSubstring(s):
    maxLen = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
        maxLen = max(maxLen, len(seen))
    return maxLen

print(lengthOfLongestSubstring(s='abcabcbb'))