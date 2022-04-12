#include <vector>
#include <iostream>
#include <map>
#include <string>

using std::string;
using std::map;
using std::vector;
using std::cout;
using std::endl;

// https://leetcode.com/problems/roman-to-integer/
class Solution {
public:
    int romanToInt(string s) {
        return romanToIntOptimized(s);
    }
private:
    int romanToIntNaive(string s) {
        map<char, int> singles = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };

        map<char, map<char, int>> doubles = {
            {'I', {
                {'V', 4},
                {'X', 9}
            }},
            {'X', {
                {'L', 40},
                {'C', 90}
            }},
            {'C', {
                {'D', 400},
                {'M', 900}
            }}
        };

        int result = 0;

        for (int i = 0, j = s.length(); i < j; ++i) {
            if (doubles.count(s[i]) > 0 
            && doubles[s[i]].count(s[i + 1]) > 0) {
                result += doubles[s[i]][s[i + 1]];
                // skip ahead one, we doubled up
                ++i;
            }
            else {
                result += singles[s[i]];
            }
        }

        return result;
    }
    int romanToIntOptimized(string s) {
        map<char, int> singles = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000},
        };
        int result = 0;
        // iterate from back to front
        for (int i = s.length() - 1; i >= 0; --i) {
            result += singles[s[i]];
            // if smaller number is ahead of bigger, subtract the smaller (IX)
            if (i > 0 && singles[s[i - 1]] < singles[s[i]]) {
                result -= singles[s[i - 1]];
                --i;
            }
        }

        return result;
    }
};

int main() {
    Solution s = Solution();
    int result = s.romanToInt("MCMXCIV");
    cout << result << endl;
    return 0;
}