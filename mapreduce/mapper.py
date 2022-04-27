import sys

import numpy as np
import pickle


data = np.genfromtxt(sys.stdin.readlines(), delimiter=",")
#data = np.zeros((1,2))

#qr = np.linalg.qr(data)
#serialized = pickle.dumps(data)

#sys.stdout.buffer.write(b'K\t')
#sys.stdout.buffer.write(len(serialized).to_bytes(1, byteorder='big'))\
#print(f'K\t', sep='', end='')

sys.stdout.write("R\t")
np.savetxt(sys.stdout, data, delimiter=",", newline="$")
sys.stdout.write("\n")