# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        curr = head.next
        prev = head
        while curr!=None:
            temp = prev.val
            prev.val = curr.val
            curr.val = temp
            if curr.next==None:
                break
            prev=curr.next
            curr=curr.next.next
        return head