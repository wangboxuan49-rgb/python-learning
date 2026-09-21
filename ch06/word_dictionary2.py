#  功能:词汇表2
#  作者:wbx
#  日期:2026-09-21

word_explain = {        #创建字典，实质上是任意个键值对组成
    'while':'入口条件循环',
    'do while':'出口条件循环',
    'if':'判断',
    'list':'列表（一系列值）',
    'dictionary':'字典（一系列键值对）'
}

word_explain['int'] = '整数类型'            #在字典中新增键值对，在空字典中添加很方便
word_explain['float'] = '浮点数类型'
word_explain['double'] = '双精度浮点数类型'
word_explain['char'] = '字符类型'
word_explain['signed'] = '有符号类型'

for word, explain in word_explain.items():      #声明两个变量，分别存储键和值，items（）方法返回一个键值对列表
    print(f"word: {word}")
    print(f"explain: {explain}\n")