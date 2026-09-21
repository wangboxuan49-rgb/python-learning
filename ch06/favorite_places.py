#  功能:喜欢的地方
#  作者:wbx
#  日期:2026-09-21

favorite_places = {         #在字典中嵌套列表
    'jack':['beijing','shanghai','shenzhen'],
    'tom':['tianjin','chengdu'],
    'ethan':['changsha','wuhan','beijing']
}

for name,places in favorite_places.items():     #将字典的键与值遍历，这里字典的值是列表
    print(name.title())     #打印键
    for place in places:        #打印值，遍历列表
        print(place.title())
    print()