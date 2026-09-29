class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        row_set=set()
        col_set=set()
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            row_set.add(min(matrix[i]))
        for j in range(cols):
            maximum=matrix[0][j]
            for i in range(rows):
                maximum=max(maximum,matrix[i][j])
            col_set.add(maximum)
        return list(col_set & row_set)
