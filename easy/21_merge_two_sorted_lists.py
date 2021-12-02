# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # dummy node to hold the head of the merged list
        dummy = ListNode()
        current = dummy
        while list1 or list2:
            # if list2 is None, then list1 is the next node
            if list1 and not list2:
                next_value = list1.val
                list1 = list1.next
            # if list1 is None, then list2 is the next node
            elif list2 and not list1:
                next_value = list2.val
                list2 = list2.next
            # if both list1 and list2 are not None, then compare the values
            else:
                if list1.val <= list2.val:
                    next_value = list1.val
                    list1 = list1.next
                else:
                    next_value = list2.val
                    list2 = list2.next
            # set the next node and move to the next node
            current.next = ListNode(next_value)
            current = current.next

        # return the head of the merged list
        return dummy.next
