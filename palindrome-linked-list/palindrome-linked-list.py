# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lista = [head.val]
        curr = head
        while curr.next != None:
            curr = curr.next
            lista.append(curr.val)
        l2 = tuple(lista)
        lista.reverse()
        print(l2)
        print(lista)
        if l2 == tuple(lista):
            return True
        return False