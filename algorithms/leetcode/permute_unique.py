class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        result = set()

        def permute(x, index, acc=None):
            if acc == None:
                acc = [0] * len(nums)

            if index == len(nums):
                result.add(tuple(acc[:]))
                return None

            for j in range(len(x)):
                acc[index] = x[j]
                _x = x[:]
                _x.pop(j)
                permute(_x, index + 1, acc)

        permute(nums, 0)
        return list(map(list, result))
