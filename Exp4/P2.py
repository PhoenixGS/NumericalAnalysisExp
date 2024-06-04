import numpy as np

eps = 1e-5

def Jacobi(A, b, x0):
    n = len(A)
    x = x0.copy()
    while True:
        x_new = np.zeros(n)
        for j in range(n):
            x_new[j] = b[j]
            for (k, val) in A[j]:
                if k != j:
                    x_new[j] -= val * x[k]
            for (k, val) in A[j]:
                if k == j:
                    x_new[j] /= val
        if np.linalg.norm(x_new - x, np.inf) < eps:
            break
        x = x_new
    return x

def GaussSeidel(A, b, x0):
    n = len(A)
    x = x0.copy()
    while True:
        x_new = np.zeros(n)
        for j in range(n):
            x_new[j] = b[j]
            for (k, val) in A[j]:
                if k < j:
                    x_new[j] -= val * x_new[k]
                elif k > j:
                    x_new[j] -= val * x[k]
            for (k, val) in A[j]:
                if k == j:
                    x_new[j] /= val
        if np.linalg.norm(x_new - x, np.inf) < eps:
            break
        x = x_new
    return x

def SOR(A, b, x0, w):
    n = len(A)
    x = x0.copy()
    while True:
        x_new = np.zeros(n)
        for j in range(n):
            x_new[j] = b[j]
            for (k, val) in A[j]:
                if k < j:
                    x_new[j] -= val * x_new[k]
                elif k > j:
                    x_new[j] -= val * x[k]
            for (k, val) in A[j]:
                if k == j:
                    x_new[j] /= val
            x_new[j] = w * x_new[j] + (1 - w) * x[j]
        if np.linalg.norm(x_new - x, np.inf) < eps:
            break
        x = x_new
    return x

def getAb(varepi, a, n):
    A = []
    b = np.zeros(n)
    h = 1 / n
    for i in range(n):
        A.append([])
        A[i].append((i, -2 * varepi))
        if i > 0:
            A[i].append((i - 1, varepi - h / 2))
        if i < n - 1:
            A[i].append((i + 1, varepi + h / 2))
        b[i] = a * h * h
    b[n - 1] = b[n - 1] - varepi - h / 2
    return A, b

if __name__ == '__main__':
    a = 1 / 2
    n = 1000
    for varepi in [1, 0.1, 0.01, 0.001]:
        print('varepi =', varepi)
        A, b = getAb(varepi, a, n - 1)
        x = np.zeros(n - 1)
        for i in range(n - 1):
            x[i] = (i + 1) / n
        exact_y = (1 - a) / (1 - np.exp(-1 / varepi)) * (1 - np.exp(-x / varepi)) + a * x
        # print(exact_y)
        y0 = np.zeros(n - 1)
        y = Jacobi(A, b, y0)
        # print(y)
        print("Jacobi:", np.linalg.norm(y - exact_y, np.inf) / np.linalg.norm(exact_y, np.inf))
        y = GaussSeidel(A, b, y0)
        # print(y)
        print("GaussSeidel:", np.linalg.norm(y - exact_y, np.inf) / np.linalg.norm(exact_y, np.inf))
        y = SOR(A, b, y0, 0.9)
        # print(y)
        print("SOR:", np.linalg.norm(y - exact_y, np.inf) / np.linalg.norm(exact_y, np.inf))

    print()

    varepi = 1
    for n in [10, 100, 1000]:
        print('n =', n)
        A, b = getAb(varepi, a, n - 1)
        x = np.zeros(n - 1)
        for i in range(n - 1):
            x[i] = (i + 1) / n
        exact_y = (1 - a) / (1 - np.exp(-1 / varepi)) * (1 - np.exp(-x / varepi)) + a * x
        # print(exact_y)
        y0 = np.zeros(n - 1)
        y = Jacobi(A, b, y0)
        # print(y)
        print("Jacobi:", np.linalg.norm(y - exact_y, np.inf) / np.linalg.norm(exact_y, np.inf))
        y = GaussSeidel(A, b, y0)
        # print(y)
        print("GaussSeidel:", np.linalg.norm(y - exact_y, np.inf) / np.linalg.norm(exact_y, np.inf))
        y = SOR(A, b, y0, 0.9)
        # print(y)
        print("SOR:", np.linalg.norm(y - exact_y, np.inf) / np.linalg.norm(exact_y, np.inf))
