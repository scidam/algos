class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        val = -int(str(x).replace('-', '')[::-1]) if neg else int(str(x)[::-1])
        if val < -(2**31) or val > 2**31 - 1:
            return 0
        return val