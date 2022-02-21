from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        left,right = 0,0
        n = len(nums)
        res = 0
        while(right< n-1): 
            max_index = left 
            for i in range(left,right+1):
                max_index = max(max_index,  i + nums[i])
            left = right+1
            right = max_index
            res+=1
        return res
