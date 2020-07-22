def statis(s):
    count1=count2=count3=count4=0
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            count1=count1+1
        elif ord(i)>=97 and ord(i)<=122:
            count2=count2+1
        elif ord(i)>=48 and ord(i)<=57:
            count3=count3+1
        else:
            count4=count4+1
    print('大写字母个数有%d个'%count1)
    print('小写字母个数有%d个'%count2)
    print('数字有%d个'%count3)
    print('其他字符有%d个'%count4)
    m=(count1,count2,count3,count4)
    print(m)
s=input("请输入一串字符：")
statis(s)