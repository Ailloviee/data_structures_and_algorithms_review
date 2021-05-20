from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        grid_map = defaultdict(list)

        for i in range(9):
            for j in range(9):
                curr_num = board[i][j]
                if curr_num == ".":
                    continue

                curr_num = int(curr_num)
                if curr_num < 1 or curr_num > 9:
                    return False

                if curr_num in row_map[i]:
                    return False

                row_map[i].append(curr_num)

                if curr_num in col_map[j]:
                    return False

                col_map[j].append(curr_num)

                grid_key = str(int(i) // 3) + str(int(j) // 3)
                if curr_num in grid_map[grid_key]:
                    return False

                grid_map[grid_key].append(curr_num)

        return True
