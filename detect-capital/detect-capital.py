class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.capitalize():
            return True
        if word == word.upper():
            return True
        if word == word.lower():
            return True
        return False