# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev will point to the previous node (start as None)
        # curr will move through the list starting at head
        prev, curr = None, head

         # Traverse the linked list
        while curr:
            # Save the next node before changing pointers
            temp = curr.next
            # Reverse the pointer: make current node point to previous
            curr.next = prev
            # Move prev and curr one step forward
            prev = curr
            curr = temp
        return prev

#RT: O(n), M: O(1) since we only have pointers
        