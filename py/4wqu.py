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
        i = self.root(p)
        j = self.root(q)

        if (i == j):
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
        return self.root(p) == self.root(q)

    def root(self, i):
        while i != self.ids[i]:
            i = self.ids[i]
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