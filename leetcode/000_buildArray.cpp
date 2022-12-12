#include <iostream>
#include <vector>

using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> result;
        
        for (int i = 0; i < nums.size(); ++i) {
            result.push_back(nums[nums[i]]);    
        }
        
        return result;
    }
};

int main()
{
    vector<int> num1 = { 5, 6, 4, 3, 1, 2, 0 };
    Solution s = Solution();
    vector<int> result = s.buildArray(num1);
    for (vector<int>::iterator it = result.begin(); it != result.end(); ++it) {
        cout << *it << endl;
    }
}