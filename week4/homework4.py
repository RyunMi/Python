""" 画出函数f(x)=e^sinx在区间[-1，1]图像 """
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1,1,20)
def f(x):
    return np.sin(x)
def g(x):
    return np.e**x
def h(X):
    return g(f(x))
y = h(x)
plt.plot(x,y,'r')
#图像（要用jupter扩展才能输出,查看——命令面板——输入jupy——点第一个）