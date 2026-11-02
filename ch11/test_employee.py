#  功能:测试雇员
#  作者:wbx
#  日期:2026-10-05

from employee import Employee
import pytest

@pytest.fixture         #使用装饰器装饰函数，创建一个夹具，生成供多个测试函数使用的资源
def employee_info():
    """一个可以供所有测试函数使用的 Employee 实例"""
    first_name = 'John'
    last_name = 'Wick'
    salary = 10000
    employee_info = Employee(first_name, last_name, salary)     #创建一个对象
    return employee_info        #返回一个实例对象

def test_give_default_raise(employee_info):     #使用夹具资源的测试函数应接受一个与该函数同名的形参
    """测试默认增加年薪功能"""
    employee_info.give_raise()      #通过对象来调用函数
    assert employee_info.salary == 15000

def test_give_custom_raise(employee_info):
    """测试自定义增加年薪功能"""
    employee_info.give_raise(1000)      #通过对象来调用函数
    assert employee_info.salary == 11000