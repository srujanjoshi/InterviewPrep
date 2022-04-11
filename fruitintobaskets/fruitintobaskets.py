from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left, right = 0, 0
        baskets = set()
        max_num = 0
        cur_num = 0
        while(right< len(fruits)):
            if(fruits[right] in baskets):
                cur_num +=1 
                max_num = max(cur_num, max_num) 
            else:
                if len(baskets)==2:
                    baskets.remove(fruits[left])
                    discarded_fruit = fruits[left]
                    while(fruits[left] == discarded_fruit and left<len(fruits)):
                        left+=1
                        cur_num-=1
                baskets.add(fruits[right])
                cur_num+=1
                max_num = max(cur_num,max_num)
                    
            right+=1
        
        return max_num 

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))