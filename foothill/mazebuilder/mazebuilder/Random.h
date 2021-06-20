#pragma once

#ifndef Random_h
#define Random_h

#include <random>

using std::default_random_engine;
using std::uniform_int_distribution;

class Random {
public:
   Random() {}
   int getInt(int max) {
      default_random_engine dre;
      uniform_int_distribution<int> uniform_dist(0, max);
      return uniform_dist(dre);
   }
private:
};

#endif // Random_h