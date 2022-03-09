from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = {}
        for i in range(n):
            adj_list[i]=[]
        for edge in edges: 
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited_set = set()
        def dfs(node, prev):
            visited_set.add(node)
            valid = True
            for neighbor in adj_list[node]:
                if(neighbor!= prev and neighbor in visited_set):
                    return False
                if(neighbor!= prev):
                    valid = valid and dfs(neighbor,node) 
            return valid

        return (dfs(0,-1) and (len(visited_set) == n))
print(Solution().validTree(5,[[0,1],[0,2],[0,3],[1,4]]))