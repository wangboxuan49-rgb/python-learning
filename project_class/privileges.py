"""一个描述管理员权限的类"""

class Privileges:
    """规定管理员权限"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """展示管理员权限"""
        for privilege in self.privileges:
            print(f"管理员权限有{privilege}")