class Solution:
    def isPalindrome(self, x: int) -> bool:
        myNew = [char for char in str(x)]
        myNew.reverse()
        myNew = ''.join(myNew)
        if myNew == str(x): return True
        else: return False