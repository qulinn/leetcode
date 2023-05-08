class Solution:
    # Reverse k nodes of the given linked list.
    # This function assumes that the list contains at least k nodes.
    # 1) Keep track of the next node to process in the original list.
    # 2) Insert the node pointed to by "ptr" at the beginning of the reversed list.
    # 3) Move on to the next node
    # 4) Decrement the count of nodes to be reversed by 1
    # 5) return the head of the reversed list

    def reverseLinkedList(self, head, k):
        new_head, ptr = None, head
        while k:       
            next_node = ptr.next      
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head
                
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        ktail = None
        
        # Head of the final, moified linked list
        new_head = None
        
        # Keep going until there are nodes in the list
        while ptr:
            count = 0
            # Start counting nodes from the head
            ptr = head
            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            # If we counted k nodes, reverse them        
            if count == k:        
                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)
                # new_head is the head of the final linked list
                if not new_head:
                    new_head = revHead
                
                # ktail is the tail of the previous block of 
                # reversed k nodes
                if ktail:
                    ktail.next = revHead
                    
                ktail = head 
                head = ptr
        
        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head
        
        return new_head if new_head else head