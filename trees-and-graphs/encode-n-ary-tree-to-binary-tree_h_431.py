"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return root 
        
        def encodeNode(node, direction):
            childDirection = 'r' if direction == 'l' else 'l'

            head = tail = TreeNode(node.val)

            if not node.children:
                return head

            for child in node.children:
                if childDirection == 'r': 
                    tail.right = encodeNode(child, childDirection)
                    tail = tail.right
                else:
                    tail.left = encodeNode(child, childDirection)
                    tail = tail.left

            return head
        
        return encodeNode(root, 'l')
                
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return data
        
        def decodeNode(node, direction):
            dNode = Node(node.val, [])
            
            if direction == 'r':
                tail = node.right
                
                while tail:
                    tailNode = None
                    
                    if tail.left:
                        tailNode = decodeNode(tail, 'l')
                    else:
                        tailNode = Node(tail.val, [])
                    
                    dNode.children.append(tailNode)
                    tail = tail.right
                    
                                
            if direction == 'l':
                tail = node.left
                
                while tail:
                    tailNode = None
                    
                    if tail.right:
                        tailNode = decodeNode(tail, 'r')
                    else:
                        tailNode = Node(tail.val, [])
                    
                    dNode.children.append(tailNode)
                    tail = tail.left
                  
            return dNode

        res = decodeNode(data, 'r')
        return res
                    
            
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
