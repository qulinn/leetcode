# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if not root:
            return result
        if root.left is not None:
            result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        if root.right is not None:
            result.extend(self.inorderTraversal(root.right))
        
        return result