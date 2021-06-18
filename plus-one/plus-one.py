class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        myNum = []
        for n in digits:
            myNum.append(str(n))
        myNums = ''.join(myNum)
        myNums = [char for char in str((int(myNums)+1))]
        result = []
        for i in myNums:
            result.append(int(i))
        return(result)