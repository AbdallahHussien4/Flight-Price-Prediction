import sys
import pickle

# reading key
key = sys.stdin.buffer.read(1).decode()
# reading tab separator
sys.stdin.buffer.read(1)
# reading value
value = sys.stdin.buffer.read()

data = pickle.loads(value)

print(data)