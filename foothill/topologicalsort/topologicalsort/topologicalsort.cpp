#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <map>
#include <queue>

using std::map;
using std::queue;
using std::pair;
using std::make_pair;
using std::vector;
using std::string;
using std::cout;
using std::endl;

struct Vertex {
   Vertex(string nameCtr) : name(nameCtr) {
      inDegree = 0;
      topSortRank = 0;
   }
   int inDegree;
   int topSortRank;
   string name;
};

struct DirectedEdge {
   DirectedEdge(Vertex* sourceCtr, Vertex* targetCtr) : source(sourceCtr), target(targetCtr) {}
   Vertex* source;
   Vertex* target;
};

int main() {
   Vertex v1 = Vertex("v1");
   Vertex v2 = Vertex("v2");
   Vertex v3 = Vertex("v3");
   Vertex v4 = Vertex("v4");
   Vertex v5 = Vertex("v5");
   Vertex v6 = Vertex("v6");
   Vertex v7 = Vertex("v7");

   DirectedEdge edge12 = DirectedEdge(&v1, &v2);
   DirectedEdge edge13 = DirectedEdge(&v1, &v3);
   DirectedEdge edge14 = DirectedEdge(&v1, &v4);

   DirectedEdge edge24 = DirectedEdge(&v2, &v4);
   DirectedEdge edge25 = DirectedEdge(&v2, &v5);

   DirectedEdge edge36 = DirectedEdge(&v3, &v6);

   DirectedEdge edge43 = DirectedEdge(&v4, &v3);
   DirectedEdge edge45 = DirectedEdge(&v4, &v5);
   DirectedEdge edge46 = DirectedEdge(&v4, &v6);
   DirectedEdge edge47 = DirectedEdge(&v4, &v7);

   DirectedEdge edge57 = DirectedEdge(&v5, &v7);

   DirectedEdge edge76 = DirectedEdge(&v7, &v6);

   vector<Vertex*> vertices = { &v1, &v2, &v3, &v4, &v5, &v6, &v7 };
   vector<DirectedEdge> edges = { edge12, edge14, edge24, edge25, edge13, edge36, edge43, edge45, edge46, edge47, edge57, edge76 };

   // build adjacency list graph representation
   map<string, vector<Vertex*> > adjacencyList;

   for (DirectedEdge edge : edges) {
      adjacencyList[edge.source->name].push_back(edge.target);
      ++edge.target->inDegree;
   }

   vector<Vertex*> topSortedVertices;

   queue<Vertex*> q;
   int counter = 0;
   
   // enqueue indegree 0 vertices, first in rank for topological sort
   for (Vertex* v : vertices) {
      if (v->inDegree == 0) {
         q.push(v);
      }
   }

   while (!q.empty()) {
      Vertex* v = q.front();
      q.pop();
      v->topSortRank = counter++;

      topSortedVertices.push_back(v);

      for (Vertex* adj : adjacencyList[v->name]) {
         if (--adj->inDegree == 0) {
            q.push(adj);
         }
      }
   }

   for (Vertex* v : topSortedVertices) {
      cout << v->name << ", " << v->topSortRank << endl;
   }

   return 0;
}