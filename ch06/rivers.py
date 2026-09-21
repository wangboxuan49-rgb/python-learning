#  功能:河流
#  作者:wbx
#  日期:2026-09-21

river_country = {      #创建河流以及流经国家对应字典
    'nile':'egypt',
    'yangtze':'china',
    'ganges':'india'
}

for river, country in river_country.items():        #将键和值均进行遍历，返回一个键值对列表
    print(f"The {river.title()} runs through {country.title()}")

for river in river_country.keys():      #使用 keys（）方法来将键进行遍历，返回一个列表
#for river in river_country:            #也可以直接省略，但是为了程序可读性不要省略
    print(f"The name of river is {river.title()}")

for country in river_country.values():      #使用 values（）方法将值进行遍历，不可以省略，返回一个值列表
    print(f"The country is {country.title()}")
