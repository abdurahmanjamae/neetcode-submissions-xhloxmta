# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()  # Track visited node references
        curr = head

        while curr:
            # If node is already in set, we've looped back
            if curr in seen:
                return True
            
            seen.add(curr) # Store current node and move forward
            curr = curr.next
            
        return False # Reached null, so no cycle exists

# Time Complexity: O(n) - Visit each node once; O(1) set lookups.
# Space Complexity: O(n) - In the worst case, we store every node in the set.