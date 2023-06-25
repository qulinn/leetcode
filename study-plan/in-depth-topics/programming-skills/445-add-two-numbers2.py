# editorial approach 1



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next
        
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        total = 0
        carry = 0
        ans = ListNode()
        while num1 or num2:
            if num1:
                total += num1.pop()
            if num2:
                total += num2.pop()
            ans.val = total % 10
            carry = total // 10
            
            head = ListNode(carry)
            head.next = ans
            ans = head
            total = carry
        
        return ans.next if carry == 0 else ans
        
