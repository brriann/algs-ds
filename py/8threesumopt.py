# CLI usage: 
# node 8threesumopt.js 4 -4 2 6 0 -2 8 10 -6 ( WILL NOT USE CLI)
#
# File usage:
#4 -4 2 6 0 -2 8 10 -6

#
# Optimized implementation of three-sum
# Read an array of ints - Identify all triples that sum to zero
# Sort the list
# for each pair of numbers a[i] and a[j], binary search for -(a[i] + a[j])
#

import sys, importlib.util

INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/8threesum1.txt'

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

file = module_from_file('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
cli = module_from_file('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
binarySearch = module_from_file('binarySearch', '/home/ubuntu/Dev/algs-ds/py/6binarysearch.py')
insertionSort = module_from_file('insertionSort', '/home/ubuntu/Dev/algs-ds/py/7insertionsort.py')

class threesumopt:

    def __init__(self):
        self.iSort = insertionSort.insertionsort()
        self.bSearch = binarySearch.binarysearch()
        self.foundTriples = []

    def threesum(self, listA):
        print('input list:')
        print(listA)
        
        self.iSort.sort(listA)

        print('sorted list:')
        print(listA)

        self.n = len(listA)
        self.count = 0

        for i in range(len(listA)):
            for j in range(i + 1, len(listA)):
                ij = -(listA[i] + listA[j])
                indexIj = self.bSearch.search(0, self.n - 1, ij, listA)
                if indexIj >= 0 and listA[i] < listA[j] < ij:
                    self.count += 1
                    self.foundTriples.append([listA[i], listA[j], ij])

        print('*** 3- SUM RESULTS ***')
        print('count: {}'.format(self.count))
        print('Found Triples:')
        print(self.foundTriples)
                

def runClient(inputs):
    listA = inputs[0]

    tso = threesumopt()
    tso.threesum(listA)

##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))