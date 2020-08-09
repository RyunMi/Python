""" 计算A B矩阵的乘积，A中元素为1-36，按行优先顺序排列；B为对角矩阵，对角线元素为[1,3,5,7,9,11] """
import numpy as np
A = np.arange(1,37).reshape(6,6)
B = np.diag(np.arange(1,12,2))#记忆这个函数
print('矩阵A=\n',A)
print('矩阵B=\n',B)
print('矩阵A B的乘积=\n',np.matmul(A,B))