 # CLI usage: 
 # java Binarysearch 29/1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
 #
 # File usage:
 # 29
 # 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

 #
 # Simple client for Binarysearch to be used in Threesum
 # Read a target, and an array of sorted ints
 # Binary Search for the target
 # Return the target's index in array if present
 # Return -1 if not present
 #

# import sys, importlib.util

# INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/6binarysearch1.txt'

# specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
# file = importlib.util.module_from_spec(specFile)
# specFile.loader.exec_module(file)

# specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
# cli = importlib.util.module_from_spec(specCli)
# specCli.loader.exec_module(cli)

class binarysearch:
    
    # def __init__(self, target, listToSearch):
    #     self.target = target
    #     self.listToSearch = listToSearch
    #     self.length = len(listToSearch)
        # print('target')
        # print(self.target)
        # print('listToSearch')
        # print(self.listToSearch)
        # print('length')
        # print(self.length)

    def search(self, low, high, target, listToSearch):
        foundIndex = -1
        found = False
        
        while (low <= high and not found):
            middle = low + ((high - low) // 2)
            #print('SEARCH lo/hi: {}/{}'.format(low, high))
            #print('calc\'d mid: {}'.format(middle))
            if (listToSearch[middle] > target):
                #print('Go lower')
                high = middle - 1
            elif (listToSearch[middle] < target):
                #print('Go higher')
                low = middle + 1
            else:
                foundIndex = middle
                found = True
        return foundIndex

##
## CLIENT
##

# def runClient(inputs):
#     targetin = inputs[0][0]
#     listin = inputs[1]

#     bs = binarysearch(targetin, listin)

#     initialLow = 0
#     initialHigh = len(listin) - 1

#     print('initial lo/hi: {}/{}'.format(initialLow, initialHigh))
#     targetIndex = bs.search(initialLow, initialHigh)

#     # targetIndex = -1 for Not Found
#     if (targetIndex < 0):
#         print('*** TARGET NOT IN LIST ***')
#     else:
#         print("*** TARGET {} FOUND AT INDEX {} IN LIST:".format(targetin, targetIndex))
#         print(listin)

# if len(sys.argv) > 1:
#     runClient(cli.readArgTo2DArray(sys.argv[1]))
# else:
#     runClient(file.readLinesTo2DArray(INPUT_FILE_PATH))