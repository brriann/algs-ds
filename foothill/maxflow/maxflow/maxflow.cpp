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
   DirectedEdge(Vertex* sourceCtr, Vertex* targetCtr, int flowCapacityCtr) : source(sourceCtr), target(targetCtr), flowCapacity(flowCapacityCtr) {}
   Vertex* source;
   Vertex* target;
   int flowCapacity;
};

struct Graph {
   Graph(vector<Vertex*> verticesCtr, vector<DirectedEdge*> edgesCtr, bool isResidual = false) {
      edges = edgesCtr;

      for (Vertex*& vertex : verticesCtr) {
         vertices[vertex->name] = vertex;
      }

      for (DirectedEdge*& edge : edgesCtr) {
         adjacencyList[edge->source->name][edge->target->name] = edge->flowCapacity;
         // add residual backtracking / flow-undo edges
         if (isResidual) {
            adjacencyList[edge->target->name][edge->source->name] = 0;
         }
      }
   }
   bool findPath(Vertex* source, Vertex* sink, vector<Vertex*>& pathVertices) {
      queue<Vertex*> q;
 
      for (auto it = vertices.begin(); it != vertices.end(); it++) {
         (*it).second->pathDistance = INFINITY_NUMBER;
         (*it).second->pathPrevious = nullptr;
      }

      source->pathDistance = 0;
      q.push(source);

      while (!q.empty()) {
         Vertex* v = q.front();
         q.pop();

         for (auto it = adjacencyList[v->name].begin(); it != adjacencyList[v->name].end(); it++) {
            if (((*it).second > 0) && (vertices[(*it).first]->pathDistance == INFINITY_NUMBER)) {
               vertices[(*it).first]->pathDistance = v->pathDistance + 1;
               vertices[(*it).first]->pathPrevious = v;
               q.push(vertices[(*it).first]);
            }
         }
      }

      Vertex* current = sink;
      while (current != source) {
         if (current == nullptr) {
            return false;
         }
         pathVertices.push_back(current);
         current = current->pathPrevious;
      }
      pathVertices.push_back(current);
      reverse(pathVertices.begin(), pathVertices.end());

      return true;
   }
   int findMinFlowCapacityForPath(vector<Vertex*>& path) {
      int minFlowCapacity = INFINITY_NUMBER;

      for (auto it = path.begin(); it != path.end(); it++) {
         Vertex* v = *it;
         if (v == *(path.end() - 1)) {
            break;
         }

         if (adjacencyList[v->name][(*(it + 1))->name] < minFlowCapacity) {
            minFlowCapacity = adjacencyList[v->name][(*(it + 1))->name];
         }
      }
      return minFlowCapacity;
   }
   void addFlowToPath(vector<Vertex*>& path, int flowAdded, bool isResidual = false) {
      for (auto it = path.begin(); it != path.end(); it++) {
         Vertex* v = *it;
         if (v == *(path.end() - 1)) {
            break;
         }

         if (isResidual) {
            // subtract flow from forward edge
            adjacencyList[v->name][(*(it + 1))->name] -= flowAdded;

            // add flow to backward / undo edge
            adjacencyList[(*(it + 1))->name][v->name] += flowAdded;
         }
         else {
            // add flow to forward edge
            adjacencyList[v->name][(*(it + 1))->name] += flowAdded;
         }
      }
   }
   string print() {
      stringstream ss;

      for (auto it = adjacencyList.begin(); it != adjacencyList.end(); it++) {
         for (auto it2 = (*it).second.begin(); it2 != (*it).second.end(); it2++) {
            ss << "From " << (*it).first << " to " << (*it2).first << " : " << (*it2).second << endl;
         }
      }
      return ss.str();
   }
   map<string, Vertex*> vertices;
   vector<DirectedEdge*> edges;
   map<string, map<string, int> > adjacencyList;
};

int main() {

   // ORIGINAL GRAPH

   Vertex s = Vertex("s");
   Vertex a = Vertex("a");
   Vertex b = Vertex("b");
   Vertex c = Vertex("c");
   Vertex d = Vertex("d");
   Vertex t = Vertex("t");

   DirectedEdge sa = DirectedEdge(&s, &a, 4);
   DirectedEdge sb = DirectedEdge(&s, &b, 2);

   DirectedEdge ab = DirectedEdge(&a, &b, 1);
   DirectedEdge ac = DirectedEdge(&a, &c, 2);
   DirectedEdge ad = DirectedEdge(&a, &d, 4);

   DirectedEdge bd = DirectedEdge(&b, &d, 2);

   DirectedEdge ct = DirectedEdge(&c, &t, 3);

   DirectedEdge dt = DirectedEdge(&d, &t, 3);

   vector<Vertex*> graphVertices = { &s, &a, &b, &c, &d, &t };
   vector<DirectedEdge*> graphEdges = { &sa, &sb, &ab, &ac, &ad, &bd, &ct, &dt };

   Graph originalGraph = Graph(graphVertices, graphEdges);

   // FLOW GRAPH

   Vertex fs = Vertex("s");
   Vertex fa = Vertex("a");
   Vertex fb = Vertex("b");
   Vertex fc = Vertex("c");
   Vertex fd = Vertex("d");
   Vertex ft = Vertex("t");

   DirectedEdge fsa = DirectedEdge(&fs, &fa, 0);
   DirectedEdge fsb = DirectedEdge(&fs, &fb, 0);

   DirectedEdge fab = DirectedEdge(&fa, &fb, 0);
   DirectedEdge fac = DirectedEdge(&fa, &fc, 0);
   DirectedEdge fad = DirectedEdge(&fa, &fd, 0);

   DirectedEdge fbd = DirectedEdge(&fb, &fd, 0);

   DirectedEdge fct = DirectedEdge(&fc, &ft, 0);

   DirectedEdge fdt = DirectedEdge(&fd, &ft, 0);

   vector<Vertex*> flowGraphVertices = { &fs, &fa, &fb, &fc, &fd, &ft };
   vector<DirectedEdge*> flowGraphEdges = { &fsa, &fsb, &fab, &fac, &fad, &fbd, &fct, &fdt };

   Graph flowGraph = Graph(flowGraphVertices, flowGraphEdges);

   // RESIDUAL GRAPH

   Vertex rs = Vertex("s");
   Vertex ra = Vertex("a");
   Vertex rb = Vertex("b");
   Vertex rc = Vertex("c");
   Vertex rd = Vertex("d");
   Vertex rt = Vertex("t");

   DirectedEdge rsa = DirectedEdge(&rs, &ra, 4);
   DirectedEdge rsb = DirectedEdge(&rs, &rb, 2);

   DirectedEdge rab = DirectedEdge(&ra, &rb, 1);
   DirectedEdge rac = DirectedEdge(&ra, &rc, 2);
   DirectedEdge rad = DirectedEdge(&ra, &rd, 4);

   DirectedEdge rbd = DirectedEdge(&rb, &rd, 2);

   DirectedEdge rct = DirectedEdge(&rc, &rt, 3);

   DirectedEdge rdt = DirectedEdge(&rd, &rt, 3);

   vector<Vertex*> residualVertices = { &rs, &ra, &rb, &rc, &rd, &rt };
   vector<DirectedEdge*> residualEdges = { &rsa, &rsb, &rab, &rac, &rad, &rbd, &rct, &rdt };

   Graph residualGraph = Graph(residualVertices, residualEdges, true);

   // find a path in residualGraph from s to t
   vector<Vertex*> residualPath;
   while (residualGraph.findPath(&rs, &rt, residualPath)) {
      // find amount of flow that can be added: min edge on this path
      int minFlow = residualGraph.findMinFlowCapacityForPath(residualPath);

      // adjust flowGraph and residualGraph
      flowGraph.addFlowToPath(residualPath, minFlow);
      residualGraph.addFlowToPath(residualPath, minFlow, true);

      // clear out reference collection and min flow value for path found
      residualPath.clear();
   }

   cout << "Max Flow path is ..." << endl;
   cout << flowGraph.print();

   return 0;
}