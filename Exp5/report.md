# 矩阵特征值计算 

## 上机题1

题目要求矩阵的最大模长的特征值以及对应的特征向量，则使用课上所讲的幂法求解即可。即先初始化一个向量 $x$，然后迭代计算 $x = Ax$，直到 $x$ 收敛。最后计算 $Ax$ 的模长即为特征值，$x$ 即为特征向量。

运行代码 `python P1.py` 后，可以得到如下结果：

```
Eigenvalue of A: 12.254327364587589
Eigenvector of A: [ 0.67401588 -1.          0.88956596]
Correct Eigenvalue of A: 12.254315860794474
Correct Eigenvector of A: [-0.6740206   1.         -0.88955836]
Eigenvalue of B: 98.52160650737164
Eigenvector of B: [-0.60396543  1.         -0.25114387  0.1489578 ]
Correct Eigenvalue of B: 98.52169771010125
Correct Eigenvector of B: [ 0.60397234 -1.          0.25113513 -0.14895345]
```

其中 `Correct` 开头的结果为 `numpy` 库计算得到的正确结果。可以发现使用幂法计算得到的结果与正确结果非常接近。
