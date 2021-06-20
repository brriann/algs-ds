# High Level Data Structures and Algorithm Notes

## Data Structures

### Iterator

Iterator can be implemented over any collection.

Begin and End locations, increment operator, dereference operation enable forEach loops in C++.

### Array/Vector

Indexing operations are O(1).

Inserts/deletes at the end of the array are inexpensive.

Inserts/deletes at the start or middle of the array are expensive.  O(n) copies happen.

Search operations are O(n)

### Linked List

Linked list operations require an iterator pointing at the position under operation.

Inserts/deletes at the start or middle of the list are inexpensive.

Search operations are O(n)

### Stack

LIFO, last-in-first-out, push onto and pop off of the "top"

Array vs Linked-List implementations

### Queue

FIFO, first-in-first-out, enqueue onto the "back" and dequeue off of the "front"

Array vs Linked-List implementations

### Binary Search Tree

Insert, Delete, and Search operations are generally O(log(n)).

A sorted order is maintained.

Search complexity is improved over array/list.

Insert/Delete complexity is slower than array/list.

Balanced vs Unbalanced

### AVL Tree

Balance condition maintained - Insert and Delete operations are still O(log(n)), but with a higher constant.

Balance condition guarantees O(log(n)) tree height, and therefore O(log(n)) search/insert/delete complexity.

Rotations between nodes in a subtree as the subtree's root node becomes imbalanced from insert/delete operations

### Splay Tree

### Hash Table

Insert, Delete, and Search operations in average O(1) time.

Only a subset of BST / ordered set operations are available - no findMin, findMax, outputInSortedOrder

Sacrifice sorted order for increased speed on the core set, of set operations

### Perfect Hashing

### Cuckoo Hashing

### Hopscotch Hashing

### Binary Heap

Binary tree that is completely filled, with possible exception of bottom level (bottom level is filled left to right)

Since a complete binary tree is regular, can be represented in an array (with array index helpers findParent = i/2, findLeftChild = 2i, findRightChild = 2i + 1)

Heap Order Property: (Min Heap), for every node X, the parent node key is less than or equal to the key in X.

Heap Operations: insert (insert at bottom, percolate up), deleteMin (create hole at top, percolate down)

### Priority Queue

Generally built on a min/max heap, PQ is a type of queue that supports Enqueue, and DequeueHighestPriority (ie, insert and deleteMin)

### d-Heap

### Leftist Heap

### Skew Heap

### Binomial Queue

### Union-Find / Disjoint Sets

Data structure to support equivalence relations

Array representation of a forest of trees. Union connected / joined trees share the same root or parent element.

Operations: find (return root/parent) and union (join two disjoint sets - set root A = root B or vice versa)

## Search / Sort / Select Algorithms

### Binary Search

### Insertion Sort

O(n^2) in-place stable sort.  Elements from start of the array to main iterator are sorted.  However, it is not a partition, since elements can be inserted into that sorted section.  (Primary iterator covers collection 1x.  Secondary iterator covers sorted elements, finding spot to insert next element.)

### Selection Sort

O(n^2) in-place unstable sort.  Sorted partition forms at start of array and grows.  (Primary iterator covers collection 1x.  Secondary iterator covers unsorted elements, finding next minimum element, to be placed at the end of the sorted parition.)

### Bubble Sort

O(n^2) in-place, stable sort. Sorted partition forms at the end of collection.

### Merge, Merge Sort

O(Nlog(N)) divide and conquer, out-of-pace, stable sort.  O(N) space complexity due to copy of merge arrays.

Recursively divide and merge smaller sub lists.

### Heap Sort

O(Nlog(N)) in-place, unstable sort using a Max Heap array representation

Step 1: Build a Max Heap (O(N))

Step 2: Perform N-1 deleteMax operations, swapping the first (max) element in the Heap/array with the last, and decrementing Heap size by 1

### Shell Sort

O(N^3/2) in-place, unstable sort when using Hibbard increment sequence

Insertion sort using a decremented offset to sort elements at an interval (skipping adjacent swaps)

### Quick Sort

O(Nlog(N)) average, O(N^2) worst case, divide and conquer, in-place, unstable sort

Pivot selected, elements less than / greater than pivot partioned on either side of pivot

Implement with left and right iterators, (inc|dec)rementing while values are properly left/right of pivot.  Swapping right and left elements when needed.

### Quick Sort and Heap Sort combo

Best of both worlds - can achieve Quick Sort's fast running time, with guarantee of Heap Sort's O(Nlog(N)) worst case running

### Quick Select

### Bucket Sort

### Radix Sort

## DS + Algs using Disk

### B Tree

### Extendible Hashing

### External Sorting

## Graph Algorithms

### Topological Sort

### Breadth First Search

### Depth First Search

### Unweighted Shortest Paths

### Dijkstra's Algorithm for Weighted Shortest Paths

### Shortest Paths with Negative Edge Costs

### Acyclic Graph Shortest Paths, Critical Path Analysis

### Network Flow, Min-Cut / Max-Flow

### Minimum Spanning Tree

#### Prim's Algorithm

#### Kruskal's Algorithm

### Depth First Search Applications

#### Biconnectivity, Articulation Points

#### Undirected Graph Traversal: Euler Circuit, Euler Tour, Hamiltonian Cycle

#### Directed Graph Traversal: Test if a Directed Graph is Acyclic

#### Test if a Directed Graph is Strongly Connected, Find Strongly Connected Components

## Greedy Algorithms

### Scheduling (Average, Final Completion Time)

### File Compression (Huffman Codes, Optimal Prefix Code)

### Bin-Packing (online, offline, next/first/best fit)

## Divide and Conquer Algorithms

### Closest Points problem

### Selection problem

### Integer Multiplication

### Matrix Multiplication

## Dynamic Programming

### Ordering Matrix Multiplications

### Optimal Binary Search Tree

### All-Pairs Shortest Path

## Randomized Algorithms

### Skip Lists

### Primality Testing

## Backtracking Algorithms

### Turnpike Reconstruction Problem

### Turn-based Game AI (Minimax, Negamax, Alpha Beta pruning, Transposition Table)






