#  功能:制作专辑
#  作者:wbx
#  日期:2026-09-24

albums = {}

def make_album(singer, album, song_count:None):     #可选形参song_count 默认为None（表示为变量没有值）
    albums = {'singer':singer,'album':album}

    if song_count:      #如果非空，新增键值对
        albums['song_count'] = song_count
    
    return albums       #函数里的 albums 并非全局变量，不能赋值给函数外的 albums，需要用返回值

while True:     #无限循环
    print("输入 q 随时退出")

    singer_name = input('请输入一个歌手名：')
    if singer_name == 'q':
        break

    album_name = input('请输入一个专辑名：')
    if album_name == 'q':
        break

    count = input("歌曲数（直接回车可跳过）：")
    if count == 'q':
        break

    if count:       #如果用户输入非空
        song_count = int(count)     #则将字符串转换为整数类型
    else:
        song_count = None

    albums = make_album(singer_name, album_name, song_count)    #返回值给字典赋值
    
    for k, v in albums.items():   # 加 .items()，一次拿到键和值
        print(f"{k} 是 {v}")