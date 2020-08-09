class dictclass(object):
    def __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        if (key in self.dict):
            dict.pop(key)
        else:
            return 'not found'
    def get_dict(self,key):
        if (key in self.dict.keys()):
            """ if里最后有没有.keys()函数好像是一样的结果，而且如果输入“value”一样是找不到 """
            return self.dict[key]
        else:
            return "not found"
    def get_key(self):#这里的参数只有self就行，因为没传入参数，而前面的方法中传入了多余的参数，就要多写参数在（）里
        return self.dict.keys()
    def update_dict(self,dict2):
        self.dict.update(dict2)
        return self.dict
    """ 这里如果直接返回 return self.dict.update(dict2)会输出None，说明update()这个函数不能这样用？ """
A = dictclass({'a':1,'b':2})
print(A.get_dict('c'))
print(A.del_dict('c'))
print(A.get_key())
print(A.update_dict({'c':3,'d':4}))