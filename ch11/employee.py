#  功能:雇员
#  作者:wbx
#  日期:2026-10-05

class Employee:
    """一个描述雇员年薪的类"""

    def __init__(self, first_name, last_name, salary):
        """描述基本属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_salary = 5000):
        """默认年薪增加 5000 美元，同时能接受其他的年薪增加量"""
        self.salary += add_salary       #不接收形参时，每次调用函数时默认值为 5000
        """
        if add_salary == '':
            self.salary += 5000
        else:
            self.salary += add_salary
        """

    def show(self):
        """打印姓名和年薪"""
        print(f"{self.first_name} {self.last_name}'s salary is {self.salary}")