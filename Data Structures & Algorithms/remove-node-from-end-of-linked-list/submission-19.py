# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles edge cases (like removing the head)
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Create a gap of 'n' nodes between left and right pointers
        while n > 0:
            right = right.next
            n -= 1
        
        # Move both pointers until right reaches the end
        # Left will stop exactly one node BEFORE the target
        while right:
            left = left.next
            right = right.next
        
        # Skip the target node by pointing to the one after it
        left.next = left.next.next
        
        # Return dummy.next instead of head (in case head was removed)
        return dummy.next

# Time Complexity: O(n) - Single pass through the list
# Space Complexity: O(1) - Only constant extra pointers used
        