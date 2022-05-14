import sys
import numpy as np
from io import StringIO
import re

ss_res = 0
ss_tot = 0
for line in sys.stdin:
    # Reading key value pair from stdin 
    key, value = re.split("\t", line)
    value = np.genfromtxt(StringIO(value))
    # Summing ss_res and ss_tot from all mappers
    ss_res += value[0]
    ss_tot += value[1]

# Computing the coefficient of determination
r2 = 1 - ss_res/ss_tot

print("Score: ", r2)