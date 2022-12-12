#include <iostream>
#include <string>
#include <vector>

using std::vector;
using std::max;
using std::cout;
using std::endl;
using std::string;

// https://leetcode.com/problems/length-of-last-word/

class Solution {
    public:
        int lengthOfLastWord(string s) {
            char space = ' ';
            vector<string> subStrings;

            // split string into vector of sub-strings
            size_t pos = 0;
            string subString;
            while ((pos = s.find(space)) != std::string::npos) { // BUG won't grab last word in string, if string ends in non-space
                subString = s.substr(0, pos);
                subStrings.push_back(subString);
                s.erase(0, pos + 1); // space delimiter has 1 character length
            }
            
            string lastString = subStrings.back();
            return lastString.length();
        }
};

int main() {
    Solution s = Solution();

    string test1 = "This is crazy";
    string test2 = " is apples   ";

    vector<string> testRuns = { test1, test2 };
    for (int i = 0; i < testRuns.size(); ++i) {
        int result = s.lengthOfLastWord(testRuns[i]);
        cout << result << endl;
    }

    return 0;
}