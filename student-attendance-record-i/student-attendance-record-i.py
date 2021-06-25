class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') >= 2: return False
        if s.count('L') < 3: return True
        
        my_attendance = [char for char in s]
        for i in range(len(my_attendance)):
            if (my_attendance[i] == 'L') and (i > len(my_attendance)-3):
                return True
            if my_attendance[i] == 'L' and my_attendance[i+1] == 'L' and my_attendance[i+2] == 'L':
                return False
        return True