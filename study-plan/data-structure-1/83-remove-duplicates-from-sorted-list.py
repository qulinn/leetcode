# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head
        while curr is not None and curr.next is not None:
            next_node = curr.next
            if curr.val == next_node.val:
                curr.next = next_node.next
                next_node.next = None
            else:
                curr = curr.next
        return head