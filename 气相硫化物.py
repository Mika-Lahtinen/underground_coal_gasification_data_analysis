# -*- coding: utf-8 -*-
"""
Created on Sat May  5 10:28:08 2018

@author: Mikka
"""

import numpy as np
import matplotlib.pyplot as plt
#显示中文
plt.rcParams['font.sans-serif']=['SimHei']

x = ['40','60','80','100']
ash = 0.2

#二氧化硫数据
y1 = [6.0279865,8.2763755,30.18181,6.330302]
#硫化氢数据
y2 = [642.13525,645.86886,158.34547,1003.0515]
#构造条形图
plt.bar(np.arange(4),y1,width = 0.2,align='center',color = 'r',label = u'二氧化硫',hatch = '++',alpha=0.8)
plt.bar(np.arange(4)+ash,y2,width = 0.2,align='center',hatch = '//',label = u'硫化氢',color = 'y',alpha=0.8)
#刻度标签
plt.xticks(np.arange(4)+0.1,x)
#y轴范围
plt.ylim([0,1100])
#数据标签
for a,b in enumerate(y1):
    plt.text(a-0.1, b+10, '%.2f' % b)

for a,b in enumerate(y2):
    plt.text(a+0.05, b+10, '%.2f' % b)
#其他标签
plt.xlabel(u'氧浓度 %') #X轴标签  
plt.ylabel(u'硫化物含量 mg/Nm3')  #Y轴标签  
plt.title(u'不同氧浓度气相硫化物含量') #图标题
plt.legend()
plt.show()
