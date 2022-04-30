import sys
import numpy as np

# Writes the numpy arrays to stdout as one key value pair.
def write_line(key, Q, R, Y):
    sys.stdout.write(f"{key}\t")
    np.savetxt(sys.stdout, Q, delimiter=",", newline="$")
    sys.stdout.write("R")
    np.savetxt(sys.stdout, R, delimiter=",", newline="$")
    sys.stdout.write("Y")
    np.savetxt(sys.stdout, Y, delimiter=",", newline="$")
    sys.stdout.write("\n")


# Reading the input split from stdin as numpy array.
input_split = np.genfromtxt(sys.stdin.readlines(), delimiter=",")

X, y = input_split[:, :-1], input_split[:, -1]

# Getting the QR decomposition.
q, r = np.linalg.qr(X)

# Writing the output to stdout.
write_line("none", q, r, y)
