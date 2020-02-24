# CLI usage: 
# node 0Intro.js x-y-z/a-b-c
#
# File usage:
# x y z 
# a b c

import sys, importlib.util

specFile = importlib.util.spec_from_file_location('file', '/home/ubuntu/Dev/algs-ds/tools/file.py')
file = importlib.util.module_from_spec(specFile)
specFile.loader.exec_module(file)

specCli = importlib.util.spec_from_file_location('cli', '/home/ubuntu/Dev/algs-ds/tools/cli.py')
cli = importlib.util.module_from_spec(specCli)
specCli.loader.exec_module(cli)

if len(sys.argv) > 1:
    cli.readArgTo2DArray(sys.argv[1])
else:
    file.readLinesTo2DArray('asdfasdfasdf')