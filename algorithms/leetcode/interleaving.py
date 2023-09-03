class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s1) < len(s2):
            # assume s1 string is always longer than s2
            return self.isInterleave(s2, s1, s3)

        result = [[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
        result[0][0] = True

        for i in range(1, len(s1) + 1):
            result[i][0] = result[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            result[0][j] = result[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                result[i][j] = (result[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    result[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        return result[len(s1)][len(s2)]
