from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m= len(heights)
        n= len(heights[0])
        drain = [[0]*n for i in range(m)] 
        
        visited_set = {}
        
        #0-> Not known whether spot drains to Atlantic or Pacific Ocean
        #1-> Spot drains to Pacific Ocean
        #2-> Spot drains to Atlantic Ocean
        #3-> Spot drains to both Pacific and Atlantic Ocean
        #4-> Spot drains to neither Ocean
        def dfs(i,j):
            if(drain[i][j] != 0):
                return drain[i][j]
            if(i==0 and j==n-1) or (i==m-1 and j ==0):
                drain[i][j]=3
                return 3
            surrounding_spots=set()
            if(i==0) or (j==0):
                surrounding_spots.add(1)
            if(i==m-1) or  (j==n-1):
                surrounding_spots.add(2)
            if (i,j) in visited_set: 
                visited_set[(i,j)]+=1
            else:
                visited_set[(i,j)]=1
            if (i+1 <m) and (((i+1,j) in visited_set and visited_set[(i+1,j)] <2 ) or (i+1,j) not in visited_set) and (heights[i][j]>= heights[i+1][j]):
                surrounding_spots.add(dfs(i+1,j))
            if (j+1 <n) and (((i,j+1) in visited_set and visited_set[(i,j+1)] <2 ) or (i,j+1) not in visited_set)and (heights[i][j]>= heights[i][j+1]):
                surrounding_spots.add(dfs(i,j+1))
            if (i >0) and (((i-1,j) in visited_set and visited_set[(i-1,j)] <2 ) or (i-1,j) not in visited_set)and (heights[i][j]>= heights[i-1][j]):
                surrounding_spots.add(dfs(i-1,j))
            if (j>0) and (((i,j-1) in visited_set and visited_set[(i,j-1)] <2 ) or (i,j-1) not in visited_set) and (heights[i][j]>= heights[i][j-1]):
                surrounding_spots.add(dfs(i,j-1))
            if(visited_set[i,j]>1):
                visited_set[i,j]-=1
            else:
                visited_set.pop((i,j))
            if((1 in surrounding_spots) and (2 in surrounding_spots)) or (3 in surrounding_spots):
                drain[i][j]=3
                return 3
            elif(1 in surrounding_spots):
                drain[i][j]=1
                return 1
            elif(2 in surrounding_spots):
                drain[i][j]=2
                return 2 
            else:
                drain[i][j]=4
                return 4
        
        res = []
        for i in range(m):
            for j in range(n): 
                if dfs(i,j) == 3:
                    res.append([i,j])                
        return res
                
                
print(Solution().pacificAtlantic([[13],[4],[12]]))

