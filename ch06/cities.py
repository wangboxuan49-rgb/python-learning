#  功能:城市
#  作者:wbx
#  日期:2026-09-21

cities = {              #在字典里面嵌套字典
    'beijing':{
        'country':'china',
        'population':'14.8 billion',
        'fact':'long history'
    },
    'new york':{
        'country':'america',
        'population':'3.42 billion',
        'fact':'bustling'
    },
    'london':{
        'country':'england',
        'population':'0.68 billion',
        'fact':'foggy'
    }
}

for city_name,city_infor in cities.items():     #遍历外层字典的键和值，此处值为字典
    print(city_name.title())
    for intro,infor in city_infor.items():      #遍历内层字典的键和值
        print(f"{intro.title()} is {infor.title()}")
    print()