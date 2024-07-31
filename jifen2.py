import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import time
# 设置matplotlib支持中文的字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 'SimHei' 是黑体的意思
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
# 复合辛普森公式
def Compound_Simpson(x,h,f):
    result = 0.0
    n = len(x) - 1
    for k in range(n):
        result += f(x[k]) + 4*f(x[k] + h/2) + f(x[k+1])
    result *= h/6
    return result
# 定义被积函数
def f(x):
    return 1 / (1 + x**2)
# 定义误差函数
def error(approximation, exact):
    return np.abs(approximation - exact)
# 调用复合辛普森公式
x_values = np.linspace(-1, 1, 1001)  # 从-1到1，包括端点，共1001个点
h = x_values[1] - x_values[0]
simpson_result = Compound_Simpson(x_values, h, f)
print("辛普森法结果:", simpson_result)
simpson_error = error(simpson_result, 0.5*np.pi)
print("辛普森法误差:", simpson_error)

# 定义理论积分值
exact_integral = 0.5 * np.pi


# 计算不同 n 下的误差
n_values = np.logspace(1, 4, 10, base=10)  # 选择 n 的值，从10到10000
simpson_errors = []

for n in n_values:
    x_values = np.linspace(-1, 1, int(n))  # 从-1到1，包括端点，共 n 个点
    h = x_values[1] - x_values[0]
    
    simpson_result = Compound_Simpson(x_values, h, f)
    simpson_error = error(simpson_result, exact_integral)
    simpson_errors.append(simpson_error)
    
# 绘制 n 与积分误差的关系图
plt.figure(figsize=(10, 6))
plt.plot(n_values, simpson_errors, label='辛普森法误差', marker='s', linestyle='-')
plt.xscale('log')  # 对 x 轴进行对数变换
plt.yscale('log')  # 对 y 轴进行对数变换
plt.xlabel('n (区间划分数)', fontsize=12)  # 增加字体大小
plt.ylabel('误差', fontsize=12)  # 增加字体大小
plt.title('n 与积分误差的关系', fontsize=14)  # 增加字体大小

# 绘制图例
legend = plt.legend(prop={'size': 12})

# 显示图表
plt.grid(True)
plt.show()

# 定义区间划分数
n_values = [10, 100, 1000,10000]
times_trapezoid = []
times_simpson = []
# 测量算法执行时间
def measure_time(func, x, h, f):
    start_time = time.time()
    result = func(x, h, f)
    end_time = time.time()
    return result, end_time - start_time
for n in n_values:
    x_values = np.linspace(-1, 1, int(n))  # 从-1到1，包括端点，共 n 个点
    h = x_values[1] - x_values[0]

    simpson_result, simpson_time = measure_time(Compound_Simpson, x_values, h, f)
    times_simpson.append(simpson_time)

for n, simpson_time in zip(n_values,times_simpson):
    print(f"当 n = {n} 时:")
    print(f"辛普森法所需时间: {simpson_time:.6f} 秒")
# 绘图比较速度
plt.figure(figsize=(10, 6))
plt.plot(n_values, times_simpson, label='辛普森法时间', marker='s')
plt.xscale('log')  # 对 x 轴进行对数变换
plt.xlabel('n (区间划分数)')
plt.ylabel('时间 (秒)')
plt.title('算法速度比较')
plt.legend()
plt.grid(True)
plt.show()