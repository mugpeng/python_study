# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def product(*number):
    if number is None:
        raise TypeError
    else:
        products = 1
        for n in number:
            products = products * n
    return products