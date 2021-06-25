class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dic = {}
        maxi = 0
        for n in nums:
            if n not in my_dic.keys():
                my_dic[n] = 1
            else:
                my_dic[n] += 1
        max_key = max(my_dic, key = my_dic.get)
        return max_key