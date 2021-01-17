#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>

using std::string;
using std::vector;
using std::ifstream;
using std::stringstream;

namespace utils
{
    const char LINE_DELIMITER = ' ';
    
    vector<vector<int>> readFileTo2dVector(string filePath)
    {
        vector<vector<int>> vvi;
        string lineTemp;
        ifstream inputFile(filePath);
        if (inputFile.is_open())
        {
            while (getline(inputFile, lineTemp))
            {
                vector<int> lineVector;
                stringstream ssLine(lineTemp);
                string cellTemp;
                while (getline(ssLine, cellTemp, LINE_DELIMITER))
                {
                    lineVector.push_back(stoi(cellTemp));
                }
                vvi.push_back(lineVector);
            }
            inputFile.close();
        }
        return vvi;
    }
}