class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp= [0]*(n+1)
        dp[n]= 1
        mapping = {}
        #Generate character mapping 
        for i in range(1,27): 
            c = chr(i + 64)
            mapping[str(i)]=c

        for i in range (n-1, -1, -1):
            if s[i]=="0":
                dp[i]=0
                continue
            dp[i]= dp[i+1]
            if(i < n-1 and s[i:i+2] in mapping.keys()):
                dp[i]+=dp[i+2]
        return dp[0]
    

print(Solution().numDecodings("06"))
