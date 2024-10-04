#21. Merge Two Sorted Lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the Solution class containing the mergeTwoLists method
class Solution:
    def mergeTwoLists(self, list1, list2) :
        # Create a dummy node to simplify merging logic
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list starts from the next of the dummy node
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(0)  # Dummy node
    current = head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return head.next

# Helper function to print the linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)
