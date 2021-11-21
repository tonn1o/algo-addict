class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        res = 0
        rowsN = len(grid)
        colsN = len(grid[0])

        def removeAdjacentCells(rowIdx, colIdx):
            grid[rowIdx][colIdx] = "0"

            if rowIdx > 0 and grid[rowIdx - 1][colIdx] == "1":
                removeAdjacentCells(rowIdx - 1, colIdx)

            if rowIdx < rowsN - 1 and grid[rowIdx + 1][colIdx] == "1":
                removeAdjacentCells(rowIdx + 1, colIdx)

            if colIdx > 0 and grid[rowIdx][colIdx - 1] == "1":
                removeAdjacentCells(rowIdx, colIdx - 1)

            if colIdx < colsN - 1 and grid[rowIdx][colIdx + 1] == "1":
                removeAdjacentCells(rowIdx, colIdx + 1)


        for rowIdx in range(rowsN):
            for colIdx in range(colsN):
                val = grid[rowIdx][colIdx]

                if val == "0":
                    continue

                res += 1
                removeAdjacentCells(rowIdx, colIdx)


        return res
