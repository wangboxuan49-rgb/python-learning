#  功能:电影票
#  作者:wbx
#  日期:2026-09-23

prompt = '请输入您的年龄：（输入 quit 退出）'
active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("免费\n")
        elif age < 12:
            print("收费 10 美元\n")
        else:
            print("收费 15 美元\n")