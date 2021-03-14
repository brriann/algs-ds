# CLI usage: 
# node 0Intro.js x-y-z/a-b-c
#
# File usage:
# x y z 
# a b c

import sys, importlib.util

INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/0intro3.txt'

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

def intro(inputs):
    print('A.) Full 2D Array')
    print(inputs)
    print('B.) Each Row')
    for row in inputs:
        print(row)
    print('C.) Each Cell')
    for row in inputs:
        for cell in row:
            print(cell)

if len(sys.argv) > 1:
    intro(cli.readArgTo2DArray(sys.argv[1]))
else:
    intro(file.readLinesTo2DArray(INPUT_FILE_PATH))