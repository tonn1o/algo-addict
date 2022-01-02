# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorderTraversalRecursive(node):
            if node:
                postorderTraversalRecursive(node.left)
                postorderTraversalRecursive(node.right)
                res.append(node.val)

        postorderTraversalRecursive(root)

        return res 
    
        def postorderTraversalInterative(root):
            stack = [(root, False)]
            res = []
            
            while stack:
                node, visited = stack.pop()

                if node:
                    if visited:
                        res.append(node.val)
                    else:
                        stack.append((node, True))
                        stack.append((node.right, False))
                        stack.append((node.left, False))
                
            return res
