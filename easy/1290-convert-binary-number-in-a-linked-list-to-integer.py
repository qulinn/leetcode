# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        digit = len(l) - 1
        ans = 0
        for i in range(len(l)):
            ans += l[i] * 2 ** digit
            digit -= 1
        return ans
