
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        mem = 0
        result = ""
        for i in range(1, max_len+1):
            u = int(a[-i]) if i < len(a)+1 else 0
            v = int(b[-i]) if i < len(b)+1 else 0
            mem, res = divmod(u + v + mem, 2)
            result+=str(res)
        if mem:
            result+='1'
        return result[::-1]

s = Solution()
print(s.addBinary("11", "1"))