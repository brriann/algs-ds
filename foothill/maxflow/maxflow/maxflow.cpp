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
      outDegree = 0;
   }
   Vertex(Vertex& vertexCtr) : inDegree(vertexCtr.inDegree), outDegree(vertexCtr.outDegree), name(vertexCtr.name) {}
   int inDegree;
   int outDegree;
   string name;
};

struct DirectedEdge {
   DirectedEdge(Vertex* sourceCtr, Vertex* targetCtr) : source(sourceCtr), target(targetCtr) {}
   Vertex* source;
   Vertex* target;
};

struct Graph {
   vector<Vertex*> vertices;
   vector<DirectedEdge> edges;
   map<string, vector<Vertex*> > adjacencyList;
};

struct ResidualGraph {
   vector<Vertex*> vertices;
   vector<DirectedEdge> edges;
   map<string, vector<Vertex*> > adjacencyList;
   map<string, vector<Vertex*> > residualAdjacencyList;
};

int main() {

   return 0;
}