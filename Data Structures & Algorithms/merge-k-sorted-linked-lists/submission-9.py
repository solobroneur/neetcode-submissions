# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = list()

        for node_list in lists:
            curr = node_list
            while curr:
                values.append(curr.val)
                curr = curr.next

        values.sort()

        sentinel = ListNode(0)
        curr = sentinel
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return sentinel.next

