
#include <iostream>

using std::cout;

int main (int argc, char **argv)
{
    cout << "hello world!\n";
    cout << "argc: " << argc << std::endl;

    if (argc > 0)
    {
        for (int i = 1; i < argc; i++)
        {
            cout << argv[i] << std::endl;
        }
    }
    return 0;
}