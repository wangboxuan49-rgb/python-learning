#  功能:数值列表
#  作者:wbx
#  日期:2026-09-15

for value1 in range(1,21):   #用 range（）函数生成一系列数，并且给 value 赋值
    print(value1)

numbers = list(range(1,1000001))    #用 list（）函数创建数值列表
#print(numbers)
print(min(numbers))     #打印最大最小值，总和
print(max(numbers))
print(sum(numbers))

evens = list(range(1,21,2))     #range（）函数步长为 2，可以打印出所有奇数
for value2 in evens:        #利用for循环打印出数值列表
    print(value2)

cubes = []      #创建空列表
for value3 in range(1,11):
    cube = value3 ** 3      #创建临时变量，用一系列数的立方给变量赋值
    cubes.append(cube)      #在空列表后追加临时变量的值
for value4 in cubes:    #用for循环打印列表
    print(value4)

#用列表推导式创建列表，表达式value ** 3 是要储存到列表的值，for循环用于给表达式赋值
cubes1 = [value ** 3 for value in range(1,11)]      
print(cubes1)