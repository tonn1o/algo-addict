# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def traverseInOrder(node):
            res = []

            if node:
                res = traverseInOrder(node.left)
                res.append(node.val)
                res += traverseInOrder(node.right)

            return res

        return traverseInOrder(root)



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderRecursive(node):
            if not node:
                return []
            
            left = inOrderRecursive(node.left)
            right = inOrderRecursive(node.right)
            root = [node.val]
            
            return left + root + right
        
        def inOrderIterative(root):
            current = root
            res = []
            stack = []
            
            while current or stack:
                while current:
                    stack.append(current)
                    current = current.left
                    
                current = stack.pop()
                
                if current.right:
                  current = current.right
                
            return res
        return inOrderIterative(root)
                    
