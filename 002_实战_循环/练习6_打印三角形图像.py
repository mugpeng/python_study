'''
打印如下所示的三角形图案。
    *
   ***
  *****
 *******
*********
'''

row = int(input(''))

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print() # 完成一次大循环后，换行
    