class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Make an adjacency list
        adj_list= {}
        for i in range(n):
            adj_list[i]=[]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited_set = set()
        def dfs(node, prev): 
            visited_set.add(node)
            for neighbor in adj_list[node]:
                if (neighbor not in visited_set): 
                    dfs(neighbor, node)
        ret = 0 
        for node in adj_list.keys():
            if (node not in visited_set):
                ret+=1
                dfs(node,-1)
        
        return ret
        