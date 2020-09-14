import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus']  = False


df = pd.read_excel("C:/Users/Administrator/Desktop/test.xlsx")
x =df['数据时刻']
y=df['数值']
plt.plot(x,y,label = 'PTP值')

plt.xlabel('时间')
plt.ylabel('PTP')
plt.title('设备的PTP值')
plt.show()

print('sans-serif')