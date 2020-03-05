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

INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/7insertionsort1.txt'

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

class insertionsort:
    
    def __init__(self):
        self.counter = 0

    def search(self, unsortedList):
        return unsortedList


def runClient(inputs):
    unsortedList = inputs[0]

    is = insertionsort(unsortedList)
    sortedList = is.sort

    print('Unsorted list: ')
    print(unsortedList)
    print('Sorted list: ')
    print(sortedList)

##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))