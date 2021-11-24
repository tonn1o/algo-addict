
# Non optimal solution. Working but exceeds time limit
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not words:
            return []

        res = []
        height = len(board)
        width = len(board[0])

        def hasLetterSequenceAt(word, row, col):
            if not letters:
                return True

            val = board[row][col]
            board[row][col] = 0

            if row < height - 1 and board[row + 1][col] == letters[0] and hasLetterSequenceAt(letters[1:], row + 1, col):
                board[row][col] = val
                return True
            if col < width - 1 and board[row][col + 1] == letters[0] and hasLetterSequenceAt(letters[1:], row, col + 1):
                board[row][col] = val
                return True
            if row > 0 and board[row - 1][col] == letters[0] and hasLetterSequenceAt(letters[1:], row - 1, col):
                board[row][col] = val
                return True
            if col > 0 and board[row][col - 1] == letters[0] and hasLetterSequenceAt(letters[1:], row, col - 1):
                board[row][col] = val
                return True

            board[row][col] = val
            return False

        def hasWord(word):
            for i in range(height):
                for j in range(width):
                    if board[i][j] == word[0]:
                        if hasLetterSequenceAt(word[1:], i, j):
                            return True

        for word in words:
            if hasWord(word):
                res.append(word)

        return res
