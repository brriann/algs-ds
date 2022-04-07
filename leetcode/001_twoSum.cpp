#include <iostream>
#include <vector>
#include <map>

using std::map;
using std::vector;
using std::cout;
using std::endl;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        return twoSumON(nums, target);
    }
private:
    vector<int> twoSumONSquared(vector<int>& nums, int target) {
        vector<int> result;

        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i + 1; j < nums.size(); ++j) {
                if (nums[i] + nums[j] == target) {
                    result.push_back(i);
                    result.push_back(j);
                }
            }
        }
        return result;
    }
    vector<int> twoSumON(vector<int>& nums, int target) {
        vector<int> result;

        map<int, vector<int>> eltIdxMap;
        // populate map of elt:[idx] O(n)
        for (int i = 0; i < nums.size(); ++i) {
            eltIdxMap[nums[i]].push_back(i);
        }
        // iterate over collection O(n)
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            // std::map.count() O(log(n))
            if (eltIdxMap.count(complement) > 0) {
                // if we have found the elt "itself"
                if (nums[i] == complement && eltIdxMap[complement].size() == 1) {
                    continue;
                }
                result.push_back(i);
                // if target = 2 * nums[i], eg, target = 6, nums[i] = 3
                if (i == eltIdxMap[complement][0]) {
                    // since we can't use the same elt twice, and there's only one possible pair,
                    // there must be 2 idx's in the collection, so ... take the 2nd one.
                    result.push_back(eltIdxMap[complement][1]);
                }
                else {
                    // otherwise, we've found the other matching partner
                    result.push_back(eltIdxMap[complement][0]);
                }
                return result;
            }
        }
        return result;
    }
};

int main()
{
    vector<int> nums1 = { 3, 2, 4};
    int target1 = 6;
    Solution s = Solution();
    vector<int> result = s.twoSum(nums1, target1);
    cout << " Result indices are: " << result[0] << " and " << result[1] << endl;
    return 0;
}