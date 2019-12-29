#!/usr/bin/python
# coding: utf-8

import sys
import re
import random

#python DataEmit.py [2,3,4] 20 30
#default parameters
wstr = "1,2,3"
m = 5
n = 4

#get input argument
if len(sys.argv[1:]) != 3:
    raise IOError('''please input three parameters: 
    1) [w0,w1,w2]
    2) m
    3) n
    for example: python DataEmit.py [1,2,3] 4 5
    ''')

wstr = sys.argv[1]
pattern = re.compile(r'\d+')
w = pattern.findall(wstr)
if len(w) != 3:
    raise IOError("input parameter should be a three-dimentional vector [w0,w1,w2]")
w0 = int(w[0])
w1 = int(w[1])
w2 = int(w[2])

m = int(sys.argv[2])
n = int(sys.argv[3])
if m < 1 or n < 1:
    raise ValueError("m and n should be positive numbers")

#clear train.txt
data_file = open('train.txt','w+')
data_file.truncate()
data_file.close()

#generate train data
rand_range = 100
while m > 0 or n > 0:
    x1 = random.uniform(-rand_range, rand_range)
    x1 = round(x1,1)
    x2 = random.uniform(-rand_range, rand_range)
    x2 = round(x2,1)
    if m > 0 and w1*x1+w2*x2+w0 > 0:
        m -= 1
        #print("{} {} +".format(x1,x2))
        with open("train.txt",'a') as f:
            f.write("{} {} +\n".format(x1,x2))
    if n > 0 and w1*x1+w2*x2+w0 < 0:
        n -= 1
        #print("{} {} -".format(x1,x2))
        with open("train.txt",'a') as f:
            f.write("{} {} -\n".format(x1,x2))

f.close()
print("The training data has been generated successfully!")