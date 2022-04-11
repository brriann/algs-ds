#include <string>
#include <vector>
#include <iostream>

using std::vector;
using std::cout;
using std::endl;
using std::string;

// https://leetcode.com/problems/palindrome-number
class Solution {
public:
    bool isPalindrome(int x) {
        return isPalindromeOptimal(x);
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
    bool isPalindromeNoStringConvert(int x) {
        if (x < 0) { return false; }

        vector<int> numbers;

        while (x > 0) {
            numbers.push_back(x % 10);
            x = x / 10;
        }

        vector<int>::iterator it1 = numbers.begin();
        vector<int>::reverse_iterator it2 = numbers.rbegin();
        for (
            ;
            it1 != numbers.end(), it2 != numbers.rend();
            ++it1, ++it2
        ) {
            if (*it1 != *it2) {
                return false;
            }
        }
        // backwards and forwards iterators have made it through the vector<int> of digits
        // no inequalities were found
        return true;
    }
    bool isPalindromeOptimal(int x) {
        long long int y = 0;
        int orig = x;

        // build the number backwards, digit-by-digit
        while (x > 0) {
            y = (y * 10) + (x % 10);
            x = x / 10;
        }

        if (y == orig) {
            return true;
        }

        return false;
    }
};

int main() {
    Solution s = Solution();
    bool result = s.isPalindrome(12344321);
    string report = result ? "pali!" : "nope";
    cout << report << endl;
    return 0;
}