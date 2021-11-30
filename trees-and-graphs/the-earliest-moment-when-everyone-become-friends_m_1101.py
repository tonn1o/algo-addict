class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if not logs:
            return -1

        sortedLogs = sorted(logs, key=lambda x: x[0])

        root = [0] * n
        for i in range(n):
            root[i] = i


        def find(x):
            while x != root[x]:
                x = root[x]

            return x

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                root[rootX] = rootY

        def allConntected():
            mainRoot = find(root[0])

            for i in range (1, n):
                if mainRoot != find(root[i]):
                    return False

            return True


        for log in sortedLogs:
            union(log[1], log[2])

            if allConntected():
                return log[0]

        return -1


