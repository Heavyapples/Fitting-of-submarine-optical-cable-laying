import numpy as np  # 导入 NumPy 库，用于数组操作
from scipy import interpolate  # 从 SciPy 库中导入 interpolate 方法，用于数据插值
import matplotlib.pyplot as plt  # 导入 Matplotlib 的 pyplot，用于数据可视化
from matplotlib.font_manager import FontProperties  # 从 Matplotlib 中导入 FontProperties，用于设置字体

# 设置字体为黑体，大小为14
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置全局字体为 SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

# 探测点和深度数据
x = np.array([i*100 for i in range(51)])  # 探测点
y = np.array([311.96, 311.10, 315.74, 328.49, 321.14, 333.09, 318.68, 338.88, 325.66, 309.84, 328.62, 321.80, 320.74, 308.30,
              328.45, 312.62, 317.83, 327.40, 323.75, 313.48, 316.66, 340.19, 332.40, 319.20, 334.64, 311.43, 328.92, 314.11,
              319.84, 321.28, 333.84, 319.68, 321.20, 320.89, 325.90, 335.28, 332.00, 324.47, 313.36, 330.60, 322.32, 315.10,
              319.89, 316.75, 321.92, 327.64, 320.40, 329.88, 332.00, 344.35, 348.41])  # 深度

# 使用 scipy 的 interpolate 方法进行线性插值
f = interpolate.interp1d(x, y)

# 使用插值函数 f，生成新的 x 值（xnew）和对应的 y 值
xnew = np.linspace(0, 5000, num=1000, endpoint=True)  # 生成一个从0到5000的等差数列，总共1000个点
# 绘制原始数据点和插值生成的曲线
plt.plot(x, y, 'o', xnew, f(xnew), '-')
plt.title('海底电缆敷设曲线图')  # 图片标题
plt.xlabel('探测点 (m)')  # x轴标签
plt.ylabel('深度 (m)')  # y轴标签
plt.show()  # 显示图形

# 计算光缆长度
# 使用公式 sqrt((x2-x1)**2 + (y2-y1)**2) 计算每两点之间的距离，然后求和得到总长度
length = np.sqrt((x[1:] - x[:-1])**2 + (y[1:] - y[:-1])**2).sum()
print(f"估计海底电缆长度: {length:.1f} 米")  # 打印估计的电缆长度

#使用的算法是线性插值，这是一种数学计算方法，它根据两点之间的线性关系，生成一个通过这两点的直线。对于每对相邻的数据点，线性插值都会生成一个线性函数。线性插值通常用于一维数据的插值
