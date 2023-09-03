class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 0 or len(s) == 1:
            return None

        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
