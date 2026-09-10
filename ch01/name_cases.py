#  功能:字符串练习
#  作者:wbx
#  日期:2026-09-09

name = "eric"   #用字符串给变量赋值
#使用 f 字符串在字符串中插入变量的值，并且使用方法让首字母大写
print(f"Hello {name.title()},would you like to learn some Python today?")   


name = "joHnSon"
print(name.lower())   #用方法令字符串全小写
#print(f"{name.lower()}\n") 换行方法
print(name.upper())     #用方法令字符串全大写
print(name.title())     #用方法令字符串每个单词首字母大写


first_name = "albert"
last_name = "einstein"
#用 f 字符串在字符串中插入变量的值
famous_name = f"{first_name} {last_name}"   
message = "a person who never made a mistake never tried anything new"
#使用 f 字符串在字符串中插入变量的值,并且使用方法分别让每个单词首字母大写 和 第一个字符大写其余小写
print(f'{famous_name.title()} once said,"{message.capitalize()}."')  