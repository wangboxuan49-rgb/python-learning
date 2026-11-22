#  功能:字符串中的第一个唯一字符
#  作者:wbx
#  日期:2026-11-22

# 思路：取出字符串的下标与字符，查找每一个字符在字符串中出现的次数，返回第一个出现次数一次的字符的下标
# 时间复杂度 O(n^2) ，空间复杂度 O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index,char in enumerate(s):
            if s.count(char) == 1:
                return index

        return -1

"""
# 思路：首先遍历 26 个字母，用列表记录下来每一个只出现在字符串中一次的字符
# 然后再取出字符串的下标和字符，如果字符出现在列表当中，说明是唯一字符，返回对应下标
# 时间复杂度 O(n) ，空间复杂度 O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        val = []

        for ch in ascii_lowercase:
            if s.count(ch) == 1:
                val.append(ch)

        for index,char in enumerate(s):
            if char in val:
                return index

        return -1
"""

"""
# 思路：使用哈希表，先遍历字符串，如果字符不在字典里面，添加字符并且值设为 True（意为当前为唯一字符）
# 如果字符在字典里面，把该字符的值设为 False（不再是唯一字符），最后再遍历一次字符串，查找第一个值为 True 的字符
# 时间复杂度 O(n) ，空间复杂度 O(1)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}

        for ch in s:
            dic[ch] = not ch in dic
        for index,char in enumerate(s):
            if dic[char]:
                return index
        return -1
"""