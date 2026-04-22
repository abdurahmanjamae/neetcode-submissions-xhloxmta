# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()  # placeholder node
        tail = dummy        # pointer to track the end of the new list

        # iterate while both lists have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next  # advance the tail
        
        # append the remaining nodes from the non-empty list
        tail.next = list1 or list2
        
        return dummy.next


# rt: O(n + m) where n and m are the lengths of the two lists.
# space: O(1) as we are rearranging existing nodes, not creating a new list.