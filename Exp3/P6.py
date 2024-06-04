import numpy as np
import scipy.linalg

def getH(n):
    return scipy.linalg.hilbert(n)
    H = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1/(i+j+1)
    return H

def Cholesky(H, b):
    L = np.zeros_like(H)
    for j in range(H.shape[0]):
        L[j, j] = np.sqrt(H[j, j] - np.sum(L[j, :j] ** 2))
        for i in range(j + 1, H.shape[0]):
            L[i, j] = (H[i, j] - np.dot(L[i, :j], L[j, :j])) / L[j, j]
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(L.T, y)
    return x
    y = np.zeros(L.shape[0])
    for i in range(L.shape[0]):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    L = L.T
    x = np.zeros(L.shape[0])
    for i in range(L.shape[0] - 1, -1, -1):
        x[i] = (y[i] - np.dot(L[i, i + 1:], x[i + 1:])) / L[i, i]
    return x

if __name__ == '__main__':
    n = 10
    H = getH(n)
    b = H @ np.ones(n)
    print("b =", b)
    x = Cholesky(H, b)
    r = b - H @ x
    e = x - np.ones(n)
    print("norm(r) =", np.linalg.norm(r, np.inf))
    print("norm(e) =", np.linalg.norm(e, np.inf))

    print()

    H = getH(n)
    b = H @ np.ones(n)
    b += 1e-7 * np.linalg.norm(b, np.inf)
    print("b =", b)
    x = Cholesky(H, b)
    r = b - H @ x
    e = x - np.ones(n)
    print("norm(r) =", np.linalg.norm(r, np.inf))
    print("norm(e) =", np.linalg.norm(e, np.inf))

    print()

    for n in [8, 10, 12, 14]:
        H = getH(n)
        b = H @ np.ones(n)
        x = Cholesky(H, b)
        r = b - H @ x
        e = x - np.ones(n)
        print("n =", n)
        print("norm(r) =", np.linalg.norm(r, np.inf))
        print("norm(e) =", np.linalg.norm(e, np.inf))
        print()

