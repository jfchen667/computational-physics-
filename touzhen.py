import random
import math
from math import pi

#先生成所需要的量和随机数

d = 3
l = 2
n = 0
x = [random.uniform(0,d/2) for _ in range(500000)]
y = [random.uniform(0,pi/2) for _ in range(500000)]

#判断，注意要用zip一一配对，再做判断，两个列表不能直接去做运算

for xi, yi in zip(x, y):
    if xi/math.cos(yi) < l/2:
        n = n+1
    else:
        n = n

#计算结果

p = n/500000
pai = 2*l/(d*p)
print(pai)