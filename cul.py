# 通过比较 余数 和 除数的一半 之间的大小，来实现“四舍五入”
from hello import a
from hello import b
x = a // b         # 先运算a整除b
y = a % b          # 运算余数
if (b / 2) > a:    # 比较和输出
    x = y
else:
    x = y + 1
print(y)
