#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

// https://leetcode.com/problems/maximum-subarray/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = 0;
        int sum = 0;
        bool tracking = false;
        for (int i = 0; i < nums.size(); ++i) {
            // if not tracking, don't include negatives
            if (!tracking && nums[i] < 0) {
                continue;
            }
            // if tracking, and encounter a negative bigger than previous tracked sum, reset
            if (tracking && nums[i] < 0 && (sum + nums[i]) < 0) {
                if (sum > maxSum) {
                    maxSum = sum;
                }
                tracking = false;
                sum = 0;
                continue;
            }

            tracking = true;
            sum += nums[i];

            if (sum > maxSum) {
                maxSum = sum;
            }
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

    int result = s.maxSubArray(test6);
    cout << result << endl;
}