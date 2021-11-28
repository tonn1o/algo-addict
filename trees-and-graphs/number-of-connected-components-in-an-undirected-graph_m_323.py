class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        root = [0] * n
        rank = [0] * n

        for i in range(n):
            root[i] = i

        def find(x):
            if x != root[x]:
                x = find(root[x])

            return x

        for edge in edges:
            rootX = find(edge[0])
            rootY = find(edge[1])

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootX] = rootY
                elif rank[rootX] < rank[rootY]:
                    root[rootY] = rootX
                else:
                    root[rootX] = rootY
                    rank[rootX] += 1

        roots = set()

        for i in range(n):
            roots.add(find(root[i]))

        return len(roots)

