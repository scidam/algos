class Solution:
    def minimumTotal(self, triangle: list[List[int]]) -> int:
        from copy import deepcopy
        k, i = 0 , len(triangle) - 1 
        results = []
        for k in range(len(triangle[-1])):
            sum = triangle[-1][k]
            _k = k 
            for i in range(len(triangle), -1, -1):
                if triangle[i][_k-1] < 
                sum += min(triangle[i][_k-1], triangle[i][_k])

# i, k<i

# i-1:   m(k) = min(m(k-1), m(k))
# i: m(k) -- minimal position, 