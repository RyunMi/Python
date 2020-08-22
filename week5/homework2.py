#编写一个numpy程序来计算数组a中各个数的出现次数
import numpy as np
a = np.array([1,1,2,3,3,4,5,6])
for i in np.unique(a):
    print(i,"的个数为",np.sum(a==i))
""" 结果：
1 的个数为 2
2 的个数为 1
3 的个数为 2
4 的个数为 1
5 的个数为 1
6 的个数为 1 """
"""np.unique用来删除重复元素 
注意代码里np.sum的用法
还可以用Counter函数，但要在最前面加
from collections import Counter
用Counter(a) """
