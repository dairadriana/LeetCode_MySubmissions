class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output=[]
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l = j+1
                r = len(nums) - 1
                while l < r:
                    s_quadlet=[nums[i], nums[j], nums[l], nums[r]]
                    if sum(s_quadlet) == target and s_quadlet not in output:
                        output.append(s_quadlet)
                    elif sum(s_quadlet) > target:
                        r-=1
                    else:
                        l+=1
        return output