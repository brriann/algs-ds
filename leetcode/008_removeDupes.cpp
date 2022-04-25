#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // handle [] or [1] corner cases
        if (nums.size() < 2) {
            // no dupe removal needed
            return nums.size();
        }
        for (int i = 0; i < nums.size() - 1; ++i) {
            int peek = i + 1;
            if (nums[i] != nums[peek]) {
                // no dupes
                continue;
            }
            while (peek < nums.size() && nums[peek] == nums[i]) {
                ++peek;
            }
            nums.erase(nums.begin() + i + 1, nums.begin() + peek);
        }
        return nums.size();
    }
};

int main() {
    Solution s = Solution();
    vector<int> test3 = { 1, 2 };
    vector<int> test2 = { 1, 1 };
    vector<int> test1 = { 3, 3, 3, 7, 7, 8, 9, 9, 9 };
    vector<int> test = test1;
    s.removeDuplicates(test);

    for (vector<int>::iterator it = test.begin(); it != test.end(); ++it) {
        cout << (*it) << endl;
    }
    return 0;
}