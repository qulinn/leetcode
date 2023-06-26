# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        #keep first m nodes
        #delete the next n nodes
        keep_count = m
        delete_count = n
        root = head
        while root:
            keep_count -= 1
            if keep_count != 0:
                root = root.next 
            else:
                while delete_count != 0:
                    delete_count -= 1
                    if root.next == None:
                        break
                    root.next = root.next.next       
                root = root.next
                keep_count = m
                delete_count = n
        return head
        
#         1 2 3 4 5 6 7 8 9 10 11
#         m = 1, n = 3
        
#         keep_count = 0
#         delete_count = 3
#         root