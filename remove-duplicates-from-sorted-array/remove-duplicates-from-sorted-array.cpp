class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> removed;
        for (int i=0; i<nums.size(); i++){
            if (!count(removed.begin(), removed.end(), nums[i])){
                removed.push_back(nums[i]);
            }
        }
        for (int i=0; i<removed.size(); i++){
            nums[i] = removed[i];
        }
        return removed.size();
    }
    
};