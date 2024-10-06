#24. Swap Nodes in Pairs

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # This pointer will be used to track the previous node in the swap
        prev = dummy
        
        # Traverse the list in pairs
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Move the pointers forward
            prev = first_node
            head = first_node.next
        
        # Return the new head of the list
        return dummy.next
