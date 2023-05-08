# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA:
            return None
        if not headB:
            return None
        
        node_b = set()
        while headB is not None:
            node_b.add(headB)
            headB = headB.next
        
        while headA is not None:
            #found the point to headA
            #return the node
            
            if headA in node_b:
                return headA
            headA = headA.next
            
        return None
        