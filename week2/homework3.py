#冒泡排序
def bubble_sort(lists):
    count = len(lists)
    for i in range(count-1):
        for j in range(count-i-1):
            if lists[j]>lists[j+1]:
                lists[j],lists[j+1] = lists[j+1],lists[j]
    return lists
lists = list(input("请输入一段数字"))
bubble_sort(lists)
print("排序后的数组：",lists)   