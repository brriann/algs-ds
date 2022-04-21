#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; ++i) {
        // for (vector<int>::iterator it = nums.begin(); it != nums.end(); ++it) {
            int currentValue = nums[i];
            int peek = i + 1;
            while (nums[peek] == nums[i] && peek < nums.size() - 1) {
                ++peek;
            }
            // if peek iterator has advanced, aka, found dupes
            if (peek != i + 1) {
                //remove (it, peek)
                nums.erase(nums.begin() + i + 1, nums.begin() + peek);
                //nums.erase(it + 1, peek - 1);
            }
        }
        return nums.size();
    }
};

int main() {
    Solution s = Solution();
    vector<int> test2 = { 1, 1 }; // TODO, fix behavior in this corner case
    vector<int> test1 = { 3, 3, 3, 7, 7, 8, 9, 9, 9 };
    s.removeDuplicates(test2);

    for (vector<int>::iterator it = test2.begin(); it != test2.end(); ++it) {
        cout << (*it) << endl;
    }
    return 0;
}