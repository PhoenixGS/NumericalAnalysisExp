import numpy as np

def QR_algorithm(A):
    n = len(A)
    for i in range(100):
        Q, R = np.linalg.qr(A)
        A = np.dot(R, Q)
        if i % 10 == 0:
            print('Iteration', i, 'A:\n', A)
    return np.diag(A)

if __name__ == '__main__':
    A = [[0.5, 0.5, 0.5, 0.5], [0.5, 0.5, -0.5, -0.5], [0.5, -0.5, 0.5, -0.5], [0.5, -0.5, -0.5, 0.5]]
    print('Correct Eigenvalues of A:', np.linalg.eig(A)[0])
    print('Eigenvalues of A:', QR_algorithm(A))



