"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        g = collections.defaultdict(set)
        rootNode = node

        visited = [False] * 101

        def dfs(n):
            if visited[n.val]:
                return n.val

            visited[n.val] = True

            for neighbor in n.neighbors:
                nVal = dfs(neighbor)
                g[n.val].add(nVal)

            return n.val

        gHash = dict()

        def copyGraph(v):
            if v in gHash:
                return gHash[v]

            neighbors = []
            gHash[v] = Node(v, neighbors)

            for n in g[v]:
                neighbors.append(copyGraph(n))

            return gHash[v]

        d = dfs(node)

        return copyGraph(node.val)


