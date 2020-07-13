# -*- coding: utf-8 -*-
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：

def trim(s):
    if s == '':
        return s
    while s[0] == ' ': # 若首个字符为' ' ->
        s = s[1:] # 则s去除首个元素（从第二个到最后一个）
        if s == '':
            return s
    while s[-1] == ' ': # 若最后一个字符为' ' ->
        s = s[:-1] # 则s去除最后一个元素（从第一个到倒数第二个）
        if s == '':
            return s
    return s