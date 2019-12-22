class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        elif x < 0:
            ans = int('-' + str(x)[-1:0:-1])
        
        return ans if -2147483648 < ans < 2147483647 else 0