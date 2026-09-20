#  功能:第二周验收
#  作者:wbx
#  日期:2026-09-20

name_students = ['Jack','Tom','Leo','David']    #新建列表

score_students = {      #新建字典
    'Jack' : 91,
    'Tom' : 78,
    'Leo' : 66,
    'David' : 49
}

for name in name_students:      #遍历列表，用name临时变量存列表里的值
    score = score_students[name]        #根据列表的值作为键查字典
    print(f"{name.title()},分数是 {score}.\n")
    if score >= 90 :        #Python 的 if 语句不要求加括号
        print('优秀\n')