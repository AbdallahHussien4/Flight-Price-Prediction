import sys
import numpy as np
from io import StringIO
import re

# Reads the numpy arrays from stdin key value pair.
def read_line(line):
    key, Q, R, Y = re.split("\t|R|Y", line)
    Q = Q.replace('$', '\n')
    R = R.replace('$', '\n')
    Y = Y.replace('$', '\n')
    Q = np.genfromtxt(StringIO(Q), delimiter=",")
    R = np.genfromtxt(StringIO(R), delimiter=",")
    Y = np.genfromtxt(StringIO(Y), delimiter=",")
    return key, Q, R, Y


Q1 = []
R1 = []
Y = []

for line in sys.stdin:
    key, q, r, y = read_line(line)
    Q1.append(q)
    R1.append(r)
    Y.append(y)

m = len(Q1)

R_tmp = np.vstack(R1)
Q2, R2 = np.linalg.qr(R_tmp)
Q2 = np.split(Q2, m)

Q3 = [Q1[i].dot(Q2[i]) for i in range(m)]

V = [Q3[i].T.dot(Y[i]) for i in range(m)]

beta = np.linalg.inv(R2).dot(np.sum(V, axis=0))

print("Model coefficients: ", beta)
