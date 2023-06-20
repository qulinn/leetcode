# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = list()
        if not root:
            return path
        path.append(root.val)      
        if root.left is not None:
            path.extend(self.preorderTraversal(root.left))
        if root.right is not None:
            path.extend(self.preorderTraversal(root.right))
        return path