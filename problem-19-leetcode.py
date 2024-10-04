#19. Remove Nth Node From End of List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):  # No type hints here
        # Create a dummy node that points to the head
        dummy = ListNode(0, head)
        slow = fast = dummy
        
        # Move fast pointer n+1 steps ahead so that there's a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both slow and fast until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Skip the desired node
        slow.next = slow.next.next
        
        return dummy.next  # Return the new head of the list

# Helper function to create a linked list from a list
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list for easier output
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
