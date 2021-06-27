class Solution:
    def convert(self, s: str, numRows: int) -> str:
            if numRows==1 or numRows==0:
                return s
            data=[""]*numRows
            mode=number=0
            for letters in s:
                if mode==0:
                    data[number]+=letters
                    number+=1
                else:
                    data[number]+=letters
                    number-=1

                if number==numRows:
                    mode=1
                    number=numRows-2
                elif number==-1:
                    mode=0
                    number=1
            return ''.join(data)