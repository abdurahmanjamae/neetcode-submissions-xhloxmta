# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()  # Start of merged list
        tail = dummy        # End of merged list

        # Compare nodes while both lists have values
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1      # Attach smaller node
                list1 = list1.next     # Move list1 forward
            else:
                tail.next = list2      # Attach smaller node
                list2 = list2.next     # Move list2 forward

            tail = tail.next            # Move tail forward

        tail.next = list1 or list2      # Attach remaining nodes

        return dummy.next               # Skip dummy, return real head

# Time: O(n + m)
# Space: O(1)
# Mental cue: compare → attach smaller → move that list → move tail → attach remainder
        