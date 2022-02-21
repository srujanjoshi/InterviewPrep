from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goalpost= n -1 
        for i in range(n-1, -1, -1):
            if(nums[i]+i>=goalpost):
                goalpost=i
            
        
        return goalpost == 0

