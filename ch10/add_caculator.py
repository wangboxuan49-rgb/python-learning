#  功能:加法计算
#  作者:wbx
#  日期:2026-10-02

def add_caculator(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print("输入数据类型错误，请重新输入")
        else:
            return num

num1 = add_caculator('请输入第一个整数：')      #封装成函数能够避免输入错误时num1未定义导致 NameError
num2 = add_caculator('请输入第二个整数：')
result = num1 + num2
print(result)