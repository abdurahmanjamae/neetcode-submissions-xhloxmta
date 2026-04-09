# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()        # start of merged list
        tail = dummy              # pointer to the current end

        while list1 and list2:    # merge while both lists have nodes
            if list1.val < list2.val:
                tail.next = list1     # attach smaller node
                list1 = list1.next    # move that list forward
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next          # advance tail

        # append remaining nodes (only one list may have leftovers)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next         # head of merged list

# Runtime: O(n + m) — we scan through both lists once.
# Memory: O(1) — no new nodes created; only a few pointers used.


