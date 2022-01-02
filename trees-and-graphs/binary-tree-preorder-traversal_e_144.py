# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrderTraverseRecursion(node):
            if not node:
                return []
            
            left = preOrderTraverseRec(node.left)
            right = preOrderTraverseRec(node.right)
            root = [node.val]
            
            return root + left + right
        
        def preOrderTraverseIterative(node):
            res = []
            queue = [node]
            
            while queue:
                n = queue.pop(0)
                
                if not n:
                    continue
                    
                res.append(n.val)
                
                queue.insert(0, n.right)
                queue.insert(0, n.left)
            
            return res
        
        return preOrderTraverseIterative(root)
