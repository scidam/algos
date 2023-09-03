class Solution:
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_lowercase, digits

        rectified = "".join(filter(lambda x: x in ascii_lowercase + digits, s.lower()))
        return rectified == rectified[::-1]


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
