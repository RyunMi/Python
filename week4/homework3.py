""" 定义一个集合的操作类：Setinfo
包括的方法:
1 集合元素添加: add_setinfo(keyname) [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

初始代码：
A = set([1, 2, 3, 4, 5, 2])
B = set([5, 6, 3])
set_info = Setinfo(A)
print set_info.add_setinfo('f')
print set_info.get_intersection(B)
print set_info.get_union(B)
print set_info.del_difference(B)
 """
class Setinfo(object):
    def __init__(self,set):
        self.set = set
    def add_setinfo(self,keyname):
        self.set.add(keyname)
        return self.set
    def get_intersection(self,unioninfo):
        return self.set&unioninfo
    def get_union(self,unioninfo):
        return self.set|unioninfo
    def del_difference(self,unioninfo):
        return self.set-unioninfo
A = set([1,2,3,4,5,2])
B = set([5,6,3])
set_info = Setinfo(A)
print(set_info.add_setinfo('f'))
print(set_info.get_intersection(B))
print(set_info.get_union(B))
print(set_info.del_difference(B))