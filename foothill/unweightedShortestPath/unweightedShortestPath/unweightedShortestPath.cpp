#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <map>
#include <queue>
#include <sstream>

using std::stringstream;
using std::map;
using std::queue;
using std::pair;
using std::make_pair;
using std::vector;
using std::string;
using std::cout;
using std::endl;
using std::reverse;

const int INFINITY_NUMBER = 999999;

struct Vertex {
   Vertex(string nameCtr) : name(nameCtr) {
      pathDistance = -1;
      pathPrevious = nullptr;
   }
   string name;
   int pathDistance; // for path finding
   Vertex* pathPrevious; // for path finding
};

struct DirectedEdge {
   DirectedEdge(Vertex* sourceCtr, Vertex* targetCtr) : source(sourceCtr), target(targetCtr) {}
   Vertex* source;
   Vertex* target;
};

struct Graph {
   Graph(vector<Vertex*> verticesCtr, vector<DirectedEdge*> edgesCtr) {
      edges = edgesCtr;

      for (Vertex*& vertex : verticesCtr) {
         vertices[vertex->name] = vertex;
      }

      for (DirectedEdge*& edge : edgesCtr) {
         adjacencyList[edge->source->name].push_back(edge->target->name);
      }
   }
   void findUnweightedShortestPathFrom(Vertex* source) {
      queue<Vertex*> q;

      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         (*it).second->pathDistance = INFINITY_NUMBER;
      }

      source->pathDistance = 0;
      q.push(source);

      while (!q.empty()) {
         Vertex* v = q.front();
         q.pop();

         for (string& vertexName : adjacencyList[v->name]) {
            if (vertices[vertexName]->pathDistance == INFINITY_NUMBER) {
               vertices[vertexName]->pathDistance = v->pathDistance + 1;
               vertices[vertexName]->pathPrevious = v;
               q.push(vertices[vertexName]);
            }
         }
      }
   }
   string printShortestPathsFrom(Vertex* source) {
      stringstream ss;

      ss << "\n\n******************\nshortest paths to each vertex from: " << source->name << "\n******************" << endl;

      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         if ((*it).second->pathPrevious == nullptr) {
            if ((*it).second->pathDistance == INFINITY_NUMBER) {
               ss << (*it).second->name << " is unreachable from " << source->name << endl;
            }
            else if ((*it).second->pathDistance == 0) {
               ss << (*it).second->name << " is reachable within 0 from...itself " << endl;
            }
            else {
               ss << "Possibly bad data for " << (*it).first << " ..." << endl;
            }
         }
         else {
            vector<Vertex*> path;
            path.push_back((*it).second);
            Vertex* prev = (*it).second->pathPrevious;

            while (prev != nullptr) {
               path.push_back(prev);
               prev = prev->pathPrevious;
            }
            reverse(path.begin(), path.end());

            ss << "From " << source->name << " to " << (*it).second->name << "..." << endl;
            for (auto it = path.begin(); it != path.end(); it++) {
               ss << (*it)->name << " ";
            }
            ss << endl;
         }
         ss << endl;
      }

      return ss.str();
   }
   map<string, Vertex*> vertices;
   vector<DirectedEdge*> edges;
   map<string, vector<string> > adjacencyList;
};


int main() {

   Vertex v1 = Vertex("v1");
   Vertex v2 = Vertex("v2");
   Vertex v3 = Vertex("v3");
   Vertex v4 = Vertex("v4");
   Vertex v5 = Vertex("v5");
   Vertex v6 = Vertex("v6");
   Vertex v7 = Vertex("v7");

   DirectedEdge v12 = DirectedEdge(&v1, &v2);
   DirectedEdge v14 = DirectedEdge(&v1, &v4);

   DirectedEdge v24 = DirectedEdge(&v2, &v4);
   DirectedEdge v25 = DirectedEdge(&v2, &v5);

   DirectedEdge v31 = DirectedEdge(&v3, &v1);
   DirectedEdge v36 = DirectedEdge(&v3, &v6);

   DirectedEdge v43 = DirectedEdge(&v4, &v3);
   DirectedEdge v45 = DirectedEdge(&v4, &v5);
   DirectedEdge v46 = DirectedEdge(&v4, &v6);
   DirectedEdge v47 = DirectedEdge(&v4, &v7);

   DirectedEdge v57 = DirectedEdge(&v5, &v7);

   DirectedEdge v76 = DirectedEdge(&v7, &v6);

   vector<Vertex*> graphVertices = { &v1, &v2, &v3, &v4, &v5, &v6, &v7 };
   vector<DirectedEdge*> graphEdges = { &v12, &v14, &v24, &v25, &v31, &v36, &v43, &v45, &v46, &v47, &v57, &v76 };

   Graph graph = Graph(graphVertices, graphEdges);

   // TODO - v2 source has problems with cycle in graph

   /*for (Vertex*& v : graphVertices) {
      graph.findUnweightedShortestPathFrom(v);
      cout << graph.printShortestPathsFrom(v);
   }*/

   graph.findUnweightedShortestPathFrom(&v4);
   cout << graph.printShortestPathsFrom(&v4);

   return 0;
}