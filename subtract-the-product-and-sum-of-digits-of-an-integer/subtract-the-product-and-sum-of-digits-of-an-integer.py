class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n == 0: return 0
        n = str(n)
        mult = 1
        suma = 0
        for c in n:
            mult*=int(c)
            suma += int(c)
        return mult-suma