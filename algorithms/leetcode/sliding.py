class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        window = nums[:k]
        within_max = max(window)
        within_max_1 = max(window[1:])
        within_max_both = max(window[1:-1]) if window[1:-1] else min(nums)
        result = [within_max]
        for i in range(1, len(nums) - k + 1):
            window = nums[i:i+k]
            if window[-1] > within_max_1:
                within_max_1 = nums[-1]
                within_max = within_max_1
                
            elif within_max_1
            
            within_max_1 = max(within_max_1, nums[i + k - 1])
            result.append(within_max)
        return result


# NOTE SOLVED!


[1, 3, -1, -3, 5, 3, 6, 7]


 [1, 3, 5, -1]  => (window[0], max(widnow[1:]), max(window[1:-1]))
     [3 5  -1 -3]  (window[0]=nums[i], if nums[i+k]>mw1: mw1=nums[i+k]; if nums[i+k]<mw1: ,)



s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
