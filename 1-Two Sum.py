class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sub_target = {}
        
        for index,value in enumerate(nums):
            sub_target = target - value
            if sub_target not in dict_sub_target:
                dict_sub_target[value] = index
            else:
                return [dict_sub_target[sub_target],index]