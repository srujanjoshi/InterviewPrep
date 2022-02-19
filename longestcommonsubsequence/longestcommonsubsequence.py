class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text2)+1)]
        
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1 , -1 ):
                if(text1[i]==text2[j]):
                    dp[i][j]= (1 + dp[i+1][j+1])
                else: 
                    dp[i][j]= max(dp[i][j+1], dp[i+1][j])
        
        return dp[0][0]

s= Solution()

print(s.longestCommonSubsequence('abcba', 'abcbcba'))
        