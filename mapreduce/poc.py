import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy.linalg import lstsq

def generate_data(m, w):
    d = w.shape[0]-1
    x = np.random.uniform(-10, 10, (m, d+1))
    x[:, 0] = 1
    y = np.dot(w, x.T)
    np.savetxt('input.csv', np.hstack((x, y.reshape(m, 1))), delimiter=',')
    return x, y

def read_data(filename):
    data = np.loadtxt(filename, delimiter=',')
    x = data[:, :-1]
    y = data[:, -1]
    x[:, 0] = 1
    return x, y

w = np.array([1, 2, 3])
X, y = generate_data(1000, w)
#X, y = read_data('input.csv')
print(X.shape)
print(X.dtype)
reg = LinearRegression().fit(X, y)
#print(reg.score(X, y))
print("sklearn",reg.coef_)
#print(reg.intercept_)

# using OLS
ols = sm.OLS(y, X).fit()
print("OLS", ols.params)

# using lstsq
w_lstsq = lstsq(X, y)[0]
print("scipy", w_lstsq)

# using QR decomposition
Q, R = np.linalg.qr(X)
print("QR", np.linalg.inv(R).dot(Q.T).dot(y))

# parrallelized QR decomposition
m = 5

X_list = np.split(X, m)
y_list = np.split(y, m)

q1 = [np.linalg.qr(X_list[i])[0] for i in range(m)]
r1 = [np.linalg.qr(X_list[i])[1] for i in range(m)]

#q2 = [np.linalg.qr(r1[i])[0] for i in range(m)]
#r2 = [np.linalg.qr(r1[i])[1] for i in range(m)]
r_tmp = np.vstack(r1)
q2, r2 = np.linalg.qr(r_tmp)
q2 = np.split(q2, m)

q3 = [q1[i].dot(q2[i]) for i in range(m)]

v = [q3[i].T.dot(y_list[i]) for i in range(m)]

coef = np.linalg.inv(r2).dot(np.sum(v, axis=0))

print("parallel QR", coef)