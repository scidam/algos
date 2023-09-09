class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        _ints = sorted(intervals, key=lambda x: x[0])

        result = []
        if not _ints:
            return []
        cint = [_ints[0][0], _ints[0][1]]
        for i in range(len(_ints)):
            if cint[1] < _ints[i][0]:
                result.append(cint[:])
                cint = [_ints[i][0], _ints[i][1]]
            if cint[1] >= _ints[i][0]:
                cint[1] = max(_ints[i][1], cint[1])
        result.append(cint[:])
        return result


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
