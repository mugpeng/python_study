# 练习3：输入三条边长，如果能构成三角形就计算周长和面积。
'''
海伦公式： 
三角形三边，a，b，c
周长为p，计算面积area
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
'''

a = int(input("1st length is: \n"))
b = int(input("2ed length is: \n"))
c = int(input("3rd length is: \n"))

if a + b > c or a + c > b or b + c > a:
    Per = a + b + c
    p = (a + b + c) / 2
    area = (p *(p - a) * (p - b) * (p - c)) ** 0.5
    print('The perimeter is %d, the area is %d.' % (Per, area))
else:
    print("Sorry, it's not an legal triangle.")