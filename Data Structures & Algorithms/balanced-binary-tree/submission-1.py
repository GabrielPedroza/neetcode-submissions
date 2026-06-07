# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        balanced = abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1

        return balanced and left and right
    
    def getHeight(self, node):
        if not node: return 0

        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))