#  功能:列表切片
#  作者:wbx
#  日期:2026-09-15

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]      #用包含所有元素的切片当做列表的复制

my_foods.append('cannoli')
friend_foods.append('ice cream')

for my_food in my_foods:        #用单数与复数关系表示变量与列表
    print(my_food)

for friend_food in friend_foods:
    print(friend_food)

#[:]从左边索引开始（包含），到右边索引结束（不包含）
print(f"The first three foods is {my_foods[:3]}")       #打印列表前三个元素切片
print(f"The last three foods is {my_foods[-3:]}")       #打印列表倒数三个元素切片

my_foods = ('pizza','falafel','carrot cake','cannoli')      #定义元组用圆括号
print(my_foods)
#my_foods[0] = 'dumpling'       #元组中数据不能修改
#print(my_food)