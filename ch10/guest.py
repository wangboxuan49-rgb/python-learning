#  功能:访客
#  作者:wbx
#  日期:2026-10-01

from pathlib import Path

contents = input("请输入你的名字：")    #创建字符串将其写入文件

path = Path('guest.txt')
path.write_text(contents)       #如果路径指定的文件不存在，就创建它，如果指定文件已经存在，将删除其内容，将指定内容写入