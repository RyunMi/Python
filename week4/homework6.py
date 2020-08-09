""" 创建向量[1,2,3……,100]，并不用循环输出所有3的倍数 """
import numpy as np
A = np.arange(1,101)
B = A[2:100:3]
print(B)