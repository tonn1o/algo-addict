"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        
        
        queue = collections.deque([root])
        lvlDict = collections.defaultdict(list)
        root.lvl = 0
        
        while queue:
            node = queue.popleft()
            nodeChildrenValues = []
            nodeLvl = node.lvl
            
            lvlDict[nodeLvl].append(node.val)
            
            for child in node.children:
                child.lvl = node.lvl + 1
                queue.append(child)

        return lvlDict.values()
        
        
