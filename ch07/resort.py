#  功能:梦想中的度假圣地
#  作者:wbx
#  日期:2026-09-23

resorts = {}

prompt1 = 'What your name?\n'
prompt2 = 'If you could visit one place in the world, where would you go?\n'
prompt3 = 'Would you like to let another person respond?(yes or no)\n'
active = True       #循环标志

while active:
    name = input(prompt1)       #新的键
    response = input(prompt2)   #新的值

    resorts[name] = response    #向字典里新增键值对

    repeat = input(prompt3) 
    while True:         #判断是否还有人要接受调查,保证只能输入 yes 或 no
        if repeat == 'no':
            active = False      #退出外层循环
            break               #退出内层循环
        elif repeat == 'yes':
            break               #退出内层循环，但是不退出外层循环
        else:
            print('Plese try again!(yes or no)')