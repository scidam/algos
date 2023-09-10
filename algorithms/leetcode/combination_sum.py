class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        candidates = sorted(list(filter(lambda x: x <= target, candidates)))

        def get_combination(acc=[], csum=0, index=0):
            if csum == target:
                results.append(acc[:])
                return
            if csum > target:
                return
            for i in range(index, len(candidates)):
                _acc = acc + [candidates[i]]
                get_combination(_acc, csum + candidates[i], i)

        get_combination()
        return results


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))


# [2, 3, 4, 5],   7

# 2,   target = 5  acc=[2]
# 2,   target = 3  acc=[2,2]
# 2,   target = 1  acc=[2,2,2]
