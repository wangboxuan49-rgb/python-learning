#  功能:检查用户名
#  作者:wbx
#  日期:2026-09-17

current_users = ['Tom','John','Jack','Leo','Alex'] 
new_users = ['Jerry','John','Luke','Bill','Alex']
current_users_lower = []

#创建列表的小写副本，使用遍历来在空列表追加元素
#也可以用列表推导式来创建列表：current_users_lower = [user.lower() for user in current_users]
for current_user in current_users:
    current_users_lower.append(current_user.lower())
print(current_users_lower)

for new_user in new_users:      #遍历来判断当前列表元素是否在另一列表当中
    if new_user.lower() in current_users_lower:
        print(f"{new_user}用户名已被使用，请更换用户名！")
    elif new_user.lower() not in current_users_lower:       #直接使用else也可以
        print(f"{new_user}用户名未被使用！")
    