# Runtime: 64 ms, faster than 50.85% of Python3 online submissions for Palindrome Number.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x == 0:
            return True
        elif (x < 0) or (x%10 == 0):
            return False
        
        input_x = x
        reverse = 0
        while x >= 10:
            reverse = (reverse * 10) + (x % 10)
            x = int(x / 10)
        
        reverse = (reverse*10) + x
        
        if input_x == reverse:
            return True
        else:
            return False
        