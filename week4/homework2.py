class Listinfo(object):
    def __init__(self,list):
        self.list = list
    def add_key(self,keyname):
        self.list.append(keyname)
        return self.list
    def get_key(self,num):
        return self.list[num]
    def update_list(self,list2):
        self.list.extend(list2)#记忆这个函数
        #self.list+= list2
        return self.list
    def del_key(self):
        return self.list.pop()
list_info = Listinfo([44,222,111,333,454,'sss','333'])
print(list_info.add_key('1111'))
print(list_info.get_key(4))
print(list_info.update_list(['1','2','3']))
print(list_info.del_key())