# CLI usage: 
# java Insertionsort 1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
#
# File usage:
# 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

#
# Simple client for Insertion Sort to be used in Threesum
# Read an array of ints
# Sort using Insertion Sort
# Return sorted list
#

import sys, importlib.util

onUbuntu = False

baseDevFolder = '/home/ubuntu/Dev' if onUbuntu else '/Users/brianfoster/dev'

INPUT_FILE_PATH = baseDevFolder + '/algs-ds/input/7insertionsort1.txt'

specFile = importlib.util.spec_from_file_location('file', baseDevFolder + '/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', baseDevFolder + '/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

class shellsort:
    
    def __init__(self):
        self.counter = 0

    def less(self, v, w):
        # only ints for now. comparator function to come maybe.
        return v < w
    
    def exchange(self, listB, i, j):
        swap = listB[i]
        listB[i] = listB[j]
        listB[j] = swap

    def sort(self, listA):
        N = len(listA)

        h = 1
        while h < N // 3:
            h = 3 * h + 1
        while h >= 1:
            for i in range(h, N):
                temp = listA[i]

                j = i
                while j >= h and listA[j - h] > temp:
                    listA[j] = listA[j - h]
                    j -= h
                
                listA[j] = temp
            h = h // 3

##
## CLIENT
##

def runClient(inputs):
    listA = inputs[0]

    print('Unsorted list: ')
    print(listA)

    ss = shellsort()
    ss.sort(listA)
    
    print('Sorted list: ')
    print(listA)


if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))