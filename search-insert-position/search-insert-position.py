class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: return(nums.index(target))
        sorted(nums)
        myIndex = 0
        for n in nums:
            if n>target: 
                return(myIndex)
            myIndex+=1
        return(len(nums))