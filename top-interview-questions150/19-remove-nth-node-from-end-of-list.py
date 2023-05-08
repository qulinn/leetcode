class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

         
class Solution:
    def removeNthFromEnd(self, head:ListNode, n: int) -> ListNode:
        #全部のノードをたどる -> len(linkedlist)を得る
        #len(linkedlist) - n 番目を削除        
        curr = head
        len_list = 1
        while curr.next:
            len_list += 1
            curr = curr.next
        
        count = 1
        prev = None
        curr = head
        
        if len_list - n == 0:
            head = head.next
            return head
            
        while curr:
            if count == len_list - n + 1:
                prev.next = curr.next
                break
            else:
                prev = curr
                curr = curr.next
            count += 1
        return head
