#求1-2+3-4+5......99的所有数的和
sum = 0
for i in range(100):
    if (i%2) == 0:
        i = -i
    sum = sum+i
print("1-2+3-4+5......99=",sum)