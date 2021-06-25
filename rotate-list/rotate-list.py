# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        l = 0
        if not head or k == 0:
            return head
        curr = head
        while curr:
            l += 1
            curr = curr.next
        if k >= l: 
            k %= l
        last, curr, prev = head, head, None
        while last.next:
            prev = last
            last = last.next
        last.next = head
        k = l - k
        while k:
            k -= 1
            prev = curr
            curr = curr.next
        prev.next = None
        return curr