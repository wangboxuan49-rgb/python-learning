#  功能:管理员权限
#  作者:wbx
#  日期:2026-09-29

class User:
    """一个表示用户的简单类。"""

    def __init__(self, first_name, last_name, age, city):
        """初始化用户的基本信息。"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0          # 新增属性：登录尝试次数

    def describe_user(self):
        """打印用户信息摘要。"""
        print(f"用户信息：{self.last_name}{self.first_name}"
              f"，{self.age} 岁，来自 {self.city}。")

    def greet_user(self):
        """向用户发出个性化问候。"""
        print(f"你好，{self.first_name}！欢迎回来。")

    def increment_login_attempts(self):
        """将登录尝试次数加 1。"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将登录尝试次数重置为 0。"""
        self.login_attempts = 0

class Privileges:
    """规定管理员权限"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """展示管理员权限"""
        for privilege in self.privileges:
            print(f"管理员权限有{privilege}")

class Admin(User):
    """管理员是一种特殊的用户"""

    def __init__(self, first_name, last_name, age, city, privileges):
        """初始化父类属性，再初始化管理员特殊属性"""
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges(privileges)      #用实例来作为类中的属性，需要传入参数


admin_privileges = ['can add post', 'can delete post', 'can ban user']
admin = Admin('明', '李', 24, '北京', admin_privileges)     #创建管理员实例
admin.privileges.show_privileges()      #两级调用