class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        root = [0] * n

        for i in range(n):
            root[i] = i

        def find(x):
            while x != root[x]:
                x = root[x]

            return x


        for edge in edges:
            rootX = find(edge[0])
            rootY = find(edge[1])

            if rootX == rootY:
                return False

            root[rootX] = rootY

        return True
