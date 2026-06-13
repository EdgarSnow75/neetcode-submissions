class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_col_start, box_row_start = 0, 0
        box_col_end, box_row_end = 3, 3
        box_count = 0
        board_length = len(board)
        for i in range(board_length):
            col_num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            row_num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            box_num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(board_length):
                if board[i][j] != ".":
                    if board[i][j] in col_num_list:
                        col_num_list.remove(board[i][j])
                    else:
                        return False
                
                if board[j][i] != ".":
                    if board[j][i] in row_num_list:
                        row_num_list.remove(board[j][i])
                    else:
                        return False
            
            while box_row_start < box_row_end:
                while box_col_start < box_col_end:
                    if board[box_row_start][box_col_start] != ".":
                        if board[box_row_start][box_col_start] in box_num_list:
                            box_num_list.remove(board[box_row_start][box_col_start])
                        else:
                            return False
                    box_col_start += 1
                box_row_start += 1
                box_col_start -= 3
            box_count += 1
            box_col_start = box_col_end
            box_col_end += 3
            box_row_start -= 3
            if box_count % 3 == 0:
                box_row_start = box_row_end
                box_row_end += 3
                box_col_start = 0
                box_col_end = 3
        return True





        