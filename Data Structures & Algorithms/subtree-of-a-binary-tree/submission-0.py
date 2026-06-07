# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False

        if root.val == subRoot.val and self.isSame(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right



    def isSame(self, node, subRoot):
        if not node and not subRoot: return True

        if not node or not subRoot: return False
        if node.val != subRoot.val: return False

        return self.isSame(node.left, subRoot.left) and self.isSame(node.right, subRoot.right)