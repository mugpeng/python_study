# -*- coding: utf-8 -*-

# 为返回多个值的练习

# 开根可以用 math 包中的 math.sqrt() 函数
'''
>>> import math
>>> math.sqrt(2)
1.4142135623730951
'''

import math

def quadratic(a, b, c):
    A = math.sqrt(b**2 - 4*a*c)
    x1 = (-b + A)/(2*a)
    x2 = (-b - A)/(2*a)
    return x1, x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')