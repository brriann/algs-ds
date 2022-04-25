#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

class Solution {
public:
    int strStr(string haystack, string needle) {
        for (int i = 0; i < haystack.length(); ++i) { // only iterator to haystack - needle
            int idx = 0;
            while (haystack[i + idx] == needle[idx]) {
                idx++;
            }
            // did we find the whole needle?
        }
        // didn't find needle in haystack
        return -1;
    }
};

int main() {
    string needle = "ll";
    string haystack = "hello";
    Solution sol = Solution();
    cout << sol(haystack, needle); << endl;
    return 0;
}