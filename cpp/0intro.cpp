
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

#include "cli.h"
#include "file.h"

using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::stringstream;
using std::stoi;

using utils::readArgTo2dVector;
using utils::readFileTo2dVector;

// CLI expected format "./a.out 1-2-3/4-5-6/7-8-9"
// to represent the file format:
// 1 2 3
// 4 5 6
// 7 8 9

const string INPUT_FILE_PATH = "./../input/0intro1.txt";

void runClient(vector<vector<int>> inputs);

int main (int argc, char **argv)
{
    if (argc > 1)
    {
        runClient(readArgTo2dVector(argv[1]));
    }
    else
    {
        runClient(readFileTo2dVector(INPUT_FILE_PATH));
    }

    return 0;
}

void runClient(vector<vector<int>> inputs)
{
    cout << "\nA.) Full 2D Vector\n";
    for (vector<int> vi : inputs)
    {
        for (int i : vi)
        {
            cout << i << " ";
        }
    }
    cout << "\n\nB.) Each Row\n";
    for (vector<int> vi : inputs)
    {
        for (int i : vi)
        {
            cout << i << " ";
        }
        cout << endl;
    }
    cout << "\nC.) Each Cell\n";
    for (vector<int> vi : inputs)
    {
        for (int i : vi)
        {
            cout << i << endl;
        }
    }
}
