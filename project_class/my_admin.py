#  功能:模块导入类
#  作者:wbx
#  日期:2026-09-29

from admin import Admin     #导入模块当中的类，调用无需句点
import user as u        #导入整个模块，并给模块一个别名，避免较长模块名重复出现

# ---- 根据 User 类创建一个实例 ----
user = u.User('明', '李', 24, '北京')       #调用模块中类，用句点调用
user.describe_user()
user.greet_user()

# ---- 调用 increment_login_attempts() 多次 ----
print("\n模拟多次登录尝试：")
for i in range(5):
    user.increment_login_attempts()
    print(f"  第 {i + 1} 次尝试后，login_attempts = {user.login_attempts}")

# ---- 调用 reset_login_attempts() 并再次打印 ----
user.reset_login_attempts()
print(f"\n调用 reset_login_attempts() 后，login_attempts = {user.login_attempts}")

admin_privileges = ['can add post', 'can delete post', 'can ban user']
admin = Admin('明', '李', 24, '北京', admin_privileges)     #创建管理员实例
admin.privileges.show_privileges()      #两级调用