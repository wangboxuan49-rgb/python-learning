#  功能:读文件并处理
#  作者:wbx
#  日期:2026-10-03

from pathlib import Path

def analyze(text):
    line_num = 0
    noempty_line_num = 0
    word_num = 0
    words_top3 = []

    lines = text.splitlines()       #按行切成列表，自动处理各种换行符，末尾换行不会多出空元素
    line_num = len(lines)
    for line in lines:
        if line.strip():      #这一行有内容，strip() 返回的字符串非空，为真值
            noempty_line_num += 1

    words = text.split()        #不带参数按任意空白切分，得到一个单词列表；这是算总单词数和词频的主力
    word_num = len(words)       #统计列表元素个数

    #元素个数计数：先准备两个空容器，循环里对每个元素做"有就加一，没有就新增一行"
    names = []
    nums = []
    for word in words:  #每遇到一个词，就到 names 里挨个找有没有，找到就把对应位置的计数加一，找不到就新开一条记 1 次
        found = False
        word = word.lower()     #替换为小写，并处理标点符号
        word = word.replace('.', '').replace(',', '').replace('(', '').replace(')', '')
        for i in range(len(names)):
            if names[i] == word:
                nums[i] += 1
                found = True
        if not found:
            names.append(word)
            nums.append(1)

    pairs = []
    for i in range(len(names)):
        pairs.append((-nums[i], names[i]))  #把第 i 行的"次数取负"和"单词"装进一个元组，从此它俩同进同出
    pairs.sort()    #先比第一个元素（-次数，小的在前 = 次数大的在前），第一个相等再比第二个（单词，字母序升序）
    words_top3 = pairs[:3]

    text_info = {
        'line_num' : line_num,
        'noempty_line_num' : noempty_line_num,
        'word_num' : word_num,
        'words_top3' : words_top3
    }

    return text_info

def write_report(path, stats):
    s = "读文件统计报告\n"
    s += f"总行数: {stats['line_num']}\n"
    s += f"非空行数: {stats['noempty_line_num']}\n"
    s += f"总单词数: {stats['word_num']}\n"
    s += "出现最多的 3 个单词:\n"
    for n, word in stats['words_top3']:     #遍历列表，列表里装着元组，自动把两元素元组拆开赋给这两个名字
        s += f"  {word}: {-n} 次\n"     #排序的时候次数变负，需要还原回来
    path.write_text(s)      #write_text() 只接收字符串，不接受字典

     
filename = input('请输入文件名称：')
path = Path(filename)
try:
    text = path.read_text()
except FileNotFoundError:
    print('文件未找到')
else:
    if not text.strip():
        print('文件是空的，没有内容可统计')
    else:
        stats = analyze(text)
        write_report(Path('report.txt'), stats)     #写入新文件，否则原文会被覆盖
        print(Path('report.txt').read_text())