
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::stringstream;
using std::stoi;

// CLI expected format "./a.out 1-2-3/4-5-6/7-8-9"
// to represent the file format:
// 1 2 3
// 4 5 6
// 7 8 9

vector<int> splitStringToInts(string);

int main (int argc, char **argv)
{
    cout << "args: " << (argc - 1) << endl;

    if ((argc - 1) > 0)
    {
        cout << "argv:\n";
        for (int i = 1; i < argc; i++)
        {
            cout << argv[i] << endl;
        }
        vector<int> splitArg1 = splitStringToInts(argv[1]);
        for (int s : splitArg1)
        {
            cout << s << endl;
        }
    }
    else
    {
        cout << "no args, using file...\n";
        // TODO: file reader
    }
    
    
    return 0;
}

vector<int> splitStringToInts(string delimitedString)
{
    stringstream ss(delimitedString);
    vector<int> intVector;
    string temp;
    while(getline(ss, temp, '-'))
    {
        intVector.push_back(stoi(temp));
    }
    return intVector;
}