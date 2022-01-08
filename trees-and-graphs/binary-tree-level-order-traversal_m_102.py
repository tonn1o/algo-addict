# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        queue = collections.deque([(root, 0)])
        res = []
        
        while queue:                
            (node, depth) = queue.popleft()
            
            if len(res) > depth:
                res[depth].append(node.val)
            else:
                res.append([node.val])
            
            if node.left:
                queue.append((node.left, depth + 1))
                
            if node.right:
                queue.append((node.right, depth + 1))
                
        return res
