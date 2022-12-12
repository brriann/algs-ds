#include <stack>
#include <map>
#include <iostream>
#include <string>

using std::stack;
using std::map;
using std::string;
using std::cout;
using std::endl;

// https://leetcode.com/problems/valid-parentheses/
class Solution {
public:
    bool isValid(string s) {
        // keys = openers, values = closers
        map<char, char> openParens = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'},
        };

        stack<char> encountered;

        for (int i = 0; i < s.length(); ++i) {
            if (openParens.count(s[i]) > 0) {
                encountered.push(s[i]);
                continue;
            }
            // s[i] is a closer
            if (encountered.empty()) {
                // no valid opener match
                return false;
            }
            char previousOpener = encountered.top();
            if (s[i] != openParens[previousOpener]) {
                // opener-closer mismatch
                return false;
            }
            // valid opener-closer match
            encountered.pop();
        }
        return encountered.empty();
    }
};

// client
int main() {
    Solution s = Solution();
    string string0 = "]";
    string string1 = "()[]{}";
    string string2 = "(([[{{{}}}]]))";
    string string3 = "([[}])";
    string string4 = "(()";
    cout << s.isValid(string0) << endl;
    cout << s.isValid(string1) << endl;
    cout << s.isValid(string2) << endl;
    cout << s.isValid(string3) << endl;
    cout << s.isValid(string4) << endl;
    return 0;
}
