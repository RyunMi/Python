number = input('输入五个数字吧：')
a = list(map(int,list(number))) 
b = sorted(a,reverse=True)
print(b)