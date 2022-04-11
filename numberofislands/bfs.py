import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0 
        m= len(grid)
        n= len(grid[0])

        def bfs(i,j):
            visited = set()
            q = collections.deque()
            q.append((i,j))
            visited.add((i,j))
            while(q): 
                cur = q.popleft()
                r,c = cur[0], cur[1]
                if(
                    r < 0 or 
                    c < 0 or 
                    r > m-1 or 
                    c > n-1 or 
                    grid[r][c]=="0"
                ):
                    continue
                grid[r][c]="0"
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions: 
                    if((r+dr,c+dc) not in visited):
                        q.append((r+dr,r+dc))
        
        for i in range(m): 
            for j in range(n): 
                if(grid[i][j] == "1"):
                    bfs(i,j)
                    ret+=1
                    
        return ret



print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
