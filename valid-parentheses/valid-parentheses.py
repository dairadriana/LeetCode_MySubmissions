class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "{":"}", "[":"]"}
        stack = []
        for c in s:
            if c in d.keys():
                stack.append(c)
            elif not stack or d[stack.pop()] != c:
                return False
        return not stack