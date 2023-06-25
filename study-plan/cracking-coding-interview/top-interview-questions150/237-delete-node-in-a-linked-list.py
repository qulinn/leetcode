# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #given_node.next.valをgiven_nodeにコピー
        #given_node.nextをgiven_nodeの代わりに削除
        node.val = node.next.val
        node.next = node.next.next