# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSame(root.left, root.right)
    
    def isSame(self, l,r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and self.isSame(l.left, r.right) and self.isSame(l.right, r.left)

