class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        new_arr = []

        def take_first_row(m):
            return m[0][:], [_ for _ in m[1:]] if m[1:] else [[]]

        def take_last_row(m):
            return m[-1][:], [_ for _ in m[:-1]] if m[:-1] else [[]]

        def take_last_col(m):
            return [_[-1] for _ in m if _] if m else [], [_[:-1] for _ in m] if m else [
                []
            ]

        def take_first_col(m):
            return [_[0] for _ in m if _] if m else [], [_[1:] for _ in m] if m else [
                []
            ]

        def spiral_matrix(mat):
            nonlocal new_arr

            if len(mat) == 0:
                return
            m, n = len(mat), len(mat[0])
            if m == 1 and n == 0:
                return

            row, m = take_first_row(mat)
            new_arr += row[:]
            col, m = take_last_col(m)
            new_arr += col[:]
            lrow, m = take_last_row(m)
            new_arr += lrow[::-1][:]
            fcol, m = take_first_col(m)
            new_arr += fcol[::-1][:]
            spiral_matrix(m)

        spiral_matrix(matrix)
        return new_arr


s = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(s.spiralOrder(mat))
