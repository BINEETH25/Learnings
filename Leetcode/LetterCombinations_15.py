def LetterCombinations(digits):
    
    if not digits:
        return []
    
    mapping = {
        2 : 'abc',
        3 : 'def',
        4 : 'ghi',
        5 : 'jkl',
        6 : 'mno',
        7 : 'pqrs',
        8 : 'tuv',
        9 : 'wxyz'
    }
    
    result = []
    
    def backtrack(index, path):
        if len(path) == len(digits):
            result.append(path)
            return
        current_digit = int(digits[index])
        for letter in mapping[current_digit]:
            backtrack(index + 1, path + letter)
            
    backtrack(0, "")
    return result

print(LetterCombinations("24"))