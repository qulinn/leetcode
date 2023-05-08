# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = collections.deque()
        stack.append([1,root])
        answer = 0
        while stack:
            v,node = stack.pop()
            if node:
                answer = max(answer,v)
            if node.right is not None:
                stack.append([v+1, node.right])
            if node.left is not None:
                stack.append([v+1, node.left])
        return answer