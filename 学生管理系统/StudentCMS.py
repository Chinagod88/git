"""
学生管理系统:StudentCMS
管理学员
添加，修改，删除，查询，保存，退出
"""

# 导包
from Student import Student
import time

class StudentCMS(object):
    def __init__(self):
        self.stu_list = []  #学生对象

    @staticmethod
    def show_view():
        print('-'*23)
        print('学生管理系统')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('-'*23,'\n')

    def add_stu(self):
        name = input('请输入姓名:')
        age = int(input('请输入年龄:'))
        gender = input('请输入性别:')
        mobile = input('请输入联系电话:')
        description = input('请输入学生描述:')
        stu = Student(name, age, gender, mobile, description)
        self.stu_list.append(stu)
        print(f'{name}学生信息添加成功')

    def del_stu(self):
        name = input('请输入要删除的学生姓名:')
        for s in self.stu_list:
            if s.name == name:
                self.stu_list.remove(s)
                print(f'{name}学生信息删除成功')
                return
        print(f'{name}学生信息不存在')

    def query_stu(self):
        name = input('请输入要查询的学生姓名:')
        for s in self.stu_list:
            if s.name == name:
                print(s)
                break
        else:
            print(f'{name}学生信息不存在')

    def save_stu(self):
        with open('./student_data.txt','w',encoding='utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            dest_f.write(str(stu_dict))
            print('学生信息保存成功')

    def mod_stu(self):
        name = input('请输入要修改的学生姓名:')
        for s in self.stu_list:
            if s.name == name:
                s.age = int(input('请输入年龄:'))
                s.gender = input('请输入性别:')
                s.mobile = input('请输入联系电话:')
                s.description = input('请输入学生描述:')
                print(f'{name}学生信息修改成功')
                break
        else:
            print(f'{name}学生信息不存在')

    def query_all_stu(self):
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        else:
            print('当前系统中无学生信息')
        print()

    def load_stu(self):
        try:
            with open('./student_data.txt','r',encoding='utf-8') as src_f:
                stu_dict = eval(src_f.read())
                if len(stu_dict) > 0:
                    self.stu_list = [Student(**stu) for stu in stu_dict]
                else:
                    self.stu_list = []
        except:
            with open('./student_data.txt','w',encoding='utf-8') as src_f:
                self.stu_list = []
        
        def exit(self):
            pass

    def start(self):
        self.load_stu()
        while True:
            time.sleep(2)
            StudentCMS.show_view()
            input_snum = input('请输入您的选择:')
            if input_snum == '1':
                self.add_stu()
            elif input_snum == '2':
                self.del_stu()
            elif input_snum == '3':
                self.mod_stu()
            elif input_snum == '4':
                self.query_stu()
            elif input_snum == '5':
                self.query_all_stu()
            elif input_snum == '6':
                self.save_stu()
            elif input_snum == '0':
                print('是否退出系统?')
                input_snum = input('请输入(y/n): ->')
                if input_snum.lower() == 'y':
                    self.save_stu()
                    print('谢谢使用')
                    self.exit()
                    break
            else:
                print('输入有误,请重新输入!')