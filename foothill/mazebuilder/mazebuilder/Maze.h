#pragma once

#ifndef Maze_h
#define Maze_h

#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using std::vector;
using std::string;
using std::stringstream;
using std::endl;

const string BOTTOM_BORDER = "___";
const string SIDE_BORDER = "|";
const string CELL_SPACE = "  ";

class Maze {
public:
   Maze(int heightCtr, int widthCtr) : height(heightCtr), width(widthCtr) {
      for (int i = 0; i < height; ++i) {
         vector<MazeCell> mazeRow;
         for (int j = 0; j < width; ++j) {
            MazeCell cell;
            mazeRow.push_back(cell);
         }
         mazeGrid.push_back(mazeRow);
      }
      mazeGrid[height - 1][width - 1].connectedDown = true; // empty for print, exit bottom right
   }
   string print() {
      stringstream ss;
      // print top border
      ss << "   "; // empty - start at top left
      for (int i = 1; i < width; ++i) {
         ss << BOTTOM_BORDER;
      }
      ss << endl;
      // print each row
      for (int i = 0; i < height; ++i) {
         // print each cell - connectedRight or |
         for (int j = 0; j < width; ++j) {
            ss << CELL_SPACE << (mazeGrid[i][j].connectedRight ? " " : SIDE_BORDER);
         }
         ss << endl;
         // print each cell lower border - connectedDown or _
         for (int j = 0; j < width; ++j) {
            ss << "" << (mazeGrid[i][j].connectedDown ? "" : BOTTOM_BORDER);
         }
         ss << endl;
      }
      return ss.str();
   }
   void setCellConnected(int row, int col, bool connectRight) {
      if (connectRight) {
         mazeGrid[row][col].connectedRight = true;
      }
      else {
         mazeGrid[row][col].connectedDown = true;
      }
   }

private:
   struct MazeCell {
      MazeCell() {
         connectedRight = false;
         connectedDown = false;
      }
      bool connectedRight;
      bool connectedDown;
   };
   vector<vector<MazeCell> > mazeGrid;
   int width;
   int height;
};

#endif // Maze_h