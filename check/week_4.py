#  功能:第四周验收
#  作者:wbx
#  日期:2026-10-04

from pathlib import Path

def analyze(contents):
    line_num = 0
    noempty_line_num = 0
    word_num = 0
    words_top3 = []
    names = []
    nums = []
    pairs = []

    lines = contents.splitlines()
    line_num = len(lines)
    for line in lines:
        if line.strip() != '':
            noempty_line_num += 1

    words = contents.split()
    word_num = len(words)
    for word in words:
        found = False
        word = word.lower()
        word = word.replace(',','').replace('.','').replace('(','').replace(')','')

        for i in range(len(names)):     #因为要修改 nums。直接把列表交给 for 遍历,拿到的只是值的副本,没有位置信息
            if word == names[i]:
                nums[i] += 1
                found = True
            
        if not found:
            names.append(word)
            nums.append(1)

    for i in range(len(names)):
        pairs.append((-nums[i],names[i]))
    pairs.sort()
    words_top3 = pairs[:3]
    
    contents_info = {
        'line_num' : line_num,
        'noempty_line_num' : noempty_line_num,
        'word_num' : word_num,
        'words_top3' : words_top3
    }

    return contents_info

def write_report(path, stats):
    s = "读文件统计报告\n"
    s += f"总行数: {stats['line_num']}\n"
    s += f"非空行数: {stats['noempty_line_num']}\n"
    s += f"总单词数: {stats['word_num']}\n"
    s += "出现最多的 3 个单词:\n"
    for n, word in stats['words_top3']:     #遍历列表，列表里装着元组，自动把两元素元组拆开赋给这两个名字
        s += f"  {word}: {-n} 次\n"     #排序的时候次数变负，需要还原回来
    path.write_text(s)      #write_text() 只接收字符串，不接受字典


filename = input("请输入文件名")
path = Path(filename)
try:
    contents = path.read_text()
except FileNotFoundError:
    print('文件不存在')
else:
    if contents.strip() == '':
        print('文件为空')
    else:
        stats = analyze(contents)
        write_report(Path('report.txt'),stats)
        print(Path('report.txt').read_text())
