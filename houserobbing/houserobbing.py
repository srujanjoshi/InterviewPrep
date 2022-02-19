class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp=[0]*n
        
        for i in range(n):
            if(i==0):
                dp[i]=nums[0]
            elif(i==1):
                dp[i]= max(nums[0],nums[1])
            elif(i==2):
                dp[i]= max(nums[2]+nums[0],nums[1])
            if(i>=3):
                dp[i]= max(dp[i-2]+nums[i], dp[i-3]+nums[i-1])

        return dp[n-1]

