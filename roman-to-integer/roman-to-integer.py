class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50, 
            "C" : 100, 
            "D" : 500, 
            "M" : 1000
        }
        l = 0
        i = 0
        while i <len(s):
            if i < len(s)-1:
                if d.get(s[i+1]) > d.get(s[i]):
                    l += (d.get(s[i+1]) - d.get(s[i]))
                    i+=1
                else:
                    l += (d.get(s[i]))
            else:
                # Add last value
                l += (d.get(s[i]))
            i+=1
        return l