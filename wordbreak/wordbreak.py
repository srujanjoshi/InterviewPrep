from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n= len(s)
        dp = [False]*n+1
        dp[n]=True
        dictionary= set()
        for word in wordDict: 
            dictionary.add(word)
        for i in range(n-1, -1, -1):
            valid = False
            for j in range(i, n):
                sub_chunk= s[i:j+1]
                if sub_chunk in dictionary: 
                    valid = valid or dp[j+1]
            dp[i]= valid
        
        return dp[0]


s= Solution()

print(s.wordBreak('leetcode',['leet','code']))