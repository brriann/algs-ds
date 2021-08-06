//#include <stack>
//#include <iostream>
//
//using std::stack;
//using std::cout;
//using std::endl;
//
//// O(n^2)
//void stack_sort(stack<int>& source, stack<int>& target) {
//   // O(n)
//   while (!source.empty()) {
//      int sourceTop = source.top();
//      source.pop();
//      
//      int numMoved = 0;
//
//      // O(n)
//      while (!target.empty() && target.top() < sourceTop) {
//         source.push(target.top());
//         target.pop();
//         numMoved++;
//      }
//
//      target.push(sourceTop);
//
//      for (int i = 0; i < numMoved; ++i) {
//         target.push(source.top());
//         source.pop();
//      }
//   }
//}
//
//int main()
//{
//   stack<int> source;
//   stack<int> target;
//
//   source.push(4);
//   source.push(7);
//   source.push(2);
//   source.push(-1);
//   source.push(3);
//   source.push(-24);
//
//   stack_sort(source, target);
//
//   while (!target.empty()) {
//      cout << target.top() << endl;
//      target.pop();
//   }
//
//   return 0;
//}