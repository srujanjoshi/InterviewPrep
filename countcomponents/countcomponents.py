class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        adj_list = {}
        
        for i in range(n):
            adj_list[i] = []
            
            
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
            
        visited = set()
        def dfs(node):
            visited.add(node)
            for child in adj_list[node]:
                if child not in visited:
                    dfs(child)
            
        num = 0 
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                num+=1
                
        
        return num 