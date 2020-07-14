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

onUbuntu = False

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
        self.queueArray = [None]
        self.N = 0
        self.first = 0
        self.last = 0
    
    def enQueue(self, item):
        if self.N == len(self.queueArray):
            self.resize(2 * len(self.queueArray))
        self.queueArray[self.last] = item
        self.last = self.last + 1
        if self.last == len(self.queueArray):
            self.last = 0
        self.N = self.N + 1

    def deQueue(self):
        item = self.queueArray[self.first]
        self.queueArray[self.first] = None
        self.N = self.N - 1
        self.first = self.first + 1
        if self.first == len(self.queueArray):
            self.first = 0
        if self.N > 0 and self.N == len(self.queueArray) / 4:
            self.resize(len(self.queueArray) / 2)
        return item
    
    def isEmpty(self):
        return self.N == 0

    def resize(self, capacity):
        if capacity >= self.N:
            copyArray = [None] * capacity
            for i in range(self.N):
                copyArray[i] = self.queueArray[(self.first + i) % len(self.queueArray)]
            self.queueArray = copyArray
            self.first = 0
            self.last = self.N

    def size(self):
        return self.N

    def queueValues(self):
        if self.isEmpty() or self.size() == 0:
            return []
        else:
            queueValues = [None] * self.size()
            for i in range(self.N):
                queueValues[i] = self.queueArray[(self.first + i) % len(self.queueArray)]
            return queueValues

    

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