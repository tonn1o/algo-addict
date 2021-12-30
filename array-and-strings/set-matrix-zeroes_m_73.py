class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        fillRows = set()
        fillCols = set()
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    fillRows.add(i)        
                    fillCols.add(j)        
            
            
        for i in range(m):
            for j in range(n):
                if i in fillRows or j in fillCols:
                    matrix[i][j] = 0
            
            
