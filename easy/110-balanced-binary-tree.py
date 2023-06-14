# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #compute the tree's height via recursion
    def height(self, root:TreeNode)->int:
        #an enpty tree has height-1
        if not root:
            return -1
        return 1+max(self.height(root.left), self.height(root.right))



    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #an empty tree satisties the definition of a balanced tree.
        if not root:
            return True
        
        #check if subtrees have height within 1.
        #if they do, check if the subtrees are balanced
        return abs(self.height(root.left)-self.height(root.right))<2 \
        and self.isBalanced(root.left)\
        and self.isBalanced(root.right)
        