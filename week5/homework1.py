#编写一个numpy程序将数组a,b分别沿0轴和1轴进行拼接
import numpy as np
a = np.array([1,1,2,3,3,4,5,6])
b = np.array([2,3,4,5,2,4,2,1])
c = np.concatenate((a,b),axis=0)
print("按0轴拼接为",c)
""" 结果：
按0轴拼接为 [1 1 2 3 3 4 5 6 2 3 4 5 2 4 2 1] """
"""d = np.concatenate((a,b),axis=1)
这样会报错，一维数组只有0轴 """
