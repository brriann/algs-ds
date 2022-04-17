#include <vector>
#include <iostream>
#include <iostream>
#include <iterator>

using std::string;
using std::vector;
using std::cout;
using std::endl;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string commonPrefix = strs[0];
        for (
            int i = 1;
            i < strs.size();
            ++i
        ) {
            int index = 0;
            while (
                index < commonPrefix.size() 
                && index < strs[i].size() 
                && strs[i][index] == commonPrefix[index]
            ) {
                index++;
            }
            commonPrefix = strs[i].substr(0, index);
        }
        return commonPrefix;
    }
};

// client
int main() {
    vector<string> strings = {"flowers", "flow", "flight"};
    vector<string> strings1 = {"race", "dog", "racecar"};
    vector<string> strings2 = {"ab", "a"};
    vector<string> strings3 = {"a", "ab"};
    Solution s = Solution();
    cout << s.longestCommonPrefix(strings) << endl;
    cout << s.longestCommonPrefix(strings1) << endl;
    cout << s.longestCommonPrefix(strings2) << endl;
    cout << s.longestCommonPrefix(strings3) << endl;
    return 0;
}