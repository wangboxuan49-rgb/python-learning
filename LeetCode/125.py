#  功能:验证回文串
#  作者:wbx
#  日期:2026-11-10

#思路：先对原始字符串进行处理，全部转化为小写字符，并且去掉非字母和非数字符号，存为正序字符串，再与反序字符串比较
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 保留原字符串中的字母和数字
        # 或者使用 re.sub(匹配规则, 替换成什么, 要处理的字符串)
        # r 表示原始字符串，让字符串里的反斜杠 \ 通常按原样保留，不会转化为换行等
        # [ ... ]   匹配括号内指定的一类字符
        # a-z       小写英文字母
        # A-Z       大写英文字母
        # 0-9       数字
        # ^         放在方括号开头，表示“不属于”
        order = ''
        for char in s:              #字符串可以直接遍历，每次取出一个字符
            if char.isalnum():      #isalnum() 判断字符是否属于字母或数字，中文字符也会被保留；空格、标点、下划线等会被移除
                order += char

        # 统一转换为小写
        order = order.lower()

        # 得到整理后字符串的逆序
        reverse = order[::-1]       #使用切片得到逆序字符串，[开始位置:结束位置:步长]

        # 比较正序和逆序是否相同
        if order == reverse:        #可以简化为 return order == order[::-1]，判断成功返回 True
            return True
        else:
            return False