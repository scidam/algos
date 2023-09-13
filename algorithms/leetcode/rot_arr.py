class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k % len(nums) == 0:
            return nums
        remainder = k % len(nums)
        print(remainder)
        nums[:] = nums[-remainder:] + nums[:-remainder]


s = Solution()
arr = [1, 2, 3]
s.rotate(arr, 7)
print(arr)
