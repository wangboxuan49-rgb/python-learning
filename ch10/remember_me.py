#  功能:用户字典
#  作者:wbx
#  日期:2026-10-02

from pathlib import Path
import json


def get_stored_user(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)        #读取一个字典
        return user_info
    else:
        return None


def get_new_user(path):
    """提示用户输入用户名"""
    username = input("What is your name? ")
    userage = input("What is your age? ")
    useraddress = input("Where is your address? ") 

    user_info = {
        'username' : username,
        'userage' : userage,
        'useraddress' : useraddress
    } 

    contents = json.dumps(user_info)    #存入一个字典
    path.write_text(contents)

    return user_info


def greet_user():
    """问候用户，并指出其名字"""
    path = Path('user_info.json')
    user_info = get_stored_user(path)   #返回一个字典

    if user_info:       #如果存储过用户信息，就直接打印出来
        print("Welcome back!")
        for userinfo in user_info.values():     #遍历字典中的所有值
            print(f"{userinfo}")
    else:               #如果文件中没有用户信息或者没有文件，就新建并存储信息
        user_info = get_new_user(path)
        print("We'll remember you when you come back!")

        for userinfo in user_info.values():     #遍历字典中的所有值
            print(f"{userinfo}")


greet_user()