# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(pNode, qNode):
            if not pNode and not qNode:
                return True
            
            if not pNode or not qNode:
                return False
            
            if pNode.val != qNode.val:
                return False
            
            return dfs(pNode.left, qNode.left) and dfs(pNode.right, qNode.right)
        
        return dfs(p, q)