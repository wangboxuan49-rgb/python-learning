#  功能:最喜欢的语言
#  作者:wbx
#  日期:2026-09-21

favorite_languages = {      #创建字典
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}

respondents = ['sarah','phil','jack']    #创建列表表示参与调查的人

for name in favorite_languages.keys():      #遍历字典中的键
    print(f"{name.title()}")
    if name in respondents:         #检查字典中的键是否在列表当中
        print(f"{name.title()},thank you!")
    else:
        print(f"{name.title()},could you join?")
    print("")       #print自带一行换行，再加上\n 就是两行空行

for name in sorted(favorite_languages.keys()):      #利用sorted（）函数对键列表按字母顺序进行排序
    print(name)

for languages in set(favorite_languages.values()):      #为剔除重复项，可使用集合，用 set（）来提取
    print(languages.title())