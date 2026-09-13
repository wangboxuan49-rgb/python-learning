#  功能:第一周验收
#  作者:wbx
#  日期:2026-09-13

numbers = [4,6,1,9,7]   #创建列表,列表中是数字
num_list = ['4','6','1','9','7']    #列表中是字符串

print(numbers)      #打印列表
print(num_list)
print(f"两数字元素相加{numbers[0]}+{numbers[1]}={numbers[0] + numbers[1]}")
print(f"两字符串元素相加'{num_list[0]}'+'{num_list[1]}'={num_list[0] + num_list[1]}")

numbers.append('0')     #列表末尾追加一个新数字
print(numbers)