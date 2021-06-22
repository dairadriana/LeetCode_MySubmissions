class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        my_numbers = []
        my_number = 0
        for c in s:
            if c.isnumeric() or c == "-" or c == '+': 
                if c == '-' and my_numbers or c == '+' and my_numbers: 
                    break
                my_numbers.append(c)
            elif not c.isnumeric():
                break
        if "-" in my_numbers and '+' in my_numbers: 
                return 0
        if my_numbers and my_numbers != ["-"] and my_numbers != ['+']: 
            my_number = int(''.join(my_numbers))
            if my_number < (-2)**31:
                return -2**31
            elif my_number > 2**31-1:
                return 2**31-1
        return my_number