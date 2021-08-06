#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int reverse(int x) {

   int answer = 0;
   int places = 0;
   while (x != 0) {
      answer = answer * 10 + x % 10;
      x /= 10;
      ++places;
   }
   if (places == 10) {
      // compare reversed digits to 2^32, if greater, return 0
   }
   return answer;
}

int main()
{
   int toReverse = 1234;
   cout << reverse(toReverse);

   return 0;
}