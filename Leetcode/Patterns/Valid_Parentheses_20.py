class Valid_Parentheses:
    def valid(self, s) --> bool:
        
        dict = {
            1: (),
            2: {},
            3: []
        }
        count = 0
        for ch in s:
            count[ch] += value

s = "()[]{}"

Check = Valid_Parentheses()
print(Check.valid(s))