# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeTree(self, root1, root2):
        if not root1 and not root2:
            return None
        if not root2:
            return root1
        if not root1:
            return root2

        node = TreeNode(root1.val + root2.val)
        node.left = self.makeTree(root1.left, root2.left)
        node.right = self.makeTree(root1.right, root2.right)

        return node



    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.makeTree(root1, root2)


