#插入排序
def charupaixu(list1):
    for i in range(1, len(list1)):

        key = list1[i]

        j = i - 1
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = key
list1 = list(input("请输入一段数字"))
charupaixu(list1)
print("排序后的数组:",list1)