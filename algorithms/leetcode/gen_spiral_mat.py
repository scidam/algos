import time


class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        from itertools import cycle

        nums = list(range(1, n * n + 1))[::-1]
        i, j = 0, -1
        direction = cycle(["right", "down", "left", "up"])

        result = [[None] * n for _ in range(n)]
        cdir = next(direction)
        while nums:
            # time.sleep(1)
            _i, _j = i, j
            if cdir == "right":
                j += 1
            elif cdir == "down":
                i += 1
            elif cdir == "left":
                j -= 1
            elif cdir == "up":
                i -= 1
            # print(f"i={i}, j={j}, direction={cdir}, nums={nums}")
            if j < 0 or j > n - 1 or i < 0 or i > n - 1:
                cdir = next(direction)
                i, j = _i, _j
                continue

            elif result[i][j] is None:
                el = nums.pop()
                result[i][j] = el

            elif result[i][j] is not None:
                cdir = next(direction)
                i, j = _i, _j

        return result


s = Solution()
print(s.generateMatrix(3))
