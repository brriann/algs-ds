
#include <iostream>
#include "Maze.h"
#include "Random.h"
#include "UnionFind.h"

using std::cout;

// UTILITY VARIABLES AND FUNCTIONS
const int MAZE_WIDTH = 60;
const int MAZE_HEIGHT = 20;

int convert2dIdxTo1dIdx(int row, int col) {
   int asdf = (row * MAZE_WIDTH) + col;
   return asdf;
}

int main()
{
   Maze maze = Maze(MAZE_HEIGHT, MAZE_WIDTH);
   UnionFind uf = UnionFind(MAZE_HEIGHT * MAZE_WIDTH);
   Random rand = Random();
   cout << maze.print();
   int counter = 0;
   while (!uf.twoCellsConnected(convert2dIdxTo1dIdx(0, 0), convert2dIdxTo1dIdx(MAZE_HEIGHT - 1, MAZE_WIDTH - 1))) { // !uf.allCellsConnected()
      // pick a random cell
      int rowSource = rand.getInt(MAZE_HEIGHT - 1);
      int colSource = rand.getInt(MAZE_WIDTH - 1);

      // pick random [right/down]
      bool connectRight = (rand.getInt(1) == 1); // 0 down, 1 right...

      // escape out of bounds cases
      if ((connectRight && colSource == MAZE_WIDTH - 1)
         || (!connectRight && rowSource == MAZE_HEIGHT - 1)) {
         continue;
      }


      int rowTarget = connectRight ? rowSource : rowSource + 1;
      int colTarget = connectRight? colSource + 1 : colSource;

      // if cell and cell to the [right/down] aren't connected
      if (!uf.twoCellsConnected(convert2dIdxTo1dIdx(rowSource, colSource), convert2dIdxTo1dIdx(rowTarget, colTarget))) {
         // set connected[right/down] to true on the target cell
         maze.setCellConnected(rowSource, colSource, connectRight);
         // and join the cells in unionfind data structure
         uf.unionTwoCells(convert2dIdxTo1dIdx(rowSource, colSource), convert2dIdxTo1dIdx(rowTarget, colTarget));
      }
      cout << maze.print();
      ++counter;
   }
   cout << endl << endl;
   cout << maze.print();

   return 0;
}
