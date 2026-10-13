#  功能:餐馆
#  作者:wbx
#  日期:2026-09-28

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

france_restaurant = Restaurant('A', 'french')   #根据类来创建实例

print(france_restaurant.restaurant_name)    #访问实例的属性，使用点号
print(france_restaurant.cuisine_type)

#print(f"有 {france_restaurant.number_served} 人在餐馆用餐过。")
#france_restaurant.number_served = 50        #通过实例访问属性，再直接修改
#print(f"有 {france_restaurant.number_served} 人在餐馆用餐过。")

#print(f"有 {france_restaurant.number_served} 人在餐馆用餐过。")
#france_restaurant.set_number_served(50)        #通过方法修改属性的值
#print(f"有 {france_restaurant.number_served} 人在餐馆用餐过。")

print(f"有 {france_restaurant.number_served} 人在餐馆用餐过。")
france_restaurant.increment_number_served(50)   #通过方法让属性的值递增
print(f"有 {france_restaurant.number_served} 人在餐馆用餐过。")

france_restaurant.describe_restaurant()     #调用类中定义的任何方法，使用点号
france_restaurant.open_restaurant()