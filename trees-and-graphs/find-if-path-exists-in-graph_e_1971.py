# Disjoint set
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = dict()

        for edge in edges:
            if graph.get(edge[0]):
                graph[edge[0]].add(edge[1])
            else:
                graph[edge[0]] = set({edge[1]})

            if graph.get(edge[1]):
                graph[edge[1]].add(edge[0])
            else:
                graph[edge[1]] = set({edge[0]})


        visited = set()

        def find(node):
            if node in visited:
                return False

            visited.add(node)

            if node == end:
                return True

            for n in graph[node]:
                if find(n):
                    return True

            return False

        return find(start)

# BFS
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = collections.defaultdict(set)
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
            
        visited = [False] * n
        
        
        def bfs(node):
            queue = []
            queue.append(node)
            visited[node] = True
        
            while queue: 
                node = queue.pop()
                
                if  node == end:
                    return True
                
                for childNode in graph[node]:
                    if visited[childNode] == False:
                        visited[childNode] = True
                        queue.append(childNode)
                        
                            
            return False
        
        return bfs(start)
