#25. Reverse Nodes in k-Group

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Helper function to reverse a portion of the linked list
        def reverse_linked_list(head, k):
            prev = None
            current = head
            while k > 0:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                k -= 1
            return prev
        
        # Dummy node initialization to simplify the head handling
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Check if there are k nodes left to reverse
            kth_node = group_prev
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next  # If less than k nodes, return the list as is
            
            # Keep track of the next group
            group_next = kth_node.next
            
            # Reverse the k nodes
            prev, current = None, group_prev.next
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Now `prev` is the new head of the reversed group, and `group_prev.next` is the tail
            tail = group_prev.next
            group_prev.next = prev  # Link the previous part to the reversed head
            tail.next = group_next  # Link the reversed group's tail to the next group
            
            # Move `group_prev` to the end of the reversed group
            group_prev = tail
        
        return dummy.next
