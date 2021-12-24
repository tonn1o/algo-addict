class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        results = []
        visited = set()
        
        for edge in edges:
            graph[edge[0]].add(edge[1])
            
        if len(graph[destination]) > 0:
            return False
            
        def dfs(node):
            if len(graph[node]) == 0:
                return node == destination
            
            for n in graph[node]:
                if n in visited:
                    return False
                
                visited.add(n)
                
                if not dfs(n):
                    return False
                
                visited.remove(n)
                    
            return True            
        
        return dfs(source)
        
