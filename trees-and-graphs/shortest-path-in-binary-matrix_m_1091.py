# BFS (Passed)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1
        
        if grid[0][0] != 0 or grid[maxRow][maxCol] != 0:
            return -1 

        def getNeighbors(cell):
            row = cell[0]
            col = cell[1]
            
            validNeighbors = []
            neighbors = [
                (-1, -1), (-1, 0), (-1, 1), 
                (0, -1), (0, 0), (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            
            for nRow, nCol in neighbors:
                r = row + nRow
                c = col + nCol
                
                if r > maxRow or c > maxCol or r < 0 or c < 0 or grid[r][c] != 0:
                    continue
                    
                validNeighbors.append((r, c))
            
            return validNeighbors
        
        queue = [[0, 0]]
        grid[0][0] = 1
        
        
        while queue:
            cell = queue.pop(0)
            distance = grid[cell[0]][cell[1]]
            
            if cell[0] == maxRow and cell[1] == maxCol:
                return distance
                
            for n in getNeighbors(cell):                
                grid[n[0]][n[1]] = distance + 1
                queue.append(n)

        return -1 


# DFS (Time limit exceeded)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if not grid or grid[n-1][n-1] != 0:
            return -1
        
        visited = [ [ False for i in range(n) ] for j in range(n) ]
        ans = None
        
        def dfs(cell, length):
            if cell[0] == n-1 and cell[1] == n-1:
                nonlocal ans
                
                if not ans or ans > length:
                    ans = length
                    
                return True
            
            if cell[0] < 0 or cell[1] < 0 or cell[0] >= n or cell[1] >= n:
                return False 
                
            if visited[cell[0]][cell[1]]:
                return False
            
            visited[cell[0]][cell[1]] = True
            
            if grid[cell[0]][cell[1]] != 0:
                return False
            
            possible = [
                [cell[0] + 1, cell[1] + 1],                
                [cell[0] + 1, cell[1]],
                [cell[0], cell[1] + 1],
                [cell[0] + 1, cell[1] - 1],
                [cell[0] - 1, cell[1] + 1],
                [cell[0], cell[1] - 1],
                [cell[0] - 1, cell[1]],
                [cell[0] - 1, cell[1] - 1],
            ]
            
            for c in possible:
                dfs(c, length + 1)
            
            visited[cell[0]][cell[1]] = False
                
        dfs([0,0], 1)
        
        return ans or -1                
