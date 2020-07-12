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

class queueresizingarray:

    def __init__(self):
        self.firstNode = None
        self.lastNode = None
    
    def enQueue(self, item):
        oldLastNode = self.lastNode
        self.lastNode = node(item, None)
        if self.isEmpty():
            self.firstNode = self.lastNode
        else:
            oldLastNode.nextNode = self.lastNode

    def deQueue(self):
        item = self.firstNode.item
        self.firstNode = self.firstNode.nextNode
        if self.isEmpty():
            self.lastNode = None
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

    def queueValues(self):
        if self.isEmpty() or self.size() == 0:
            return []
        else:
            queueValues = []
            nodeTracker = self.firstNode
            while nodeTracker is not None:
                queueValues.append(nodeTracker.item)
                nodeTracker = nodeTracker.nextNode
            return queueValues


class node:
    def __init__(self, item, nextNode):
        self.item = item
        self.nextNode = nextNode
    

def runClient(inputs):
    qra = queueresizingarray()

    iterInputs = iter(inputs[0])
    for item in iterInputs:
        if item == 777:
            print("dequeued from queue: {}".format(qra.deQueue()))
            print("queue size: {}".format(qra.size()))
        else:
            qra.enQueue(item)
            print("enqueued: {}".format(item))
            print("queue size: {}".format(qra.size()))

    finalSize = qra.size()
    if finalSize > 0:
        print("final queue:")
        print(qra.queueValues())
    elif qra.isEmpty():
        print("final queue is empty")
    else:
        print("error? final size and isEmpty don't agree")
##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))