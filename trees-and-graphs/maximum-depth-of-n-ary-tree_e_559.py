"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        res = 0
        
        def getMaxDepth(node, depth):
            nonlocal res
            res = max(res, depth)
            
            for child in node.children:
                getMaxDepth(child, depth + 1)
                
        getMaxDepth(root, 1)
        return res
            
            
# Alternative solution
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        if not root.children:
            return 1
        
        heights = []
        
        for child in root.children:
            heights.append(self.maxDepth(child))
            
        return max(heights) +  1
            
