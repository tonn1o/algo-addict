class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        visited = [False] * numCourses
        completed = [False] * numCourses
        
        for p in prerequisites:
            graph[p[0]].add(p[1])

        def dfs(node):
            if completed[node]:
                return True
                
            if visited[node]:
                return False
            
            visited[node] = True
            
            for n in graph[node]:
                if not dfs(n):
                    visited[node] = False
                    return False
            
            visited[node] = False
            completed[node] = True 
            return True
        
        
        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
