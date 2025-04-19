from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                element = board[i][j]
                if element in rows[i]:
                    return False
                rows[i].add(element)

                if element in columns[j]:
                    return False
                columns[j].add(element)

                if element in squares[i // 3][j // 3]:
                    return False
                squares[i // 3][j // 3].add(element)
        return True
