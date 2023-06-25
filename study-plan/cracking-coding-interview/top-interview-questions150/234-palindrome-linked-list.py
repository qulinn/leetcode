# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        
        for i in range(len(node_list)//2):
            if node_list[i] != node_list[len(node_list)-i-1]:
                return False
        return True