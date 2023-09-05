class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        current = 0
        while current < len(nums):
            if nums[current] != val:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
            current += 1
        return left


s = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
print(s.removeElement(nums, 2))
print(nums)
