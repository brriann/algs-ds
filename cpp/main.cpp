
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

const string INPUT_FILE_PATH = "./../input/7insertionsort1.txt";

int main (int argc, char **argv)
{
    cout << "args: " << (argc - 1) << endl;
    vector<vector<int>> vector2d;
    if ((argc - 1) > 0)
    {
        cout << "argv:\n";
        for (int i = 1; i < argc; i++)
        {
            cout << argv[i] << endl;
        }

        vector2d = readArgTo2dVector(argv[1]);
        
    }
    else
    {
        cout << "no args, using file...\n";
        
        vector2d = readFileTo2dVector(INPUT_FILE_PATH);
    }

    for (vector<int> vi : vector2d)
    {
        for (int i : vi)
        {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}



