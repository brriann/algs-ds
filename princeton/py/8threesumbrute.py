# CLI usage: 
# python 8threesumbrute.py 4 -4 2 6 0 -2 8 10 -6 ( WILL NOT USE CLI)
#
# File usage:
#4 -4 2 6 0 -2 8 10 -6

#
# Brute force implementation of Three-sum
# Read an array of ints
# Identify all triples that sum to zero
#

import sys, importlib.util

INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/8threesum1.txt'

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

class threesumbrute:
    
    def __init__(self):
        self.counter = 0

    def threesum(self, listA):
        for i in range(len(listA)):
            for j in range(i + 1, len(listA)):
                for k in range(j + 1, len(listA)):
                    if (listA[i] + listA[j] + listA[k] == 0):
                        print("3-SUM: {} {} {}".format(listA[i], listA[j], listA[k]))
                        self.counter += 1
        print('count: {}'.format(self.counter))


def runClient(inputs):
    listA = inputs[0]

    tsb = threesumbrute()
    tsb.threesum(listA)

##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))