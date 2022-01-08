# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node1, node2):
            if node1 == None or node2 == None:
                return node1 == node2
            
            if node1.val != node2.val:
                return False
            
            if not dfs(node1.left, node2.right):
                return False
                
            if not dfs(node1.right, node2.left):
                return False
            
            return True
        
        return dfs(root.left, root.right)
