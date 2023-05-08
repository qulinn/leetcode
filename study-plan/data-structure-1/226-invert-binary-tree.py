# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        container = collections.deque()
        container.append(root)

        while container:
            current = container.popleft()
            current.left, current.right = current.right, current.left
            if current.left:
                container.append(current.left)
            if current.right:
                container.append(current.right)            
        return root