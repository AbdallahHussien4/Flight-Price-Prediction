import sys
import pickle
import numpy as np
from io import StringIO

def read_line(line):
    key, value = line.split('\t')
    value = value.replace('$', '\n')
    data = np.genfromtxt(StringIO(value), delimiter=",")
    #print(key, data)
    return key, data

for line in sys.stdin:
    #print(line)
    key, value = read_line(line)


# for line in sys.stdin:
#     key, value = sys.stdin.readline().split('\t')
#     s = StringIO(sys.stdin.read())
#     data = np.loadtxt(sys.stdin, delimiter=",")
#     data = pickle.loads(line)
# print(data)
    

    # # reading key
    # key = sys.stdin.buffer.read(1).decode()
    # # reading tab separator
    # sys.stdin.buffer.read(1)
    # # reading value
    # value = sys.stdin.buffer.read()

    # #data = pickle.loads(value)

    #print(key)
#except Exception as e:
#    print(e)