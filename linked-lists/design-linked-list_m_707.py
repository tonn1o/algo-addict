class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current_index = 0
        node = self.head
        
        while node and current_index != index:
            node = node.next
            current_index += 1
            
        if node: 
            return node.val 
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        newHead = Node(val)
        
        if self.head:
            newHead.next = self.head
        
        self.head = newHead
        

    def addAtTail(self, val: int) -> None:
        newTail = Node(val)
        node = self.head
        
        if not node:
            self.head = newTail
            return

        while node.next:
            node = node.next
            
        node.next = newTail
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        current_index = 0
        prev = None
        node = self.head
        
        if index == 0 and not node:
            self.head = newNode
            return
        
        if index == 0 and node:
            newNode.next = self.head
            self.head = newNode
            return
        
        
        while node and current_index != index:
            prev = node
            node = node.next
            current_index += 1

        if node:
            prev.next = newNode
            newNode.next = node
            
        if prev and current_index == index:
            prev.next = newNode

            
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return 
        
        current_index = 0
        prev = node = self.head
        
        while node and current_index != index:
            prev = node
            node = node.next
            current_index += 1
            
        if node:
            prev.next = node.next
            

