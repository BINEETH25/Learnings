# Valid Palindrome 
# Constraints : Check if the string is alphanumeric and all the letters in lowercase.

def Valid_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "A man, a plan, a canal: Panama"
print("Valid palindrome",Valid_palindrome(s))