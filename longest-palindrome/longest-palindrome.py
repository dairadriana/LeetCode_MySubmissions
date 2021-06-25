class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter_vals = Counter(s).values()
        res = sum([n-(n%2) for n in counter_vals])
        contains_odd = any(n%2 for n in counter_vals)
        return res+contains_odd