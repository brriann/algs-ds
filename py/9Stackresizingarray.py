# CLI usage: 
# node js/9stacklinkedlist.js 1-2-3-777-4-5-6-777-777-777
#
# File usage:
# 1 2 3 777 4 5 6 777 777 777

#
# Stack of ints implemented by linked list
# ints in input stream will be pushed onto stack
# input of 777 will print popped int from stack
#

import sys, importlib.util

onUbuntu = True

baseDevFolder = '/home/ubuntu/Dev' if onUbuntu else '/Users/brianfoster/dev'

INPUT_FILE_PATH = baseDevFolder + '/algs-ds/input/9stack2.txt'

specFile = importlib.util.spec_from_file_location('file', baseDevFolder + '/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', baseDevFolder + '/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

class stackresizingarray:

    def __init__(self):
        self.stackArray = [None]
        self.N = 0
    
    def push(self, item):
        if self.N == len(self.stackArray):
            self.resize(2 * len(self.stackArray))
        self.stackArray[self.N] = item
        self.N = self.N + 1

    def pop(self):
        if self.N > 0 and self.N == (len(self.stackArray) / 4):
            self.resize(len(self.stackArray) / 2)
        self.N = self.N - 1
        return self.stackArray[self.N]
    
    def isEmpty(self):
        return self.N == 0
    
    def size(self):
        return self.N
    
    def resize(self, capacity):
        copyArray = [None] * capacity
        for i in range(self.N):
            copyArray[i] = self.stackArray[i]
        self.stackArray = copyArray

    def stackValues(self):
        if self.isEmpty() or self.size() == 0:
            return []
        else:
            stackValues = [None] * self.size()
            for i in range(self.N):
                stackValues[i] = self.stackArray[i]
            return stackValues


class node:
    def __init__(self, item, nextNode):
        self.item = item
        self.nextNode = nextNode
    

def runClient(inputs):
    sra = stackresizingarray()

    iterInputs = iter(inputs[0])
    for item in iterInputs:
        if item == 777:
            print("popped from stack: {}".format(sra.pop()))
            print("stack size: {}".format(sra.size()))
        else:
            sra.push(item)
            print("pushed on: {}".format(item))
            print("stack size: {}".format(sra.size()))

    finalSize = sra.size()
    if finalSize > 0:
        print("final stack:")
        print(sra.stackValues())
    elif sra.isEmpty():
        print("final stack is empty")
    else:
        print("error? final size and isEmpty don't agree")
##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))