#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            int mid = (high + low) / 2;
            if (nums[mid] < target) {
                low = mid + 1; // search higher
            }
            else if (nums[mid] > target) {
                high = mid - 1; // search lower
            }
            else { // nums[mid] == target
                return mid;
            }
        }
        return low;
    }
};

int main() {
    vector<int> test1=  { 1, 2, 4, 6, 7 };
    int target1 = 5;

    vector<int> test = test1;
    int target = target1;

    Solution sol = Solution();
    cout << sol.searchInsert(test, target) << endl;
    return 0;
}