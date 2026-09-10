#  功能:删除方法练习
#  作者:wbx
#  日期:2026-09-10

name = "   \n\tJohn Wick\t\n "
print(name.lstrip())    #删除字符串左侧空白(包括空格、换行、制表符)
print(name.rstrip())    #删除字符串右侧空白
print(name.strip())     #删除字符串首尾的空白字符


filename = "python_notes.txt"
simple_filename = filename.removesuffix(".txt")     #删除字符串尾部的指定内容
print(simple_filename)