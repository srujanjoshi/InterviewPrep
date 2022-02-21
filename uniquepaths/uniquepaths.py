class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0] * n for i in range(m)]
        
        dp[m-1][n-1]=1         
        for i in range(m-1,-1, -1):
            for j in range(n-1, -1, -1):
                if(i<m-1 and j<n-1):
                    dp[i][j]= dp[i+1][j] + dp[i][j+1]
                elif(j<n-1):
                    dp[i][j]= dp[i][j+1]
                elif(i<m-1):
                    dp[i][j]= dp[i+1][j]
        
        return dp[0][0]
         

print(Solution().uniquePaths(3,7))