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

class stacklinkedlist:

    def __init__(self):
        self.firstNode = None
    
    def push(self, item):
        oldFirstNode = self.firstNode
        self.firstNode = node(item, oldFirstNode)

    def pop(self):
        item = self.firstNode.item
        self.firstNode = self.firstNode.nextNode
        return item
    
    def isEmpty(self):
        return self.firstNode is None
    
    def size(self):
        sizeTracker = 0
        nodeTracker = self.firstNode
        while nodeTracker is not None:
            sizeTracker = sizeTracker + 1
            nodeTracker = nodeTracker.nextNode
        return sizeTracker

    def stackValues(self):
        if self.isEmpty() or self.size() == 0:
            return []
        else:
            stackValues = []
            nodeTracker = self.firstNode
            while nodeTracker is not None:
                stackValues.append(nodeTracker.item)
                nodeTracker = nodeTracker.nextNode
            return stackValues

    def hasNext(self):
        currentNode = self.firstNode
        return currentNode is not None
    
    def next(self):
        currentNode = self.firstNode
        item = currentNode.item
        currentNode = currentNode.nextNode
        return item


class node:
    def __init__(self, item, nextNode):
        self.item = item
        self.nextNode = nextNode
    

def runClient(inputs):
    sll = stacklinkedlist()

    iterInputs = iter(inputs[0])
    for item in iterInputs:
        if item == 777:
            print("popped from stack: {}".format(sll.pop()))
            print("stack size: {}".format(sll.size()))
        else:
            sll.push(item)
            print("pushed on: {}".format(item))
            print("stack size: {}".format(sll.size()))

    finalSize = sll.size()
    if finalSize > 0:
        print("final stack:")
        print(sll.stackValues())
    elif sll.isEmpty():
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