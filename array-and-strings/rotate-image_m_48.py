class Solution:
    import math

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def rotateSymmetricElems(row, col):
            currRow = row
            currCol = col
            tmp = matrix[currRow][currCol]


            for i in range(4):
                val = tmp
                destRow = currCol
                destCol = n - currRow - 1

                tmp = matrix[destRow][destCol]
                matrix[destRow][destCol] = val

                currRow = destRow
                currCol = destCol


        for i in range(math.ceil(n / 2)):
            for j in range(i, n-i-1):
                rotateSymmetricElems(i, j)
