#  功能:两个数组的交集 II
#  作者:wbx
#  日期:2026-11-24

# 思路：先遍历其中一个数组列表，用字典对各个数字出现次数进行计数，再遍历另外另外一个列表，相似元素存进新列表，同时计数减一
# 时间复杂度 O(n) ，空间复杂度 O(n)
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dic = {}
        res = []
        for num1 in nums1:
            if not num1 in dic:
                dic[num1] = 1
            else:
                dic[num1] += 1
        for num2 in nums2:
            if num2 in dic and dic[num2] != 0:
                res.append(num2)
                dic[num2] -= 1
        return res