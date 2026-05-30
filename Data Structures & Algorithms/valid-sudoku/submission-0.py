class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j])

                    # HANDLE ROWS
                    if rows[i][num - 1] == 1:
                        return False
                    else:
                        rows[i][num - 1] = 1
                    
                    # HANDLE COLS
                    if columns[j][num - 1] == 1:
                        return False
                    else:
                        columns[j][num - 1] = 1
                    
                    x_index = (3 * (i // 3) + (j // 3))
                    if subboxes[x_index][num - 1] == 1:
                        return False
                    else:
                        subboxes[x_index][num - 1] = 1 

        print(rows)
        print(columns)
        return True
