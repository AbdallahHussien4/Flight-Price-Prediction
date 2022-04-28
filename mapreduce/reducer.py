import sys
import numpy as np
from io import StringIO
import re


def read_line(line):
    #print(line)
    key, Q, R, Y = re.split("\t|R|Y", line)
    #key, value = line.split('\t')
    Q = Q.replace('$', '\n')
    R = R.replace('$', '\n')
    Y = Y.replace('$', '\n')
    Q = np.genfromtxt(StringIO(Q), delimiter=",")
    R = np.genfromtxt(StringIO(R), delimiter=",")
    Y = np.genfromtxt(StringIO(Y), delimiter=",")
    return key, Q, R, Y

q1 = []
r1 = []
y_list = []

for line in sys.stdin:
    key, q, r, y = read_line(line)
    q1.append(q)
    r1.append(r)
    y_list.append(y)

m = len(q1)

r_tmp = np.vstack(r1)
q2, r2 = np.linalg.qr(r_tmp)
q2 = np.split(q2, m)

q3 = [q1[i].dot(q2[i]) for i in range(m)]

v = [q3[i].T.dot(y_list[i]) for i in range(m)]

coef = np.linalg.inv(r2).dot(np.sum(v, axis=0))

print("parallel QR", coef)