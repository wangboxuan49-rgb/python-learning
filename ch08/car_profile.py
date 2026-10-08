#  功能:汽车信息
#  作者:wbx
#  日期:2026-09-25

def make_car(manufacturer, model, **car_info):  #创建一个字典，将已有的键值对存进去
    car_info['manufacturer'] = manufacturer     #在字典最后追加键值对
    car_info['model'] = model
    return car_info     #返回一个字典

car_profile = make_car('subaru','outback',color = 'blue',tow_package=True)  #赋值给字典

print(car_profile)