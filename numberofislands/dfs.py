from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0 
        m= len(grid)
        n= len(grid[0])
        
        def dfs(i,j): 
            
            if( i<0 or 
                j<0 or
                i>m-1 or 
                j>n-1 or
                grid[i][j]=="0"
              ):
                return 
            
            grid[i][j] = "0"
            
            directions = [(1,0),(-1,0),(0,-1),(0,1)]
            
            for dr,dc in directions: 
                dfs(i+dr, j+dc)
            
            return
        
        for i in range(m): 
            for j in range(n): 
                if(grid[i][j] == "1"):
                    dfs(i,j)
                    ret+=1
                    
        return ret
