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

