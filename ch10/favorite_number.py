#  功能:喜欢的数
#  作者:wbx
#  日期:2026-10-02

from pathlib import Path
import json

def storage_number(favorite_number, path):
    """将传入的字符串存储进 json 文件当中"""
    contents = json.dumps(favorite_number)  #传递一个 json 格式的字符串
    path.write_text(contents)       #把字符串写入文件当中

def show_number(favorite_number, path):
    """如果存储了用户喜欢的数，就显示它，否则提示用户输入喜欢的数并存储"""
    if path.exists():               #指定文件存在返回 True，不存在返回 False
        contents = path.read_text()     #将文件中的内容返回一个字符串
        stored_number = json.loads(contents)    #把 json 格式的字符串还原成 python 对象
        if favorite_number == stored_number:
            print(f"I know your favrite number! It's {stored_number}")
        else:
            storage_number(favorite_number, path)
    else:
        print("File not found! Now create a new file.")
        storage_number(favorite_number, path)       #如果文件不存在，则用write_text创建一个新文件


favorite_number = input("请输入你最喜欢的数：")        
path = Path('favorite_number.json')     #实例化 Path 对象，并赋值给 path
show_number(favorite_number, path)