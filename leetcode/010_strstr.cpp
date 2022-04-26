#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

// https://leetcode.com/problems/implement-strstr/
class Solution {
public:
    int strStr(string haystack, string needle) {
        // corner case: needle is empty string, return 0
        if (needle.empty()) {
            return 0;
        }
        int haystackLength = haystack.length();
        int needleLength = needle.length();
        int diff = haystackLength - needleLength;
        for (int i = 0; i <= diff; ++i) {
            int idx = 0;
            while (idx < needleLength && haystack[i + idx] == needle[idx]) {
                idx++;
            }
            // did we find the whole needle?
            if (idx == needleLength) {
                return i;
            }
        }
        // didn't find needle in haystack
        return -1;
    }
};

int main() {
    string needle = "longneedle";
    string haystack = "long";
    Solution sol = Solution();
    cout << sol.strStr(haystack, needle) << endl;
    return 0;
}