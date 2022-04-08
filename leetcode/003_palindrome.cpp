#include <string>
#include <iostream>

using std::cout;
using std::endl;
using std::string;

// https://leetcode.com/problems/palindrome-number
class Solution {
public:
    bool isPalindrome(int x) {
        return isPalindromeConvertToString(x);
    }
private:
    bool isPalindromeConvertToString(int x) {
        string s = std::to_string(x);
        int length = s.size();
        for (
            int i = 0, j = length - 1;
            i <= j;
            ++i, --j
        ) {
            if (s[i] != s[j]) {
                return false;
            }
        }
        // backwards and forwards iterators have made it through the string
        // no inequalities were found
        return true;
    }
    bool isPalindromeOptimized(int x) {
        return false; // TODO
    }
};

int main() {
    Solution s = Solution();
    bool result = s.isPalindrome(12344321);
    string report = result ? "pali!" : "nope";
    cout << report << endl;
    return 0;
}