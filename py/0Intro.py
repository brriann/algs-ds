
# invoke this script with an int array from CLI as "python 0Intro.py 0,1,2,3,4"

import sys, numpy

if len(sys.argv) < 2:
    print('usage: python 0Intro.py x,y,z,a,b,c')
else:
    arrayArgument = sys.argv[1].split(',')

    floatArray = numpy.array(arrayArgument).astype(numpy.int)
    arraySum = numpy.sum(floatArray)

    print(arrayArgument)
    print('your array sum is:')
    print(arraySum)