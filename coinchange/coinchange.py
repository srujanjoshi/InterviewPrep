class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[-1]*(amount+1) 
        dp[0]=0

        for i in range(1,amount+1):
            opt = sys.maxsize
            for coin in coins:
                if(i-coin>=0 and dp[i-coin]>=0):
                    opt= min(opt,dp[i-coin])
            if(opt<sys.maxsize):
                dp[i]=1+opt
        
        return dp[amount]