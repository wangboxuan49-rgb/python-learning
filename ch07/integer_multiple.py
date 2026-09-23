#  功能:判断十的整数倍
#  作者:wbx
#  日期:2026-09-23

while True:     #无限循环，遇到break退出循环
    num = input("请输入一个数：（输入 q 退出）")    #获取用户输入，并显示一个提示
    if num =='q':   #使用if语句能够判断退出循环条件
        break

    num = int(num)      #input（）函数输入为字符串，用于数值比较时可以用int（）函数转换为数值

    if num % 10 == 0:       #取模运算
        print(f"{num}是十的整数倍")
    else:
        print(f"{num}不是十的整数倍")