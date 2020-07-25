#提示用户输入五个整数，依次存入到列表中，并且按照从大到小的顺序依次输出到终端上
number = input('输入五个数字吧：')
a = list(map(int,list(number))) 
b = sorted(a,reverse=True)
print(b)