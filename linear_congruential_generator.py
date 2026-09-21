#线性同余法生成随机数，不能控制数量
def LCG(seed = 1,m = 256,a = 137,c = 187):
    array = []
    rnd = seed
    while rnd != 0:
        array.append(rnd/m)
        rnd = (a*rnd + c) % m
    return array
array = LCG()

#可以产生任意维随机数组，数量可控，利用循环嵌套
def LCG_nD(rows,cols,seed=1,m=256,a = 137,c = 187):
    array_nD = []
    rnd = seed
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(rnd/m)
            rnd = (a*rnd + c) % m
        array_nD.append(row)
    return array_nD

result_2 = LCG_nD(rows=200, cols=2)
# for row in result_2:
#     print(row)

result_3 = LCG_nD(rows=200, cols=3)
# for row in result_3:
#     print(row)

#下面画出随机数组的分布图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #解决无法渲染中文的问题
plt.rcParams['axes.unicode_minus'] = False

x = [row[0] for row in result_2]
y = [row[1] for row in result_2]
#画图
plt.figure(figsize=(6, 6))
plt.scatter(x, y, alpha=0.7, color='blue')
#设置坐标轴范围
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.title('LCG 二维散点图 ')
plt.xlabel('(x)')
plt.ylabel('(y)')
# 加点网格线
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#开始画三维的
a = [row[0] for row in result_3]
b = [row[1] for row in result_3]
z = [row[2] for row in result_3]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 添加颜色映射,如果只用一个颜色会有遮挡的情况，颜色变量由z决定
ax.scatter(a,b,z, c=z, cmap='viridis', alpha=0.7, s=20)

# 标签和标题
ax.set_title('LCG 三维随机数组分布散点图')
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('Z')
ax.grid(True, linestyle='--', alpha=0.5)

plt.show()