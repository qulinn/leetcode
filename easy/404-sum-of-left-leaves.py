# editorial approach 3


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        current_node = root
        while current_node is not None:
            if current_node.left is None:
                current_node = current_node.right
            else:
                previous = current_node.left
                if previous.left is None and previous.right is None:
                    total_sum += previous.val
                while previous.right is not None and previous.right is not current_node:
                    previous = previous.right
                if previous.right is None:
                    previous.right = current_node
                    current_node = current_node.left
                else:
                    previous.right = None
                    current_node = current_node.right
        
        return total_sum