#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;
using std::max;

// https://leetcode.com/problems/maximum-subarray/

// TODO, redo with divide-and-conquer algo.  this approach is O(n)

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        int sum = nums[0];
        int maxSum = nums[0];
        int vectorLength = nums.size();

        for (int i = 1; i < vectorLength; ++i) {
            sum += nums[i];

            sum = max(sum, nums[i]);
            maxSum = max(sum, maxSum);
        }

        return maxSum;
    }
    
};

int main() {
    Solution s = Solution();
    
    vector<int> test1 = { 1 }; // constraint: 1 <= nums.length
    vector<int> test2 = { 1, 1 };
    vector<int> test3 = { -1, 1 };
    vector<int> test4 = { 1, 1, -3, 3 };
    vector<int> test5 = { 3, -4, 2 };
    vector<int> test6 = { -1 };
    vector<int> test7 = { -1, -2 };
    vector<int> test8 = { -2, -1 };
    vector<int> test9 = { -2, 1 };

    vector<vector<int>> testRuns = { test1, test2, test3, test4, test5, test6, test7, test8, test9 };

    for (int i = 0; i < testRuns.size(); ++i) {
        int result = s.maxSubArray(testRuns[i]);
        cout << result << endl;
    }
    
    return 0;
}