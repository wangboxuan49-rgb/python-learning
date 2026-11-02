#  功能:测试城市和国家
#  作者:wbx
#  日期:2026-10-05

from city_functions import city_country_name    #测试之前需要将要测试的函数导入

def test_city_country():
    """能够正确处理像 Santiago, Chile 这样的字符串吗"""
    full_name = city_country_name('santiago', 'chile')      #向函数传入实参
    assert full_name == 'Santiago, Chile'       #断言正确则测试成功


def test_city_country_populations():        #新增单元测试
    """能够正确处理像 Santiago, Chile -population 500000这样的字符串吗"""
    full_name = city_country_name('santiago', 'chile', 500000)
    assert full_name == 'Santiago, Chile -population 500000'