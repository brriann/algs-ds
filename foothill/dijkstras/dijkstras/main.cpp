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
using std::priority_queue;
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
      known = false;
   }
   string name;
   int pathDistance; // for path finding
   Vertex* pathPrevious; // for path finding
   bool known;
};

struct DirectedEdge {
   DirectedEdge(Vertex* sourceCtr, Vertex* targetCtr, int weightCtr) : source(sourceCtr), target(targetCtr), weight(weightCtr) {}
   Vertex* source;
   Vertex* target;
   int weight;
};

struct PriorityQueueEntry {
   Vertex* vertex;
   Vertex* prevVertex;
   int pathWeight;

   PriorityQueueEntry(Vertex* vertexCtr, Vertex* prevVertexCtr, int pathWeightCtr) : vertex(vertexCtr), prevVertex(prevVertexCtr), pathWeight(pathWeightCtr) {}

   // for min heap PQ behavior
   bool operator<(const PriorityQueueEntry& rhs) const {
      return pathWeight > rhs.pathWeight;
   }
};


struct Graph {
   Graph(vector<Vertex*> verticesCtr, vector<DirectedEdge*> edgesCtr) {
      edges = edgesCtr;

      for (Vertex*& vertex : verticesCtr) {
         vertices[vertex->name] = vertex;
      }

      for (DirectedEdge*& edge : edgesCtr) {
         adjacencyList[edge->source->name].push_back(make_pair(edge->target->name, edge->weight));
      }
   }
   void sparseDijkstras(Vertex* source) {
      priority_queue<PriorityQueueEntry> q;
      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         (*it).second->pathDistance = INFINITY_NUMBER;
         (*it).second->known = false;
      }

      q.emplace(source, nullptr, 0);

      while (!q.empty()) {
         const PriorityQueueEntry entry = q.top();
         q.pop();

         if (vertices[entry.vertex->name]->known) {
            continue;
         }
         else {
            if (entry.pathWeight < vertices[entry.vertex->name]->pathDistance) {
               vertices[entry.vertex->name]->known = true;
               vertices[entry.vertex->name]->pathDistance = entry.pathWeight;
               vertices[entry.vertex->name]->pathPrevious = entry.prevVertex;

               for (pair<string, int>& vertexNameWeightPair : adjacencyList[entry.vertex->name]) {
                  if (!vertices[vertexNameWeightPair.first]->known &&
                     (entry.pathWeight + vertexNameWeightPair.second) < vertices[vertexNameWeightPair.first]->pathDistance) {
                     q.emplace(vertices[vertexNameWeightPair.first], entry.vertex, entry.pathWeight + vertexNameWeightPair.second);
                  }
               }
            }
         }
      }

   }
   // this is not optimized for sparse graphs.
   void dijkstras(Vertex* source) {

      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         (*it).second->pathDistance = INFINITY_NUMBER;
         (*it).second->known = false;
      }

      source->pathDistance = 0;

      while (unknownDistanceVertexExists()) {
         Vertex* v = smallestUnknownDistanceVertex();
         v->known = true;

         for (pair<string, int>& vertexNameWeightPair : adjacencyList[v->name]) {
            if (!vertices[vertexNameWeightPair.first]->known) {
               int cvw = vertexNameWeightPair.second;

               if ((v->pathDistance + cvw) < vertices[vertexNameWeightPair.first]->pathDistance) {
                  vertices[vertexNameWeightPair.first]->pathDistance = v->pathDistance + cvw;
                  vertices[vertexNameWeightPair.first]->pathPrevious = v;
               }
            }
         }
      }
   }
   bool unknownDistanceVertexExists() {
      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         if (!(*it).second->known) {
            return true;
         }
      }
      return false;
   }
   Vertex* smallestUnknownDistanceVertex() {
      string smallestVertexName;
      int smallestDistance = INFINITY_NUMBER;

      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         if ((!(*it).second->known) && (*it).second->pathDistance < smallestDistance) {
            smallestVertexName = (*it).first;
            smallestDistance = (*it).second->pathDistance;
         }
      }
      return vertices[smallestVertexName];
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
            int pathWeightTotal = 0;
            vector<Vertex*> path;
            path.push_back((*it).second);
            Vertex* prev = (*it).second->pathPrevious;
            pathWeightTotal = (*it).second->pathDistance;

            while (prev != nullptr) {
               path.push_back(prev);
               prev = prev->pathPrevious;
            }
            reverse(path.begin(), path.end());

            ss << "From " << source->name << " to " << (*it).second->name << "... (cost: " << pathWeightTotal << ")" << endl;
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
   map<string, vector<pair<string, int> > > adjacencyList;
};

int main()
{
   Vertex v1 = Vertex("v1");
   Vertex v2 = Vertex("v2");
   Vertex v3 = Vertex("v3");
   Vertex v4 = Vertex("v4");
   Vertex v5 = Vertex("v5");
   Vertex v6 = Vertex("v6");
   Vertex v7 = Vertex("v7");

   DirectedEdge v12 = DirectedEdge(&v1, &v2, 2);
   DirectedEdge v14 = DirectedEdge(&v1, &v4, 1);

   DirectedEdge v24 = DirectedEdge(&v2, &v4, 3);
   DirectedEdge v25 = DirectedEdge(&v2, &v5, 10);

   DirectedEdge v31 = DirectedEdge(&v3, &v1, 4);
   DirectedEdge v36 = DirectedEdge(&v3, &v6, 5);

   DirectedEdge v43 = DirectedEdge(&v4, &v3, 2);
   DirectedEdge v45 = DirectedEdge(&v4, &v5, 2);
   DirectedEdge v46 = DirectedEdge(&v4, &v6, 8);
   DirectedEdge v47 = DirectedEdge(&v4, &v7, 4);

   DirectedEdge v57 = DirectedEdge(&v5, &v7, 6);

   DirectedEdge v76 = DirectedEdge(&v7, &v6, 1);

   vector<Vertex*> graphVertices = { &v1, &v2, &v3, &v4, &v5, &v6, &v7 };
   vector<DirectedEdge*> graphEdges = { &v12, &v14, &v24, &v25, &v31, &v36, &v43, &v45, &v46, &v47, &v57, &v76 };

   Graph graph = Graph(graphVertices, graphEdges);

   graph.dijkstras(&v1);
   cout << graph.printShortestPathsFrom(&v1);
   //graph.sparseDijkstras(&v1);
   //cout << graph.printShortestPathsFrom(&v1);
   return 0;
}
