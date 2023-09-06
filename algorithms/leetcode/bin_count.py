class Solution:
    def countBits(self, n: int) -> list[int]:
        return list(map(lambda x: bin(x).count("1"), range(n + 1)))
