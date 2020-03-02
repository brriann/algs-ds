 # CLI usage: 
 # java Binarysearch 29/1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
 #
 # File usage:
 # 29
 # 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

 #
 # Simple client for Binarysearch to be used in Threesum
 # Read a target, and an array of sorted ints
 # Binary Search for the target
 # Return the target's index in array if present
 # Return -1 if not present
 #

import sys, importlib.util

INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/6binarysearch1.txt'

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

class binarysearch:
    
    def __init__(self, target, listToSearch):
        self.target = target
        self.listToSearch = listToSearch
        self.length = len(listToSearch)
        print('target')
        print(self.target)
        print('listToSearch')
        print(self.listToSearch)
        print('length')
        print(self.length)

    def search(self, low, middle, high):
        lo = low
        mid = middle
        hi = high
        nextlo = lo
        nextmid = mid
        nexthi = hi
        foundIndex = -1
        print('SEARCHtop lo/mid/hi: {}/{}/{}'.format(low, middle, high))
        
        while (self.listToSearch[mid] != self.target):
            if (lo >= mid or hi <= mid):
                print('A')
                return foundIndex    
            elif (self.listToSearch[mid] > self.target):
                print('B')
                nexthi = mid
                nextmid = ((hi - lo) // 2) + 1
            elif (self.listToSearch[mid] < self.target):
                print('C')
                nextlo = mid
                nextmid = ((hi - lo) // 2) + 1
            print('SEARCHbottom lo/mid/hi: {}/{}/{}'.format(low, middle, high))
            self.search(nextlo, nextmid, nexthi)

        foundIndex = self.listToSearch.index(mid)
        return foundIndex


def runClient(inputs):
    targetin = inputs[0][0]
    listin = inputs[1]

    bs = binarysearch(targetin, listin)

    initialLow = 0
    initialMiddle = len(listin) // 2
    initialHigh = len(listin) - 1

    print('initial lo/mid/hi: {}/{}/{}'.format(initialLow, initialMiddle, initialHigh))
    targetIndex = bs.search(initialLow, initialMiddle, initialHigh)

    # targetIndex = -1 for Not Found
    if (targetIndex < 0):
        print('*** TARGET NOT IN LIST ***')
    else:
        print("*** TARGET {} FOUND AT INDEX {} IN LIST  {}".format(targetin, targetIndex, listin))

##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))