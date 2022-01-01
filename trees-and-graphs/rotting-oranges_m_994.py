class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        res = 0
        
        m = len(grid)
        n = len(grid[0])
        
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1
        
        freshOrangesCount = 0
        
        queue = collections.deque()
        
        #find all initial rotten oranges
        
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                
                if val == 2:
                    queue.append((i, j, 0))
                    
                if val == 1:
                    freshOrangesCount += 1

        if not queue:
            if freshOrangesCount > 0:
                return -1
            else: 
                return 0
            
        
        def getAdjucentFreshOranges(row, col):
            freshOranges = set()
            neighbords = {(-1, 0), (0, 1), (1, 0), (0, -1)}
            
            for n in neighbords:
                nRow = row + n[0]
                nCol = col + n[1]
                
                if nRow > maxRow or nRow < 0 or nCol > maxCol or nCol < 0:
                    continue
                    
                if grid[nRow][nCol] == 1:
                    freshOranges.add((nRow, nCol))
                    
            return freshOranges
                    
        while queue:
            cell = queue.popleft()
            
            for orangeCell in getAdjucentFreshOranges(cell[0], cell[1]):
                minutes = cell[2] + 1
                freshOrangesCount -= 1
                grid[orangeCell[0]][orangeCell[1]] = 2
                queue.append((orangeCell[0], orangeCell[1], minutes))                
                res = minutes
                
        if freshOrangesCount > 0:
            return -1 
                
        return res

