class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        result = list()

        def permute(x, index, acc=None):
            if acc == None:
                acc = [0] * len(nums)

            if index == len(nums):
                result.append(acc[:])
                return None

            for j in range(len(x)):
                acc[index] = x[j]
                _x = x[:]
                _x.pop(j)
                permute(_x, index + 1, acc)

        permute(nums, 0)
        return result


nums = [1, 2, 3]


s = Solution()
print(s.permute([1, 2, 3]))
