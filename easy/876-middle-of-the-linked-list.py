# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
    
    # [1] -> [2] -> [3] -> [4] -> [5]
    # slow = fast = [1]
    # slow = slow.next = [2]
    # fast = fast.next.next = [3]
    # slow = slow.next = [3]
    # fast = fast.next.next = [5]
    # fast.next = None -> break
    # return slow = [3]
