# https://leetcode.com/problems/insertion-sort-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        black = ListNode(head.val)
        dummy = ListNode(next=black)
        red = head.next

        while red is not None:
            # Insert
            black.next = ListNode(red.val)
            black = black.next
            # Move to next
            red = red.next

        return dummy.next
