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