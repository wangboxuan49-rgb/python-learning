#  功能:冰激凌店
#  作者:wbx
#  日期:2026-09-29

class Restaurant:
    """一次模拟餐馆的简单尝试"""

    def __init__(self, restaurant_name, cuisine_type):  #特殊方法名不能变，形参 self 必不可少
        """初始化属性餐馆名字以及菜系"""
        self.restaurant_name = restaurant_name  #可通过实例访问的变量称为属性
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):  #定义了两个方法，由于方法执行时不需要额外信息，只有形参 self
        """模拟介绍餐馆名字与菜系"""
        print(f"餐馆是 {self.restaurant_name} ,制作 {self.cuisine_type} 菜。")

    def open_restaurant(self):
        """模拟餐馆是否营业"""
        print("餐馆正在营业！")

    def set_number_served(self, number_served):
        """将服务人数设置为指定的值"""
        self.number_served = number_served

    def increment_number_served(self, number_increse):
        """让就餐人数增加指定的值"""
        self.number_served += number_increse

class IceCreamStand(Restaurant):
    """描述冰淇淋小店"""

    def __init__(self, restaurant_name, cuisine_type,flavors):
        """先初始化父类属性，再初始化冰激凌小店特有属性"""
        super().__init__(restaurant_name, cuisine_type)     #super方法后不应再使用 self
        self.flavors = flavors

    def describe_flavors(self):
        """打印列表内容"""
        for flavor in self.flavors:     #遍历列表
            print(f"冰激凌有{flavor}口味")


icecream_flavors = ['chocolate', 'strawberry']       #列表使用方括号，集合使用花括号（元素无重复）
icecream = IceCreamStand('DQ', 'icecream', icecream_flavors)
icecream.describe_flavors()