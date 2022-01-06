class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_row, max_col = len(heights), len(heights[0])
        hasAccessToOceans = [[[False, False] for j in range(max_col)] for i in range(max_row)]        
        res = []
        pacificBeachLine = []
        atlanticBeachLine = []
                
        def getAdjacentCells(coords):
            row, col = coords
            
            if row == 3 and col == 0:
                a = 1 + 1
                
            height = heights[row][col]
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            cells = []
            
            for r, c in neighbors:
                if r < max_row and r >= 0 and c < max_col and c >= 0:
                    if height <= heights[r][c]:
                        cells.append([r, c]) 
            
            return cells

                    
        
        for i in range(max_row):
            for j in range(max_col):
                if i == 0 or j == 0:
                    pacificBeachLine.append([i, j])
                if i == max_row - 1 or j == max_col - 1:
                    atlanticBeachLine.append([i, j])
                
        queue = collections.deque(pacificBeachLine)
        visited = [[False for j in range(max_col)] for i in range(max_row)]
        
        while queue:
            cell = queue.popleft()
            row, col = cell 
            visited[row][col] = True
            hasAccessToOceans[row][col][0] = True
            
            for c in getAdjacentCells(cell):
                if not visited[c[0]][c[1]]:
                    queue.append(c)
                
                
        queue = collections.deque(atlanticBeachLine)
        visited = [[False for j in range(max_col)] for i in range(max_row)]
        
        while queue:
            cell = queue.popleft()
            row, col = cell 
            visited[row][col] = True
            hasAccessToOceans[row][col][1] = True
            
            for c in getAdjacentCells(cell):
                if not visited[c[0]][c[1]]:
                    queue.append(c)
                    
        for i in range(max_row):
            for j in range(max_col):
                oceans = hasAccessToOceans[i][j]
                
                if oceans[0] and oceans[1]:
                    res.append([i, j])
                    
                    
        return res
