class Solution:
    def firstUniqChar(self, s: str) -> int:
        for c in s:
            if s.count(c) == 1:
                return s.find(c)
        return -1