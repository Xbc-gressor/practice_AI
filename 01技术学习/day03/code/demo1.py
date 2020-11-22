# 定义半径
r = input("输入菱形半径：")   # 输入的是字符串，需要转换为整数
r = int(r)    # float 

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


