# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iteratively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 2 Pointers
        prev, curr = None, head

        while curr:
            # Store old pointer
            temp = curr.next

            # Reverse pointer's direction
            curr.next = prev
            # Shift pointers to process next node
            prev = curr
            curr = temp

        return prev
