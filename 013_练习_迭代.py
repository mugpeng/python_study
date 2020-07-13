# -*- coding: utf-8 -*-
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if L == []:
        return (None, None) # 列表为空，返回指定元组
    else:
        x = L[0] # 初始化x
        y = L[0] # 初始化y
        for a in L: # 迭代列表L
            if a > x: # 如果比现有的最大值大，则替换之
                x = a
            if a < y: # 如果比现有的最小值小，则替换之
                y = a
        return (y, x) # 返回(min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')