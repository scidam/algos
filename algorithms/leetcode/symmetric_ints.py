class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        s = map(str, range(low, high + 1))
        fs = filter(
            lambda x: len(x) % 2 == 0
            and sum(map(int, x[: len(x) // 2])) == sum(map(int, x[len(x) // 2 :])),
            s,
        )
        return len(list(fs))
