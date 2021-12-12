"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head
        
        nodesDict = dict()
        
        def cpNode(n):
            if not n:
                return None
            
            val = n.val
            
            if n in nodesDict:
                return nodesDict.get(n)
            
            node = Node(n.val)
            nodesDict[n] = node
            
            node.next = cpNode(n.next)
            node.random = cpNode(n.random)
            return node
        
        return cpNode(head)
            
