class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        end = n - 1
        g = dict()

        for i, v in enumerate(graph):
            g[i] = v

        paths = list()

        def findPaths(x, path):
            if x == end:
                return paths.append(path + [x])

            for node in g[x]:
                findPaths(node, path + [x])

        findPaths(0, [])

        return paths

# DFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end = len(graph) - 1
        
        def dfs(node, path):
            p = path + [node]
            if node == end:
                res.append(p)
            
            for n in graph[node]:
                dfs(n, path + [node])
           
        dfs(0, [])
        return res
        
# BFS
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        end = len(graph) - 1
        
        def bfs(node):
            queue = [[node]]
            
            while queue:
                q = queue.pop()
                n = q[-1]
                
                for e in graph[n]:
                    queue.append(q + [e])
                    
                if n == end:
                    res.append(q)
               
        bfs(0)
        return  res
                    
                
