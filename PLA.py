#!/usr/bin/python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import sys
import math

#self defined PLA function
def my_pla(train_data):
    w = np.random.randint(-10,10,3)
    #print("start w = {}".format(w))
    ite_flag = 1
    ite_cnt = 0

    while ite_flag == 1:
        ite_cnt += 1
        ite_flag = 0
        np.random.shuffle(train_data) #shuffle train data
        for data in train_data:
            #print(data)
            label = data[2]
            #print(label)
            if label != 1 and label != -1:
                continue
            #print(w)
            h = np.dot(w,np.array([1,data[0],data[1]]))
            h = np.sign(h)
            #print(h)
            #print(type(h))

            if h != label:
                w = w + label*np.array([1,data[0],data[1]])
                ite_flag = 1
                break

    #print(f'iteration count = {ite_cnt}')
    print("PLA w = {}".format(w))
    return w


#get train data
filepath = sys.argv[1] if len(sys.argv) == 2 else "train.txt"
data_file  = open(filepath)
lines = data_file.readlines()
data_num = len(lines)
train_data = np.zeros([data_num, 3])#for train_data storage
bad_num = 0 #the number of bad data

for idx, line in enumerate(lines):
    line = line.strip('\n')
    line_split = line.split(' ')
    if len(line_split) != 3:
        bad_num += 1
        continue
    #print(line_split)
    x1 = float(line_split[0])
    x2 = float(line_split[1])
    label = +1 if line_split[2] == '+' else -1
    train_data[idx] = np.array([x1,x2,label])

#plot figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('PLA')
plt.xlabel('x1')
plt.ylabel('x2')
pp = ax.scatter(train_data[train_data[:,2] == +1, 0],train_data[train_data[:,2] == +1, 1], c='b',marker='o')#positive blue circle
pn = ax.scatter(train_data[train_data[:,2] == -1, 0],train_data[train_data[:,2] == -1, 1], c='r',marker='x')#negative red cross
plt.legend([pp,pn],['+1','-1'])

w = my_pla(train_data)# do PLA

x1_max = train_data[:,0].max()
x1_max = math.ceil(x1_max) + 1
x1_min = train_data[:,0].min()
x1_min = math.floor(x1_min) - 1

x2_max = train_data[:,1].max()
x2_max = math.ceil(x2_max) + 1
x2_min = train_data[:,1].min()
x2_min = math.floor(x2_min) - 1

f_x1 = np.arange(x1_min, x1_max, 0.1)
f_x2 = np.arange(x2_min, x2_max, 0.1)
f_x1, f_x2 = np.meshgrid(f_x1, f_x2)
f = w[0] + w[1]*f_x1 + w[2]*f_x2
plt.contour(f_x1, f_x2, f, 0, colors='k')#black line

""" #plot known line
k_w = np.array([1,1,1])
k_x1 = np.arange(x1_min, x1_max, 0.1)
k_x2 = np.arange(x2_min, x2_max, 0.1)
k_x1, k_x2 = np.meshgrid(k_x1, k_x2)
f_k = k_w[0] + k_w[1]*k_x1 + k_w[2]*k_x2
plt.contour(k_x1, k_x2, f_k, 0, colors='g', linestyles='dotted')#green dotted-line """

plt.show()