"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursive
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        if not root:
            return res
        
        def traverse(node):
            if not node:
                return
            
            for childNode in node.children:
                traverse(childNode)
                
            res.append(node.val)
                
        traverse(root)
        return res

# Iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        if not root:
            return res
        
        
        stack = [root]
        
        while stack:
            node = stack.pop()
            res.insert(0, node.val)
            
            for child in node.children:
                stack.append(child)
                
        return res
