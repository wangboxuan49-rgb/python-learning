"""一个用于表示用户的类"""      #模块开始用文档字符串来进行描述，模块可以存储任意多的类

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
