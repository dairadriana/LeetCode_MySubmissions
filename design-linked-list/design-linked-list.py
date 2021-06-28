class ListNode: # the defination of the node
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self): 
        self.head = None
        self.tail = None
        self.length = 0
		
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length: return -1
        else:
            node = self.head
            for _ in range(index):
                node = node.next
            return node.val

    def addAtHead(self, val: int) -> None:
        self.length += 1
        if self.head is None:
            self.head = self.tail = ListNode(val)
        else:
            node = ListNode(val, self.head)
            self.head = node
   
    def addAtTail(self, val: int) -> None: 
        if self.head is None:
            self.addAtHead(val)
        else:
            self.length += 1
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length: return
        if self.head is None or index == 0: return self.addAtHead(val)
        if index == self.length: return self.addAtTail(val)
        
        self.length += 1
        node = ListNode(val)
        prev = self.head
        for _ in range(index-1): prev = prev.next
        node.next = prev.next
        prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length: return
        self.length -= 1
        if self.length == 0: 
            self.head = self.tail = None
            return
        if index == 0:
            self.head = self.head.next
            return
        prev = self.head
        for _ in range(index-1): prev = prev.next
        prev.next = prev.next.next
        if self.length == index: self.tail = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)