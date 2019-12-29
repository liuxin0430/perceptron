Perceptron Learning Algorithm implementation

python version: 3.7.4

### The architecture of this project:
DataEmit.py
    implementation of generation of training data 

PLA.py
    implementation of PLA and line plot

### Usage:
Go to this program folder, open the Terminal, then type the following commands:
For generating training data:
    python DataEmit.py [w0,w1,w2] m n
    for example, python DataEmit.py [5,2,3] 100 100
    [w0,w1,w2] specifies the line, m is the number of points with label "+" and n is the number of points with label "-".
    A txt file named "train.txt" will be created in the current directory.

For PLA implementation:
    python PLA.py train.txt
    train.txt is the training data file.
    The Terminal will show out the final learned w. 