#实现用户输入用户名和密码，当用户名为 seven 且密码为 123 时，显示登陆成功，否则登陆失败，失败时允许重复输入三次答
dic = {'seven':123}
a = input("请输入用户名：")
b = int(input("请输入密码："))
c = a in dic
d = dic['seven']
cnt = 0
if c and (b == d):
        print("登录成功")
else:
    print('登陆失败 请重新输入 您还有3次机会')
    while cnt < 3:
        i = input('请输入用户名')
        j = int(input('请输入密码'))
        k = i in dic
        if k and (i == d):
            print('登陆成功')
            break
        else:
            print("登陆失败 您还有%d次机会"%(2-cnt))
        cnt = cnt + 1        