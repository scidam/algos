# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         nums.sort(key=lambda x: 0 if x != 0 else 1)


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0 and anchor != explorer:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1
            elif nums[explorer] != 0 and anchor == explorer:
                anchor += 1


s = Solution()
l = [1, 3, 0, 3, 0]
s.moveZeroes(l)
print(l)
