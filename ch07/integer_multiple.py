#  功能:判断十的整数倍
#  作者:wbx
#  日期:2026-09-23

while True:     #无限循环，遇到break退出循环
    num = input("请输入一个数：（输入 q 退出）")
    if num =='q':
        break

    num = int(num)

    if num % 10 == 0:
        print(f"{num}是十的整数倍")
    else:
        print(f"{num}不是十的整数倍")