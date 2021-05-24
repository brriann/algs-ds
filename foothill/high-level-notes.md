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

### B Tree

### Hash Table

Insert, Delete, and Search operations in average O(1) time.

Only a subset of BST / ordered set operations are available - no findMin, findMax, outputInSortedOrder

Sacrifice sorted order for increased speed on the core set, of set operations

### Perfect Hashing

### Cuckoo Hashing

### Hopscotch Hashing

### Extendible Hashing

### Priority Queue

### Binary Heap

### d-Heap

### Leftist Heap

### Skew Heap

### Binomial Queue

## Algorithms

### Binary Search

### Insertion Sort

O(n^2) in-place sort.  Elements from start of the array to main iterator are sorted.  However, it is not a partition, since elements can be inserted into that sorted section.  (Primary iterator covers collection 1x.  Secondary iterator covers sorted elements, finding spot to insert next element.)

### Selection Sort

O(n^2) in-place sort.  Sorted partition forms at start of array and grows.  (Primary iterator covers collection 1x.  Secondary iterator covers unsorted elements, finding next minimum element, to be placed at the end of the sorted parition.)

### Bubble Sort

O(n^2) in-place sort. Sorted partition forms at the end of collection.

### Merge, Merge Sort

### Heap Sort

### Shell Sort

### Quick Sort

### Quick Select

### Bucket Sort

### Radix Sort

### External Sorting

