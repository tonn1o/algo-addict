# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([root, False])

        res = []
        
        currLevelSum = 0
        levelNodesCount = 0
            
        while queue:
            node = queue.popleft()
            
            if node is False:
                if levelNodesCount == 0: continue 
                    
                res.append(currLevelSum / levelNodesCount)
                
                currLevelSum = 0 
                levelNodesCount = 0
                
                queue.append(False)
                continue
                
            currLevelSum += node.val
            levelNodesCount += 1
            
            if node.left: 
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

# DFS 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        levelValuesDict = collections.defaultdict(list)
        maxLevel = 0

        def dfs(node, lvl):
            nonlocal maxLevel
            if not node:
                return

            levelValuesDict[lvl].append(node.val)
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)
            maxLevel = max(lvl, maxLevel)


        dfs(root, 0)

        for i in range(maxLevel + 1):
            res.append(sum(levelValuesDict[i]) / len(levelValuesDict[i]))

        return res
