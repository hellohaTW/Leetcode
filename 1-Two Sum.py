# Runtime: 72 ms, faster than 36.36% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 10.23% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sub_target = {}
        
        for index,value in enumerate(nums):
            sub_target = target - value
            if sub_target not in dict_sub_target:
                dict_sub_target[value] = index
            else:
                return [dict_sub_target[sub_target],index]