from user import User
from privileges import Privileges

class Admin(User):
    """管理员是一种特殊的用户"""

    def __init__(self, first_name, last_name, age, city, privileges):
        """初始化父类属性，再初始化管理员特殊属性"""
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges(privileges)      #用实例来作为类中的属性，需要传入参数