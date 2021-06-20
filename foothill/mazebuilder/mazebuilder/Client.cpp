
#include <iostream>
#include "Maze.h"
#include "Random.h"
#include "UnionFind.h"


// UTILITY VARIABLES AND FUNCTIONS
const int MAZE_WIDTH = 10;
const int MAZE_HEIGHT = 10;

int convert2dIdxTo1dIdx(int row, int col) {
   return (row * MAZE_WIDTH) + col;
}

int main()
{
   Maze maze = Maze(MAZE_HEIGHT, MAZE_WIDTH);
   UnionFind uf = UnionFind(MAZE_HEIGHT * MAZE_WIDTH);
   std::cout << maze.print();
   while (!uf.allCellsConnected()) {
      // pick a random cell
      // pick random [right/down]

   }

   return 0;
}
