# CLI usage: 
# python 3quickunion.py n/p-q/p-q/p-q/p-q
#
# File usage:
# n
# p q
# p q
# p q

#
# Lazy approach of Union-Find
# Read an array size "n"
# Read rows of elt's "p" and "q"
#
# integer array id[] of size n.
# id[i] is parent of i
# root of i is id[id[id[...id[i]...]]]
# p and q are connected iff they have the same root
#
# Find: check if p and q have the same root
# Union: to merge components containing p and q,
#     set the id of p's root to the id of q's root
#
# Trees get too tall
# Find too expensive (could be N array accesses)

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

    def union(self, p, q):
        # This file only implements the UF client.
        asdf = 1

    def connected(self, p, q):
        return False

    def find(p):
        # This file only implements the UF client.
        asdf = 2

    def count():
        # This file only implements the UF client.
        asdf = 3


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
            print("{} <---> {}".format(p, q))
        else:
            print("({} and {} are connected.)".format(p, q))


##
## CLIENT
##

if len(sys.argv) > 1:
    runClient(cli.readArgTo2DArray(sys.argv[1]))
else:
    runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))