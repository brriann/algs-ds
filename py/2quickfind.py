# CLI usage: 
# python 2quickfind.py n/p-q/p-q/p-q/p-q
#
# File usage:
# n
# p q
# p q
# p q

#
# Eager approach of Union-Find
# Read an array size "n"
# Read rows of elt's "p" and "q"
#
# integer array id[] of size n.
# p and q are connected iff they have the same id
#
# Find: check if p and q have the same id
# Union: to merge components containing p and q,
#     change all entries whose id equals id[p] to id[q]
#
# Trees are flat, but too expensive to keep them flat.
# Union too expensive (N array accesses)

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
        for x in range(self.n):
            self.ids.append(x)

    def union(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]
        for x in range(self.n):
            if self.ids[x] == pid:
                self.ids[x] = qid
        print("{} <---> {}".format(p, q))
        print(self.ids)

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]


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