
class Geometry:
    # 数据公共部分
    def __init__(self, r=5):  # 构造器
        self.r = r # 输入
    
    # 功能部分
    def diamond(self):    # r keyowrd参数
        # r = 5   # float 
        # 循环打印每一行
        for y in range(2 * self.r + 1):
            for x in range(2 * self.r + 1):
                #if y <= x:
                #if y == -x + r or y == x -r or y == x + r or y == -x + 3 * r or y == 2 * r or y == 0 or x == 0 or x == 2 * r:
                if y >= -x + self.r and y >= x - self.r and y <= x + self.r and y <= -x + 3 * self.r:
                    print("*", end="") 
                else:
                    print(" ", end="")
            print("")
        return   # 没有输出。，则return可以省略

# ---- 怎么使用
g = Geometry(r=10)
g.diamond()
