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

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

specBinarySearch = importlib.util.spec_from_file_location('binarySearch', '/home/ubuntu/Dev/algs-ds/py/6binarysearch.py')
binarySearch = importlib.util.module_from_spec(specBinarySearch)
specBinarySearch.loader.exec_module(binarySearch)

specInsertionSort = importlib.util.spec_from_file_location('insertionSort', '/home/ubuntu/Dev/algs-ds/py/7insertionsort.py')
insertionSort = importlib.util.module_from_spec(specInsertionSort)
specInsertionSort.loader.exec_module(insertionSort)

class threesumopt:
    
    def __init__(self):
        self.counter = 0

    def threesum(self, listA):
        for i in range(len(listA)):
            for j in range(i + 1, len(listA)):
                ij = listA[i] + listA[j]
                print(ij)

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