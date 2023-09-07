class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if (len(s) == len(t) and s != t) or len(t) < len(s):
            return False

        left = 0
        right = 0

        while right < len(t):
            if t[right] == s[left]:
                if left == len(s) - 1:
                    return True
                left += 1
            right += 1

        return len(s) == left + 1 and s[-1] == t[-1]
     -