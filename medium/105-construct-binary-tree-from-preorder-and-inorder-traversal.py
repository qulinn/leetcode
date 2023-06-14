# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def arrayToTree(left, right):
            if left > right:
                return None

            nonlocal preorder_index
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)

            preorder_index += 1
            root.left = arrayToTree(left, inorder_index_map[root_value] - 1)
            root.right = arrayToTree(inorder_index_map[root_value]+ 1, right)

            return root
        
        preorder_index = 0
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return arrayToTree(0, len(preorder) - 1)