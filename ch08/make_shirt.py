#  功能:制作T恤
#  作者:wbx
#  日期:2026-09-24

def make_shirt(size,character = "I love Python"):       #给形参指定默认值，没提供实参时，使用形参默认值
    print(f"这是一件{size}码，印着{character}的花纹的 T 恤")

shirt_size = input("请输入 T 恤的尺码：")
shirt_character = input("请输入 T 恤字样：")

make_shirt(shirt_size, shirt_character)     #使用位置实参调用函数，按顺序传值，给出了指定实参，忽略默认值

make_shirt(character = shirt_character, size = shirt_size)      #使用关键值实参来调用函数，使用名值对

make_shirt(shirt_size)      #没提供实参，使用默认值