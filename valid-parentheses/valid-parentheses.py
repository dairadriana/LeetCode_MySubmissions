class Solution:
    def isValid(self, s: str) -> bool:
        dictionary={"(":")", "[":"]", "{":"}"}
        list1=[]
        for c in s:
            if c in dictionary.keys():
                list1.append(c)
            else:
                if list1:
                    if (dictionary[list1[-1]]==c):
                        list1.pop()
                    else:
                        return False
                else:
                    return False         
        return len(list1)==0