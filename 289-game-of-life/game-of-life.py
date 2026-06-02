class Solution:

    # old | new | representation
    #  0  |  0  |   0
    #  1  |  0  |   1
    #  0  |  1  |   2
    #  1  |  1  |   3

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW, COL = len(board), len(board[0])
        def count_one(r,c):
            count = 0
            for row in range(r - 1, r + 2):
                for col in range(c - 1, c + 2):
                    if row < 0 or col < 0 or row == ROW or col == COL or (row == r and col == c):
                        continue
                    else:
                        count += 1 if board[row][col] == 1 else 0
            return count
        ans = [[0]* COL for _ in range(ROW)]
        for r in range(ROW):
            for c in range(COL):
                nei = count_one(r,c)
                print(f"for r: {r} and c: {c} the nei: {nei}")
                if board[r][c] == 1:
                    if nei == 2 or nei == 3:
                        ans[r][c] = 1
                    else:
                        ans[r][c] = 0
                else:
                    if nei == 3:
                        ans[r][c] = 1
        for r in range(ROW):
            for c in range(COL):
                board[r][c] = ans[r][c]
        return board 
        