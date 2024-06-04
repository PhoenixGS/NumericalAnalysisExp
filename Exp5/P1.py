import numpy as np

def getA():
    return [[5, -4, 1], [-4, 6, -4], [1, -4, 7]]

def getB():
    return [[25, -41, 10, -6], [-41, 68, -17, 10], [10, -17, 5, -3], [-6, 10, -3, 2]]

def get_evi(A):
    x = np.ones(len(A))
    while True:
        x_new = np.dot(A, x)
        lam = np.linalg.norm(x_new, np.inf)
        x_new /= lam
        if np.linalg.norm(x_new - x, np.inf) < 1e-5:
            break
        x = x_new
    return lam, x

if __name__ == '__main__':
    A = getA()
    lam, x = get_evi(A)
    print('Eigenvalue of A:', lam)
    print('Eigenvector of A:', x)
    print('Correct Eigenvalue of A:', np.linalg.eig(A)[0][0])
    print('Correct Eigenvector of A:', np.linalg.eig(A)[1][:, 0] / np.linalg.norm(np.linalg.eig(A)[1][:, 0], np.inf))
    B = getB()
    lam, x = get_evi(B)
    print('Eigenvalue of B:', lam)
    print('Eigenvector of B:', x)
    print('Correct Eigenvalue of B:', np.linalg.eig(B)[0][0])
    print('Correct Eigenvector of B:', np.linalg.eig(B)[1][:, 0] / np.linalg.norm(np.linalg.eig(B)[1][:, 0], np.inf))
