# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head  # Start both at head

        while fast and fast.next:  # Make sure fast can move 2 steps
            slow = slow.next       # Move slow 1 step
            fast = fast.next.next  # Move fast 2 steps

            if slow == fast:       # They meet = cycle
                return True

        return False               # Fast reached the end = no cycle

# Time: O(n)
# Space: O(1)
# Mental cue: slow 1, fast 2 → if they meet, cycle