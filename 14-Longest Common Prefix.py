#Runtime: 28 ms, faster than 87.95% of Python3 online submissions for Longest Common Prefix.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if len(strs)==0: 
            return prefix
        
        min_length_str = min(strs)
        max_length_str = max(strs)
        
        
        for i in range(len(min_length_str)):
            if min_length_str[i] == max_length_str[i]:
                prefix += min_length_str[i]
            else:
                return prefix
        
        return prefix