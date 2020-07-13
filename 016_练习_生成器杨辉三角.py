def triangles():
    old = [1]
    while True:
        yield old
        new = [1, 1]
        for i in range(0, len(old)):
            if i == len(old) - 1:
                break            
            new.insert(i + 1, old[i] + old[i + 1])
        old = new
n = 0

# 验证
for a in triangles():
    print(a)
    n += 1
    if n > 10:
        break