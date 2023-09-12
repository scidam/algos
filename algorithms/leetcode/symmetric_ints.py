class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        return len(
            list(
                filter(
                    lambda x: len(x) % 2 == 0
                    and sum(map(int, x[: len(x) // 2]))
                    == sum(map(int, x[len(x) // 2 :])),
                    map(str, range(low, high + 1)),
                )
            )
        )
