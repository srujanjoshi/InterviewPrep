
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0 
        right = len(nums)-1 
        i = 0
        while(i<=right):
            if nums[i] == 2: 
                #If we find a 2, swap nums[i] and nums[right]
                nums[i], nums[right] = nums[right], nums[i]
                right-=1
                continue
            if nums[i] == 0:
                #If we find a 0, swap nums[i] and nums[left]
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
            i+=1
        return nums
print(Solution().sortColors([2,0,2,1,1,0]))

print(Solution().sortColors([2,0,1]))


[0,0,2,2,1,1]

[0,0,1,1,2,2]