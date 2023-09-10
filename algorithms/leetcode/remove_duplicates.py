class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        for k in range(1, len(nums)):
            if nums[left] != nums[k]:
                left += 1
                nums[left] = nums[k]
        return left + 1


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(nums))
print(nums)
