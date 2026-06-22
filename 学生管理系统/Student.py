class Student(object):
    def __init__(self, name, age ,gender, mobile ,description ):
        """
        该魔法方法，用于初始化属性信息
        :param name:
        :param age:
        :param gender:
        :param mobile:
        :param description:
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.description = description
 

    def __str__(self):
        return f'姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 联系电话: {self.mobile}, 描述: {self.description}'
        
if __name__ == '__main__':
    s = Student('张三',18,'男','0001','爱吃火龙果')
    print(s)
