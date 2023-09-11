class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        return "".join(map(lambda x: x[0], words)) == s


s = Solution()
print(s.isAcronym(["an", "apple"], s="a"))
