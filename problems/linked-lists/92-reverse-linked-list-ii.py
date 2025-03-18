from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)

        window = deque()

        cur = head
        count = 1
        while cur:
            if left <= count <= right:
                window.append(cur.val)
            cur = cur.next
            count += 1

        # reverse those nodes
        cur = head
        count = 1
        while cur:
            if left <= count <= right:
                cur.val = window.pop()
            count += 1
            cur = cur.next

        return dummy.next
