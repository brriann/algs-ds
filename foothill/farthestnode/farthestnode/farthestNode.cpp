#include <iostream>
#include <vector>
#include <string>
#include <utility>

using std::pair;
using std::make_pair;
using std::vector;
using std::string;
using std::cout;
using std::endl;

struct Vertex {
   Vertex(string nameCtr) : name(nameCtr) {
      known = false;
      dist = 1000000; // infinity
      path = nullptr;
   }
   string name;
   vector<pair<Vertex*, int> > adjacents; // with distance
   bool known;
   int dist;
   Vertex* path; // previous node
};

struct Graph {
   Graph(vector<Vertex*> verticesCtr) {
      for (Vertex* v : verticesCtr) {
         vertices.push_back(v);
      }
   }
   bool unknownVertexExists() {
      for (Vertex* v : vertices) {
         if (v->known == false) {
            return true;
         }
      }
      return false;
   }
   Vertex* unknownVertexWithSmallestDistance() {
      Vertex* minVertex = nullptr;
      int minDist = 999999999;
      for (Vertex* v : vertices) {
         if (!(v->known) && v->dist < minDist) {
            minVertex = v;
            minDist = v->dist;
         }
      }
      return minVertex;
   }
   vector<Vertex*> vertices;
};

void printPath(Vertex* v) {
   if (v->path != nullptr) {
      printPath(v->path);
      cout << " to ";
   }
   cout << v->name;
}

// graph image on page 394 Weiss CS2C textbook

int main() {
   Vertex v1 = Vertex("v1");
   Vertex v2 = Vertex("v2");
   Vertex v3 = Vertex("v3");
   Vertex v4 = Vertex("v4");
   Vertex v5 = Vertex("v5");
   Vertex v6 = Vertex("v6");
   Vertex v7 = Vertex("v7");

   v1.adjacents.push_back(make_pair<Vertex*, int>(&v2, 2));
   v1.adjacents.push_back(make_pair<Vertex*, int>(&v4, 1));

   v2.adjacents.push_back(make_pair<Vertex*, int>(&v4, 3));
   v2.adjacents.push_back(make_pair<Vertex*, int>(&v5, 10));

   v3.adjacents.push_back(make_pair<Vertex*, int>(&v1, 4));
   v3.adjacents.push_back(make_pair<Vertex*, int>(&v6, 5));

   v4.adjacents.push_back(make_pair<Vertex*, int>(&v3, 2));
   v4.adjacents.push_back(make_pair<Vertex*, int>(&v5, 2));
   v4.adjacents.push_back(make_pair<Vertex*, int>(&v6, 8));
   v4.adjacents.push_back(make_pair<Vertex*, int>(&v7, 4));

   v5.adjacents.push_back(make_pair<Vertex*, int>(&v7, 6));

   v7.adjacents.push_back(make_pair<Vertex*, int>(&v6, 1));

   vector<Vertex*> vertices = { &v1, &v2, &v3, &v4, &v5, &v6, &v7 };
   Graph graph = Graph(vertices);

   // find farthest node from v1, v3.  no matter what path taken
   // determine shortest path from v3 to all nodes
   // node with farthest, shortest path, will be the farthest node

   // expected: v1 --> v6 via v1,4,7,6 @ cost 6
   // expected: v3 --> v7 via v3,1,4,7 @ cost 9

   // set start vertex as known
   v3.dist = 0;

   // run Dijkstra's algorithm until all vertices are known
   // NOT using a priority queue for this implementation of Dijkstra's

   while (graph.unknownVertexExists()) {
      Vertex* v = graph.unknownVertexWithSmallestDistance();
      v->known = true;

      for (pair<Vertex*, int> adj : v->adjacents) {
         if (!(adj.first->known)) {
            int cvw = adj.second;

            if (v->dist + cvw < adj.first->dist) {
               // update w, the adjacent vertex
               adj.first->dist = v->dist + cvw;
               adj.first->path = v;
            }
         }
      }
   }

   // iterate through Vertices and find the node with largest distance, return that node
   Vertex* maxDistVertex = graph.vertices.front();
   for (auto& v : graph.vertices) {
      if (v->dist > maxDistVertex->dist) {
         maxDistVertex = v;
      }
   }

   cout << "The farthest node is " << maxDistVertex->name << ", at a distance of " << maxDistVertex->dist << endl;
  printPath(maxDistVertex);

   return 0;
}