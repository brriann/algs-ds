# File format expected:
# 1 2 3
# 4 5 6
# 7 8 9

cellDelimiter = ' '

def readLinesTo2DArray(filePath):
    array2D = []
    with open(filePath, 'r') as openfile:
        i = 0
        for line in openfile:
            array2D.append([])
            array2D[i] = [int(n) for n in line.split(cellDelimiter)]
            i += 1
    return array2D


