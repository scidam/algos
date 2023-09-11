class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2):
            return False
        if s1 == s2:
            return True
        return s2 in (
            "".join([s1[2], s1[1], s1[0], s1[3]]),
            "".join([s1[2], s1[3], s1[0], s1[1]]),
            "".join([s1[0], s1[3], s1[2], s1[1]]),
        )
