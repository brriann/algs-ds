#pragma once

#ifndef UnionFind_h
#define UnionFind_h

#include <vector>

using std::vector;

class UnionFind {
public:
   UnionFind(int capacityCtr) : capacity(capacityCtr) {
      for (int i = 0; i < capacityCtr; ++i) {
         // assign each element as its own parent/root
         dataStruct.push_back(i);
      }
   }
   void unionTwoCells(int a, int b) {
      if (a < b) {
         dataStruct[unionFindParent(b)] = unionFindParent(a);
      }
      else {
         dataStruct[unionFindParent(a)] = unionFindParent(b);
      }
   }
   bool twoCellsConnected(int a, int b) {
      return unionFindParent(a) == unionFindParent(b);
   }
   bool allCellsConnected() {
      for (int i = 0; i < capacity - 1; ++i) {
         if (dataStruct[i] != dataStruct[i + 1]) {
            return false;
         }
      }
      return true;
   }
private:
   vector<int> dataStruct;
   int capacity;
   int unionFindParent(int child) {
      while (dataStruct[child] != child) {
         child = dataStruct[child];
      }
      return child;
   }
};

#endif // UnionFind_h