# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = list()

        current = list1
        while current:
            values.append(current.val)
            current = current.next
        
        current = list2
        while current:
            values.append(current.val)
            current = current.next

        values.sort()

        node = ListNode()
        current = node

        for value in values:
            current.next = ListNode(value)
            current = current.next

        return node.next
            