def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# 用循环也可以解决
def fact_2(n):
    sum = 1
    while n > 1:
        sum = sum * n
        n = n - 1
    return sum

# 测试

print(fact(1000))