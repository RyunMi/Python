""" 定义一个学生类
有下面的类属性：1.姓名2.年龄3.成绩（语文，数学，英语）【每课成绩的类型为整数】
类方法
1.获取学生的姓名：get_name() 返回类型：str
2.获取学生的年龄：get_age() 返回类型：int
3.返回3门科目中最高的分数。get_course() 返回类型：int """
class Student(object):
    def __init__(self,name,age,chinese,math,english):
        self.name=name
        self.age =age
        self.c = chinese
        self.m = math
        self.e = english
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        if self.c >= self.m and self.c >= self.e:
            return self.c
        if self.m>= self.c and self.m >=self.e:
            return self.m
        if self.e >= self.c and self.e>= self.m:
            return self.e
""" lisa=Student('Lisa',17,100,100,100)
print(lisa.get_name(),lisa.get_age(),lisa.get_course()) """
