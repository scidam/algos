class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minlen = min(map(len, strs))
        if not minlen:
            return ""
        result = ""
        for k in range(1, minlen+1):
            if all(map(lambda x: x.startswith(strs[0][:k]), strs)):
                result = strs[0][:k]
        return result


s = Solution()
result = s.longestCommonPrefix(["dog","racecar","car"])
print(result)