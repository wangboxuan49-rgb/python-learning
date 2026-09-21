#  功能:人们
#  作者:wbx
#  日期:2026-09-21

person_1 = {
    'first_name':'a',
    'last_name':'bc',
    'age':'18',
    'city':'beijing'
}
person_2 = {
    'first_name':'e',
    'last_name':'fg',
    'age':'37',
    'city':'shanghai'
}
person_3 = {
    'first_name':'h',
    'last_name':'ij',
    'age':'69',
    'city':'tianjin'
}

people = [person_1,person_2,person_3]       #将字典嵌套到列表当中

for person in people:       #将列表里的字典赋给临时变量 person
    for infor,per_infor in person.items():      #遍历字典中的键和值
        print(f"{infor.title()} is {per_infor}")
    print()     #在每次外层循环一次时，换行