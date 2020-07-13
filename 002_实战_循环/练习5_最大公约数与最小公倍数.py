'''
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
最小公倍数可以计算为两个数的乘积除上两个数的最大公因数
'''

a = int(input('input an integer.\n'))
b = int(input('input an integer.\n'))

if a > b:
    a, b =b, a
for n in range(a, 0, -1):
    if a%n == 0 and b%n == 0:
        print("the greatest common divisor of %d and %d is %d." % (a, b, n))
        print('the smallest common multiple of %d and %d is %d.'% (a, b, a*b//n)) 
    break

