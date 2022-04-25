#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for (int i = 0; i < nums.size(); ++i) {
            while (i < nums.size() && nums[i] == val) {
                // swap ith elt with last elt
                nums[i] = nums[nums.size() - 1];
                // pop last elt
                nums.pop_back();
            }
        }
        return nums.size();
    }
};

int main () {
    vector<int> test1 = { 1, 1, 2, 2, 3};
    vector<int> test2 = { 1, 3, 2, 2, 2};
    vector<int> test3 = {};
    vector<int> test4 = { 1 };
    vector<int> test5 = { 2, 2, 2, 2, 2 };

    int val = 2;
    vector<int> test = test5;
    Solution sol = Solution();

    cout << sol.removeElement(test, val) << endl;
    for (int i = 0; i < test.size(); ++i) {
        cout << test[i] << endl;
    }
    return 0;
}