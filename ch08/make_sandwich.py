#  功能:制作三明治
#  作者:wbx
#  日期:2026-09-25

def make_sandwich(*foods):      #创建一个元组，接受任意数量的实参
    for food in foods:
        print(food)
    print()

make_sandwich('beef')
make_sandwich('fish','beef','pork')
make_sandwich('beef','chicken')