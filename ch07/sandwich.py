#  功能:熟食店
#  作者:wbx
#  日期:2026-09-23

sandwich_oreders = ['chicken sandwich','pastrami','beef sandwich','pastrami','fish sandwich','pastrami']

finished_sandwiches = []

while 'pastrami' in sandwich_oreders:       #利用while循环，删除列表里所有指定元素
    sandwich_oreders.remove('pastrami')

print(sandwich_oreders)

while sandwich_oreders:     #对列表进行遍历
    finished_sandwich = sandwich_oreders.pop()      #弹出末尾元素给临时变量赋值
    finished_sandwiches.append(finished_sandwich)   #添加到新列表中
    print(f"I made your {finished_sandwich}.")

print(finished_sandwiches)      #打印新增了元素的空列表