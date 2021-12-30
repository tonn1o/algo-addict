"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        def bfs(node):
            queue = [node]
            leftToCurrent = None
            veryRight = None
            
            while queue:
                n = queue.pop(0)
                val = n.val
                    
                if n.left:        
                    queue.append(n.left)
                
                if n.right:
                    n.left.next = n.right
                    queue.append(n.right)
                    
                if leftToCurrent and not leftToCurrent.next:
                    leftToCurrent.next = n

                if veryRight == None or veryRight == n:
                    veryRight = n.right
                    leftToCurrent = None
                else:
                    leftToCurrent = n
                
        bfs(root)
        return root
                
            
            
            
