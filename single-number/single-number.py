class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mySet = list(set(nums))
        myCounts = []
        for n in mySet:
            myCounts.append(nums.count(n))
        return(mySet[myCounts.index(min(myCounts))])