import sys
import numpy as np

# Reading the input split from stdin as numpy array.
input_split = np.genfromtxt(sys.stdin.readlines(), delimiter=",")

X, y_true = input_split[:, :-1], input_split[:, -1]

# Reading the learned model parameters
beta = np.genfromtxt("./model.txt")

# Computing the predictions
y_pred = X.dot(beta)

# Computing the residual sum of squares for the input split
ss_res = np.sum((y_true - y_pred)**2)
# Computing the total sum of squares for the input split
ss_tot = np.sum((y_true - np.sum(y_true)/y_true.shape[0])**2)

# Writing the ss_res and ss_tot to stdout.
sys.stdout.write("none\t")
np.savetxt(sys.stdout, [ss_res, ss_tot], newline=" ")
sys.stdout.write("\n")