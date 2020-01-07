# Runtime: 36 ms, faster than 94.98% of Python3 online submissions for Roman to Integer.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        
        symbol_value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
                       #'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        prev = symbol_value[s[0]]
        output = prev
        
        for i in s[1:]:
            temp = symbol_value[i]
            if temp <= prev:
                output += temp
            else:
                output += temp - prev*2
            prev = temp
        
        """
        count = 0
        while count < len(s):
            if count != len(s)-1:
                temp = s[count] + s[count+1]
                if temp in symbol_value:
                    output += symbol_value[temp]
                    count += 2
                else:
                    output += symbol_value[s[count]]
                    count += 1
                print(output)
            else:
                output+= symbol_value[s[count]]
                count += 1
        """       
        return output