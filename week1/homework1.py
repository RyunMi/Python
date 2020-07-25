#编写一个函数，调用函数返回四位不含零的随机数
import random
def two(s):
    m=0
    list_2 = [1,2,3,4,5,6,7,8,9]
    random.shuffle(list_2)
    for i in list_2:
        print(i,end="")
        m=m+1
        if m>=4:
            break
s=()
two(s)