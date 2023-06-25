# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = []
        self.traverse(root)
        
        for i in range(len(self.result)-1):
            if self.result[i] >= self.result[i+1]:
                return False
        return True
        
        
    def traverse(self, root):
        if not root:
            return True
        self.traverse(root.left)
        self.result.append(root.val)
        self.traverse(root.right)
    