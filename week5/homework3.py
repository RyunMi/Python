#编写一个numpy程序来找出数组a中等于1的数的位置
import numpy as np
a = np.array([1,1,2,3,3,4,5,6])
print("a中等于1的位置为",np.where(a == 1))
""" 结果：
a中等于1的位置为 (array([0, 1], dtype=int64),) """
#注意np.where函数用来定位，还有一些进阶用法