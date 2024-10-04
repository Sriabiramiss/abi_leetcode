#2. Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize dummy head and carry
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get values from the current nodes, or 0 if we've reached the end of a list
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry is total divided by 10
            new_val = total % 10  # The new digit is total modulo 10
            
            # Create a new node with the computed digit and append to the result list
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in l1 and l2 (if they exist)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the resulting linked list starting from dummy_head.next
        return dummy_head.next
