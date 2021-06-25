class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        if s.split():
            return len(s.split()[-1])
        return 0