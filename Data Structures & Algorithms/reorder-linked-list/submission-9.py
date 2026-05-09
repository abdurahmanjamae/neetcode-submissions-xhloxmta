# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return

        # 1. Split: Use slow/fast pointers to find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse: Flip the direction of the second half
        second = slow.next
        slow.next = None  # Sever the connection to create two separate lists
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # 3. Merge: Interleave nodes from 'first' and 'second' (prev)
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        """
        Complexity Analysis:
        - Time Complexity: O(n) 
          We traverse the list segments a constant number of times (split, reverse, merge).
        - Space Complexity: O(1) 
          We only use a few pointers; no extra data structures are created.
        """