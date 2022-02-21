class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp= [[] for i in range(n+1)]
        dp[n]=[""] 
        mapping = {}
        #Generate character mapping 
        for i in range(1,27): 
            c = chr(i + 64)
            mapping[str(i)]=c

        for i in range (n-1, -1, -1):
            if s[i]=="0":
                dp[i]=[]
                continue
            for code in dp[i+1]:
                dp[i].append(mapping[s[i]]+code)
            if(i < n-1 and s[i:i+2] in mapping.keys()):
                for code in dp[i+2]:
                    dp[i].append(mapping[s[i:i+2]]+code)
        return len(dp[0])
    

print(Solution().numDecodings("06"))
