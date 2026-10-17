#  功能:python学习笔记
#  作者:wbx
#  日期:2026-09-30

from pathlib import Path    #pathlib 模块（库）导入 Path 类，其对象指向一个文件

path = Path('learning_python.txt')      #程序和文件位于同一个目录中时，知道其文件名就可以访问
contents = path.read_text()     #使用read_text() 方法读取文件的全部内容
print(contents)

lines = contents.splitlines()       #splitlines()方法将字符串转化为一系列行，返回一个列表
for line in lines:      #可以简化临时变量，for line in contents.splitlines()
    print(line)

for line in lines:
    print(line.replace('Python', 'C'))  #replace()方法返回一个新字符串，不是在原来上面修改