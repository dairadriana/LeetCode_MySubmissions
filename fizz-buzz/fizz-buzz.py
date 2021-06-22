class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        my_array = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                my_array.append("FizzBuzz")
            elif i%3 == 0:
                my_array.append("Fizz")
            elif i%5 == 0:
                my_array.append("Buzz")
            else:
                my_array.append(str(i))
        return my_array