class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        window = nums[:k]
        within_max = max(window)
        within_max_1 = max(window[1:])
        result = [within_max]
        for i in range(1, len(nums) - k + 1):
            within_max = max(nums[i - 1], within_max_1, nums[i + k - 1])
            within_max_1 = max(within_max_1, nums[i + k - 1])
            result.append(within_max)
        return result


# NOTE SOLVED!


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
