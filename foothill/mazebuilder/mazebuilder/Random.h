#pragma once

#ifndef Random_h
#define Random_h

#include <random>
#include <chrono>

using std::default_random_engine;
using std::uniform_int_distribution;

class Random {
public:
   Random() {}
   // on interval [0, max]
   int getInt(int max) {
      default_random_engine dre;
      dre.seed(std::chrono::system_clock::now().time_since_epoch().count());
      uniform_int_distribution<int> uniform_dist(0, max);
      return uniform_dist(dre);
   }
private:
};

#endif // Random_h