# invoke this script from CLI as "python 1unionfind.py"


class unionfind:
    
    def __init__(self, n):
        self.n = n

    

    def union(self, p, q):
        asdf = 1 + 1

    def connected(self, p, q):
        return p == q

    def find(p):
        asdf = 1 + 1

    def count():
        asdf = 1 + 1

def takeFileInput():
    asdf = 1 + 2

def takeCommandLineInput():
    n = int(input("Enter n: "))
    p = int(input("Enter p: "))
    q = int (input("Enter q: "))
    return [n. p. q]

##
## Program starts here.
##

npq = takeCommandLineInput()

n = npq[0]
p = npq[1]
q = npq[2]

uf = unionfind(n)


if not uf.connected(p, q):
    uf.union(p, q)
    print(p, q)

