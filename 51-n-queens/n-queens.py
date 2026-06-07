class Solution:
    def solve(self,col, ans, rowList,lowerDiagonal, upperDiagonal, board, n):
        if col == n:
            ans.append(board[:])
            return
        for row in range(n):
            if rowList[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                rowList[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                self.solve(col+1, ans, rowList, lowerDiagonal, upperDiagonal, board, n)
                board[row] = board[row][:col] + "." + board[row][col+1:]
                rowList[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n for _ in range(n)]
        rowList = [0] * n
        lowerDiagonal = [0] * (2*n - 1)
        upperDiagonal = [0] * (2*n - 1)
        ans = []
        self.solve(0,ans, rowList, lowerDiagonal, upperDiagonal, board, n)
        return ans
