#  功能:嘉宾名单
#  作者:wbx
#  日期:2026-09-12

guests = ['Tom','John','Jack']      #创建列表
print(f"我会邀请{guests[0]},{guests[1]},{guests[-1]}来共进晚餐\n")       # 访问列表中的元素

print(f"{guests[1]}无法前来赴约")
guests[1] = 'Leo'       #修改列表中元素
print(f"我会邀请{guests[0]},{guests[1]},{guests[-1]}来共进晚餐\n")       # 访问列表中的元素

guests.insert(0,'Jerry')    #在指定位置插入元素，原元素向右位移一位
guests.insert(2,'Jason')
guests.append('Alex')       #在列表末尾插入元素
print(f"找到了更大的餐桌，我会邀请{guests[0]},{guests[1]},{guests[2]},{guests[3]},{guests[4]},{guests[5]}来共进晚餐\n")

print('抱歉，我现在只能邀请两位嘉宾')
poped_guests = guests.pop(1)    #删除指定位置的元素，但元素还可以继续使用
print(f"抱歉{poped_guests}，无法邀请你共进晚餐了")
poped_guests = guests.pop()    #默认删除列表末尾
print(f"抱歉{poped_guests}，无法邀请你共进晚餐了")
bad_guy = 'Leo'
guests.remove(bad_guy)      #可以删除指定值，元素还可以继续使用，但要提前赋值给变量
print(f"抱歉{bad_guy}，无法邀请你共进晚餐了")
poped_guests = guests.pop()    #默认删除列表末尾
print(f"抱歉{poped_guests}，无法邀请你共进晚餐了")

print(f"我仍然会邀请{guests[0]}")
print(f"我仍然会邀请{guests[-1]}")

del guests[1]   #可以删除指定位置的元素，但是不可以继续使用
del guests[0]
print(guests)