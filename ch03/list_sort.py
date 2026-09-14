#  功能:排序列表元素
#  作者:wbx
#  日期:2026-09-14

locations = ['china','america','russia','england','japan']   #创建列表
print(locations)

print(sorted(locations))    #使用 sorted（）函数来对列表进行临时排序（按字母顺序）
print(locations)    #核实列表并未产生变化

print(sorted(locations,reverse=True))   #传递参数 reverse=True 来临时反向排序，加在列表后面
print(locations)    #核实列表并未产生变化

locations.reverse()     #使用reverse（）方法永久反向排序（按列表元素顺序）
print(locations)    #核实列表产生变化

locations.reverse()     #再使用reverse（）方法，变回原排序顺序
print(locations)    #核实列表产生变化

locations.sort()     #使用sort（）方法永久排序（按字母顺序）
print(locations)    #核实列表产生变化

locations.sort(reverse=True)     #再使用sort（）方法永久反向排序
print(locations)    #核实列表产生变化

print(len(locations))      #len（）函数获取列表长度