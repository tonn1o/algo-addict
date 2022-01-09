"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        
        if not root:
            return res
        
        def traverse(node):
            if not node:
                return
            
            res.append(node.val)
            
            for childNode in node.children:
                traverse(childNode)
                
        traverse(root)
        return res
