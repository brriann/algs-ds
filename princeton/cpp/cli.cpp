#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using std::string;
using std::vector;
using std::stringstream;

namespace utils
{
    const char ROW_DELIMITER = '/';
    const char CELL_DELIMITER = '-';

    vector<vector<int>> readArgTo2dVector(string delimitedString)
    {
        vector<vector<int>> vvi;
        stringstream ss(delimitedString);
        string rowTemp;
        while(getline(ss, rowTemp, ROW_DELIMITER))
        {
            vector<int> rowVector;
            stringstream ssRow(rowTemp);
            string cellTemp;
            while(getline(ssRow, cellTemp, CELL_DELIMITER))
            {
                rowVector.push_back(stoi(cellTemp));
            }
            vvi.push_back(rowVector);
        }
        return vvi;
    }
}
