#  功能:两数之和
#  作者:wbx
#  日期:2026-11-14

# 思路：从外层循环开始，固定一个数，内层循环遍历这个数之后的所有数，比较目标和这两个数之和
# 时间复杂度 O(n^2) ，空间复杂度 O(n)
class Solution(object):
    def twoSum(self, nums : list[int], target : int) -> list[int]:
        # 遍历列表
        for i in range(len(nums)):
            # 计算需要找到的下一个目标数字
            res = target-nums[i]
                # 遍历剩下的元素，查找是否存在该数字
            if res in nums[i+1:]:
                # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
                # .index() 用来查找某个值第一次出现的下标
                # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
                return [i, nums[i+1:].index(res)+i+1]

"""
# 思路：将列表的下标和值同时取出，默认存入字典，利用目标与当前值之差来寻找另一个值
# 时间复杂度 O(n)，空间复杂度 O(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct = {}

        # enumerate(nums) 让你在遍历 nums 时，同时拿到元素的下标和它的值
        for i,num in enumerate(nums):
            val = target - num
            if val in dct.keys():       #在字典的所有键中查找
                return [i,dct[val]]
            else:
                dct[num] = i
"""