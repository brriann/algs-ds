
This is a repo in which I will be implementing algs + data structures
taught in Princeton's A+DS course. (Sedgewick)

algs4.cs.princeton.edu


Round 1 (Winter 2020): Java, Python, JS

00. Tools

    file: read a multi-line file with space delimiters to a 2D array

    cli: read CLI arg with row + cell delimiters to a 2D array

0. Intro

    0Intro.js, 0Intro.py, Intro.java

    intro exercise.  test tools. 
    
    Input a 2D array using cli and file tools, log to output A.) the full 2D array, B.) each row, and C.) each cell

1. Union-Find

    1unionfind.js, 1unionfind.py, Unionfind.java

    implement union-find

2. Quick-Find

    2quickfind.js, 2quickfind.py, Quickfind.java

    implement quick-find version of union-find

3. Quick-Union

    3quickunion.js, 3quickunion.py, Quickunion.java

    implement quick-union version of union-find


    

Dev Notes:

cd algs-ds/js
node Intro.js
node Intro.js 1-2-3/4-5-6/7-8-9

cd algs-ds
source .env/venv/bin/activate
cd py
python Intro.py
python Intro.py 1-2-3/4-5-6/7-8-9

cd algs-ds
javac java1/*.java
java java1/Intro.java
java java1/Intro.java 1-2-3/4-5-6/7-8-9