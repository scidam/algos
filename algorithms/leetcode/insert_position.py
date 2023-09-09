import time


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        def div_and_conq(left, right, val):
            if val <= nums[left]:
                return 0 if (left - 1) < 0 else left

            if val > nums[right]:
                return right + 1
            elif val == nums[right]:
                return right

            if right - left == 1:
                return left + 1
            mid_point = (right + left) // 2
            if nums[mid_point] <= val < nums[right]:
                return div_and_conq(mid_point, right, val)
            elif nums[left] < val <= nums[mid_point]:
                return div_and_conq(left, mid_point, val)

        return div_and_conq(left, right, target)


s = Solution()
#
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 7))
