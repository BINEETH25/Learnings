'''
class LongestSubSequence:
    def __init__(self, s, k):
        self.s = s
        self.k = k
        self.freq_map = {}
        self.result = []
        
    def count_freq(self):
        for ch in self.s:
            if ch in self.freq_map:
                self.freq_map[ch] += 1
            else:
                self.freq_map[ch] = 1
        return self.freq_map
    
    def print_freq(self):
        for ch, freq in self.freq_map.items():
            if freq >= self.k:
                print(f'{ch}', freq)
                
    def build_result(self):
        for ch in s:
            if self.freq_map.get(ch, 0) >= self.k:
                self.result.append(ch)
        return ''.join(self.result)

s = "letsleetcode"
k = 2
sequence = LongestSubSequence(s, k)
sequence.count_freq()
sequence.print_freq()
result_string = sequence.build_result()
print(result_string)
'''
'''
def get_all_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.append(s[i:j])
    return substrings

result = "letleete"
print(get_all_substrings(result))
'''

'''
def get_subsequences(s):
    result = []

    def backtrack(index, path):
        if index == len(s):
            if path:  # to skip empty string
                result.append(''.join(path))
            return
        # Include current character
        path.append(s[index])
        backtrack(index + 1, path)
        path.pop()
        # Exclude current character
        backtrack(index + 1, path)

    backtrack(0, [])
    return result

# Example
s = "lete"
print(get_subsequences(s))
'''
'''
from collections import Counter
from itertools import product

def count_occurrences(candidate, s):
    i, count = 0, 0
    for ch in s:
        if ch == candidate[i]:
            i += 1
            if i == len(candidate):
                count += 1
                i = 0
        if count >= 2:
            return True
    return False

def find_subsequences_with_length_k(s, min_len=3):
    freq = Counter(s)
    valid_chars = [ch for ch in freq if freq[ch] >= 2]
    results = []

    for length in range(min_len, 7):  # 7 is safe upper bound for small s
        for cand in product(valid_chars, repeat=length):
            cand_str = ''.join(cand)
            if count_occurrences(cand_str, s):
                results.append(cand_str)
    results.sort()
    return results[0]

s = 'letleete'
print(find_subsequences_with_length_k(s))
'''
class Solution:
    def generateOrderedSubsequencesWithFreq(self, s: str, k: int):
        freq_map = {}
        path = []

        def backtrack(start):
            if len(path) == 3:
                subseq = ''.join(path)
                freq_map[subseq] = freq_map.get(subseq, 0) + 1
                return

            for i in range(start, len(s)):
                path.append(s[i])
                backtrack(i + 1)  # Only explore forward characters
                path.pop()

        backtrack(0)

        return freq_map

# Example usage:
sol = Solution()
s = "letleete"
k = 2
print(sol.generateOrderedSubsequencesWithFreq(s, k))
