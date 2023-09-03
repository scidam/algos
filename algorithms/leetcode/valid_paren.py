class Solution:
    paren_mapping = {
        "[": "]",
        "(": ")",
        "{": "}",
    }
    reverse_mapping = {v: k for k, v in paren_mapping.items()}

    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in self.paren_mapping:
                stack.append(item)
            elif item in self.reverse_mapping:
                if not stack:
                    return False
                opened = stack.pop()
                if self.reverse_mapping.get(item) != opened:
                    return False
            else:
                return False
        return not stack
