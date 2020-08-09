#图像（要用jupter扩展才能输出）
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-np.pi,np.pi,20)
def f(x):
    return x**2
y = f(x)
plt.plot(x,y,'r')