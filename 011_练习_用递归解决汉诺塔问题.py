# -*- coding: utf-8 -*-

# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
# 然后打印出把所有盘子从A借助B移动到C的方法。
count = 0

def move(n, a, b, c):
    global count
    if n == 0:
        print('0')
    elif n == 1:
        print(a, '-->', c) 
        count += 1
    else:
        move(n-1, a, c, b) # 第一步
        print(a, '-->', c) # 第二步
        count += 1
        move(n-1, b, a, c) # 第三步
    return count

move(6, 'a', 'b', 'c')
print(count)