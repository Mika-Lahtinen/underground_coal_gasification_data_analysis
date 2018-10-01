# -*- coding: utf-8 -*-
"""
Created on Fri May 11 22:48:35 2018

@author: Mikka
"""

# 导入绘图模块
import matplotlib.pyplot as plt
import numpy as np
# 构建数据
fenlei = [13.76,0.59,0,0]
danhuan = [10.24,3.56,6.25,4.44]
duohuan = [25.37,45.62,38.38,51.17]
zhifang = [33.95,2.6,4.21,3.05]
saifen = [17.63,43.93,37.61,33.6]
yang = ['40','60','80','100']
bar_width = 0.15

# 中文乱码的处理
plt.rcParams['font.sans-serif']=['SimHei']

# 绘图
plt.bar(np.arange(4), fenlei, label = '酚', color = 'steelblue', alpha = 0.8, width = bar_width)
plt.bar(np.arange(4)+bar_width, danhuan, label = '单环芳烃', color = 'y', hatch='///', alpha = 0.8, width = bar_width)
plt.bar(np.arange(4)+bar_width*2, duohuan, label = '多环芳烃', color = 'pink',  hatch='+++',alpha = 0.8, width = bar_width)
plt.bar(np.arange(4)+bar_width*3, zhifang, label = '脂肪烃', color = 'coral',  hatch='\/\/\/',alpha = 0.8, width = bar_width)
plt.bar(np.arange(4)+bar_width*4, saifen, label = '噻吩', color = 'wheat', hatch='---',alpha = 0.8, width = bar_width)
# 添加轴标签
plt.xlabel('氧浓度 %')
plt.ylabel('比例 %')
# 添加标题
plt.title('不同氧浓度下王斜煤气化焦油组分比例')
# 添加刻度标签
plt.xticks(np.arange(4)+bar_width*2,yang)
#调整y轴的范围
plt.ylim([0,80])
# 为每个条形图添加数值标签
for yang,fen in enumerate(fenlei):
    plt.text(yang-0.15, fen+1, '%s' %fen)

for yang,danh in enumerate(danhuan):
    plt.text(yang, danh+1, '%s' %danh)
    
for yang,duoh in enumerate(duohuan):
    plt.text(yang+0.15, duoh+1, '%s' %duoh)
    
for yang,zhif in enumerate(zhifang):
    plt.text(yang+0.35, zhif+1, '%s' %zhif)

for yang,saif in enumerate(saifen):
    plt.text(yang+0.5, saif+1, '%s' %saif)
# 显示图例
plt.legend()
# 显示图形
plt.show()
