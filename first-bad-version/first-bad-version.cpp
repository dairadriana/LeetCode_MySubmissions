// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int right = n, left = 1;
        while (left < right){
            int pivot = left + (right-left)/2;
            if (isBadVersion(pivot)){
                right = pivot;
            }
            else {
                left = pivot + 1;
            }
        }
        return left;
    }
};