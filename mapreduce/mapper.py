import sys

import numpy as np
import pickle

def emit(key, value):
    sys.stdout.write(f"{key}\t")
    np.savetxt(sys.stdout, value, delimiter=",", newline="$")
    sys.stdout.write("\n")

input_split = np.genfromtxt(sys.stdin.readlines(), delimiter=",")

q, r = np.linalg.qr(input_split)

emit("Q", q)

