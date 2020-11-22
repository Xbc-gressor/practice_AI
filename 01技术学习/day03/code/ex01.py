
def diamond(r=5):    # r keyowrd参数
    # r = 5   # float 
    # 循环打印每一行
    for y in range(2 * r + 1):
        for x in range(2 * r + 1):
            #if y <= x:
            #if y == -x + r or y == x -r or y == x + r or y == -x + 3 * r or y == 2 * r or y == 0 or x == 0 or x == 2 * r:
            if y >= -x + r and y >= x -r and y <= x + r and y <= -x + 3 * r:
                print("*", end="") 
            else:
                print(" ", end="")
        print("")
    return   # 没有输出。，则return可以省略

r1 = diamond()
r2 = diamond(r=10)
r3 = diamond(20)
print(r1)