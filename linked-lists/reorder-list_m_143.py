# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        sortedNodes = []
        
        node = head
        
        while node:
            nodes.append(node) 
            node = node.next
            
        n = len(nodes)
            
        for i in range(math.ceil(n / 2)):
            sortedNodes.append(nodes[i])
            
            if i != n - 1 - i:
                sortedNodes.append(nodes[n - 1 - i])
            
        head = tail = sortedNodes[0]
        
        for i in range(1, n):            
            tail.next = sortedNodes[i]
            tail = tail.next
            
        tail.next = None
