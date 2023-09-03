class Solution:
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) > 4 or len(digits) <= 0:
            return []

        result = []

        def all_combinations(digits, comb=""):
            if not digits:
                result.append(comb)
                return result
            for item in self.mapping.get(digits[0]):
                all_combinations(digits[1:], comb=comb + item)

        all_combinations(digits)
        return result


s = Solution()
print(s.letterCombinations(""))
