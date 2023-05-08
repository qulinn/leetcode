# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections



class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        levels = []
        queue = collections.deque([root, 0])
        while queue:
            curr, level_num = queue.popleft()

            if len(levels) == level_num:
                levels.append([curr.val])
            else:
                levels[level_num].append(curr.val)
            
            if curr.left:
                queue.append([curr.left, level_num+1])
            if curr.right:
                queue.append([curr.right, level_num+1])

        return levels
