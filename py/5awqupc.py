# CLI usage: 
# python 4wqu.py n/p-q/p-q/p-q/p-q
#
# File usage:
# n
# p q
# p q
# p q

#
# Weighted Quick Union
# Read an array size "n"
# Read rows of elt's "p" and "q"
#
# integer array id[] of size n.
# integer array size[] of size n
# size[i] tracks the size of object whose root is id[i]
# id[i] is parent of i
# root of i is id[id[id[...id[i]...]]]
# p and q are connected iff they have the same root
#
# Find: check if p and q have the same root
# Union: to merge components containing p and q,
#     set the id of smaller tree's root to the id of larger tree's root
#     and update the size[] array
#
# By adding smaller trees to larger trees, Tree height grows slower (and is limited to at most lgN)

import sys, importlib.util

INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt'

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

class unionfind:
    
    def __init__(self, n):
        self.n = n
        self.ids = []
        self.size = []
        for x in range(self.n):
            self.ids.append(x)
            self.size.append(1)

    def union(self, p, q):
        print("UNION {} and {}".format(p, q))
        i = self.root(p)
        j = self.root(q)

        if (i == j):
            print("({} connects to {})".format(p, q))
            return

        if (self.size[i] < self.size[j]):
            self.ids[i] = j
            self.size[j] += self.size[i]
        else:
            self.ids[j] = i
            self.size[i] += self.size[j]

        print("{} <---> {}".format(p, q))
        print(self.ids)
        print(self.size)

    def connected(self, p, q):
        print("CONNECTED {} and {}".format(p, q))
        return self.root(p) == self.root(q)

    def root(self, i):
        print("ROOT {}".format(i))
        nodesToSet = []
        nodesThatWereSet = 0
        originalChild = i

        while i != self.ids[i]:
            nodesToSet.append(i)
            i = self.ids[i]

        if (len(nodesToSet) > 0):
            print("examining {}, set nodes to root {}:".format(originalChild, i))
            print(nodesToSet)

        # 2nd pass to set examined nodes to root
        for j in nodesToSet:
            if (self.ids[j] != i):
                self.ids[j] = i
                self.size[i] += self.size[j]
                nodesThatWereSet += 1
        
        if (len(nodesToSet) > 0 and nodesThatWereSet > 0):
            print("([] examined nodes set.)".format(nodesThatWereSet))
            print(self.ids)
            print(self.size)

        return i


def runClient(inputs):
    n = inputs[0][0]
    uf = unionfind(n)

    iterInputs = iter(inputs)
    next(iterInputs)
    for pair in iterInputs:
        p = pair[0]
        q = pair[1]
        
        if not uf.connected(p, q):
            uf.union(p, q)
        else:
            print("({} and {} are connected.)".format(p, q))


##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))