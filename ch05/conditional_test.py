#  功能:条件测试
#  作者:wbx
#  日期:2026-09-17

guests = ['Tom','John','Jack','Leo','Alex']      #创建列表
strangers = []     #创建空列表

if guests[0].lower() == 'tom':      #判断字符串是区分大小写，一般将其降为小写来判断是否相等
    print('True')
if guests[0].lower() != 'alex':     #elif 用于 if 语句判断不成功时，if 执行成功就不执行 elif
    print('False')

if 'John' in guests:        #判断特定元素是否在列表当中
    print('True')
if 'Luke' not in guests:
    print('True')

for guest in guests:        #遍历列表来判断指定元素是否在列表当中
    if guest == 'Leo':
        print(f"Hello {guest},would you like to see a status report?")
    else:
        print(f"Hello {guest},thank you for logging in again.")

if strangers:       #在if语句将列表名用作条件表达式时，在列表包含至少一个元素时返回True，为空时返回False
    for stranger in strangers:      #遍历列表
        print(f"Hello {stranger}!")
    print('Nice to meet you!')      # 不在遍历中，执行完退出循环
else:
    print('We need to find some strangers!')        #列表为空是执行

age = 33
if (age < 18) or (age > 65):        #or 两个条件满足一个就返回 True
    print("半价票")
elif (age >= 18) and (age <= 65):   #and 两个条件要均满足才返回 False，可以用 else，此处为了展示
    print("全价票")