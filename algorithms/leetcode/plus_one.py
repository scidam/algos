class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = []
        mem = 1
        for val in digits[::-1]:
            mem, new = divmod(val + mem, 10)
            result.append(new)
        if mem:
            result.append(1)
        return result[::-1]
        
s = Solution()
print(s.plusOne([9,9,9]))