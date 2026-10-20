#  功能:猫和狗
#  作者:wbx
#  日期:2026-10-02

from pathlib import Path

try:
    contents1 = Path('cats.txt').read_text()        #首先要实例化 Path 对象，变成一个实例，再对实例调用方法
    contents2 = Path('dogs.txt').read_text()        #contents1 是文本内容，不是 Path 实例
except FileNotFoundError:
    #print('文件不存在与该地址')
    pass        #可以使出现异常时保持静默
else:
    cats = contents1.split()
    dogs = contents2.split()
    for cat in cats:
        print(cat)
    print()
    for dog in dogs:
        print(dog)