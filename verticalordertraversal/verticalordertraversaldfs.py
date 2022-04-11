# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = {}
        
        def dfs(node, level, depth):
            if not node:
                return
            if level not in order:
                order[level]= {}
            if depth not in order[level]:
                order[level][depth] = []
            order[level][depth].append(node.val)
            dfs(node.left, level -1, depth +1)
            dfs(node.right, level +1, depth +1 )
            
            return 
        
        
        dfs(root,0, 0)
        
        ret = []
        for level in sorted(order.keys()):
            l = []
            for depth in sorted(order[level].keys()):
                l.extend(order[level][depth])
            ret.append(l)
        
        return ret
        