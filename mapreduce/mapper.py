import sys

import numpy as np
import pickle


data = np.loadtxt(sys.stdin.readlines(), delimiter=",")

#qr = np.linalg.qr(data)
serialized = pickle.dumps(data)

sys.stdout.buffer.write(b'K\t')
sys.stdout.buffer.write(serialized)
