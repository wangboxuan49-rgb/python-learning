#  功能:访客簿
#  作者:wbx
#  日期:2026-10-01

from pathlib import Path

contents = ''       #定义字符串同时避免循环可能一次不执行，导致读到一个不存在的变量

while True:
    guest_name =  input('请输入用户的名字：(输入 q 退出)')

    if guest_name == 'q':       #判断输入，实现退出循环
        break;

    #contents += guest_name 是"先读后写"，contents = contents + guest_name，所以要提前定义字符串
    #                                                ↑ 先读这里的 contents
    contents += guest_name      #将所有输入都存入字符串当中
    contents += '\n'

guest = Path('guest_book.txt')
guest.write_text(contents)