eps = 1e-6

def f1(x):
    return x ** 3 - 2 * x + 2

def f1p(x):
    return 3 * x ** 2 - 2

def f2(x):
    return -x ** 3 + 5 * x

def f2p(x):
    return -3 * x ** 2 + 5

def newton(f, fp, x0):
    x = x0
    for i in range(100):
        x1 = x - f(x) / fp(x)
        if abs(x1 - x) < eps:
            return x1
        print("x = %f" % x1)
        x = x1
    return None

def newton2(f, fp, x0, gamma):
    x = x0
    for i in range(100):
        s = f(x) / fp(x)
        x1 = x - s
        lam = gamma
        lams = []
        while abs(f(x1)) >= abs(f(x)):
            x1 = x - lam * s
            lams.append(lam)
            lam *= gamma
        if abs(x1 - x) < eps:
            return x1
        print("x = %f, lamdas = %s" % (x1, lams))
        x = x1
    return None

if __name__ == '__main__':
    print("function 1: x^3 - 2x + 2")
    print("Newton method:")
    print("Result: ", newton(f1, f1p, 0))
    print("Newton down-hill method:")
    print("Result: ", newton2(f1, f1p, 0, 0.7))
    print("function 2: -x^3 + 5x")
    print("Newton method:")
    print("Result: ", newton(f2, f2p, 1.35))
    print("Newton down-hill method:")
    print("Result: ", newton2(f2, f2p, 1.35, 0.7))

