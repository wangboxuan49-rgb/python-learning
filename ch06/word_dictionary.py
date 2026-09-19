#  功能:词汇表
#  作者:wbx
#  日期:2026-09-19

word_explain = {        #创建字典，实质上是任意个键值对组成
    'while':'入口条件循环',
    'do while':'出口条件循环',
    'if':'判断',
    'list':'列表（一系列值）',
    'dictionary':'字典（一系列键值对）'
}

explain = word_explain['while']     #通过键来访问字典的值
print(f"'while'\n\tmeans {explain}\n")

explain = word_explain['do while']
print(f"'do while'\n\tmeans {explain}\n")

explain = word_explain['if']
print(f"'if'\n\tmeans {explain}\n")

explain = word_explain['list']
print(f"'list'\n\tmeans {explain}\n")

explain = word_explain['dictionary']
print(f"'dictionary'\n\tmeans {explain}\n")

explain = word_explain.get('for','没有这个词汇')    #get()方法可以在指定键不存在时返回一个默认值
print(explain)