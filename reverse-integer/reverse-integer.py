class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            x *= -1
            is_negative = True
        myStr = [char for char in str(x)]
        myStr.reverse()
        my_answer = int(''.join(myStr))
        if is_negative: 
            my_answer *= -1
        if my_answer > (2**31-1) or my_answer < -(2**31):
            return 0
        return my_answer