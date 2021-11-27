class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0

        if not isConnected:
            return res

        n = len(isConnected)

        class UnionFind:
            def __init__(self, size):
                self.root = [0] * size
                self.rank = [1] * size

                for i in range(size):
                    self.root[i] = i

            def find(self, x):
                if x == self.root[x]:
                    return x

                self.root[x] = self.find(self.root[x])
                return self.root[x]



            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)

                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootX] = rootY
                        self.rank[rootY] += 1

            def conntected(self, x, y):
                return self.find(x) == self.find(y)

        provinces = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    provinces.union(i, j)

        memo = [False] * n

        for i in range(n):
            hasConnections = False

            for j in range(0, n):
                if i != j and provinces.conntected(i, j):
                    hasConnections = True
                    if not memo[i] and not memo[j]:
                        res += 1

                    memo[i] = True
                    memo[j] = True

            if not hasConnections:
                res += 1

        return res
