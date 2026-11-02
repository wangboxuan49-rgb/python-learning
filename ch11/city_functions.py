#  功能:城市和国家
#  作者:wbx
#  日期:2026-10-05

def city_country_name(city_name, country_name, population = ''):
    if population != '':
        full_name = f"{city_name.title()}, {country_name.title()} -population {population}"
    else:
        full_name = f"{city_name.title()}, {country_name.title()}"
    return full_name

"""
在测试时应该只放函数定义，不能有任何模块级的执行语句
city_name = input('请输入一个城市名：')
country_name = input('请输入一个国家名：')
full_name = city_country_name(city_name, country_name)
print(full_name)
"""