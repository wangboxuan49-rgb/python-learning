#  功能:可变对象练习
#  作者:wbx
#  日期:2026-11-11

list_source = ['a','b','c','d']     #列表和字典都属于可变对象，创建之后可以直接原地修改其内容，字符串是不可变对象

list_target = list_source           #此时两个变量名指向了同一个变量
list_target[0] = 'A'                #此时修改目标列表，源列表也会发生改变

print(f"list_target:{list_target}")
print(f"list_source:{list_source}")

list_source = ['a','b','c','d'] 

list_copied = list_source.copy()    #使用 copy 在源列表副本上修改，可以避免修改源列表
list_copied[0] = 'A'

print(f"list_copied:{list_copied}")
print(f"list_source:{list_source}")