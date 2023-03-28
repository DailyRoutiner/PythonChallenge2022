import collections


class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        # row에 1-9 중복되는 거 체크
        rows = collections.defaultdict(set)
        #col에 1-9 중복되는 거 체크
        cols = collections.defaultdict(set)
        # 3 * 3 에 중복되는 거 체크
        squares = collections.defaultdict(set) # keys = r3 / c3

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                # 어떻게 이렇게 조건을 달았지...?
                if ( board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)] ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


sol = Solution()

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(sol.isValidSudoku(board=board))