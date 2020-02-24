# CLI expected format "node myprog.js 1-2-3/4-5-6/7-8-9"
# to represent the file format:
# 1 2 3
# 4 5 6
# 7 8 9

rowDelimiter = '/'
cellDelimiter = '-'

def lineHelper(row):
    return row.split(cellDelimiter)

def readArgTo2DArray(cliInput):
    array2D = []
    lines = cliInput.split(rowDelimiter)
    i = 0
    for line in lines:
        array2D.append([])
        array2D[i] = [int(n) for n in line.split('-')]
    


