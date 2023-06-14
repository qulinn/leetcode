# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersect(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print(slow.val)
                return slow
                # slow = -4
        return None
# [0,1,2,3,4,5,6,7]
# pos = 3
# phase1
    # slow = 5
# phase2
    # ptr1, ptr2
    # 0 5
    # 1 6
    # 2 7
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            print(ptr1.val, ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1

