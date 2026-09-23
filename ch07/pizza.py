#  功能:披萨配料
#  作者:wbx
#  日期:2026-09-23

prompt = "请输入一种披萨配料：（输入 quit 退出）"        #将提示用变量存起来
topping = ''        #将变量初始值设置为空字符串

while topping != 'quit':    #用while条件测试来退出循环
    topping = input(prompt)

    if topping != 'quit':       #为了防止把quit也作为一条消息打印
        print(f"披萨中添加了{topping}\n")