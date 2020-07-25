print(123)
print("456.789")
print('\'Hello, world\'')
print('\'Hello, \\\'Adam\\\'\'')
print('r\'Hello, \"Bart\"\'')
print('''r\'\'\'Hello,
Lisa!\'\'\'''')
print("123\t456\n")
for i in range(1,10):
     for j in  range(1,i+1):
        print("%d*%d=%2d"%(j,i,j*i),end=' ')
     print("")