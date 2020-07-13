'''
练习1：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。
'''

c = True
a = int(input('Please input an integer.\n'))
if a == 2:
    print(a, '是素数.')
else:
    for b in range(2,a):
        if  a%b == 0:
            c = True
            break
        else:
            c = False
    if c == True:
        print(a, '不是素数.')
    else:
        print(a, '是素数..')