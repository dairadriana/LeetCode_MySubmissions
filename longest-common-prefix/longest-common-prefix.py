class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        my_s = max(strs)
        i = 0
        check = ""
        prefix = ""
        
        while i < len(my_s):
            check += my_s[i]
            for s in strs:
                if not s.startswith(check):
                    return prefix
            prefix = check
            i +=1  
        return prefix