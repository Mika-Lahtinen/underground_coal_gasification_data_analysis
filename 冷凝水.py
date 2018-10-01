# -*- coding: utf-8 -*-
"""
Created on Sun May 13 00:07:17 2018

@author: Mikka
"""

import matplotlib.pyplot as plt
import numpy
#引入数据
x = [40,60,80,100]#氧浓度
y1 = [7740,3660,11100,3760]#COD
y2 = [1.78,2.62,1.01,0.005]#硫化物
y3 = [691,2170,2090,1030]#氨氮
#显示中文
plt.rcParams['font.sans-serif']=['SimHei']
#线条绘制
plt.figure()
plt.plot(x,y1,'r',linewidth=1,marker='*',label=u'COD')
plt.plot(x,y2,'g',linewidth=1,marker='^',label=u'硫化物')
plt.plot(x,y3,'b',linewidth=1,marker='d',label=u'氨氮')
#添加数据标签
for a,b in zip(x,y1):
    plt.text(a, b+0.3, '%.2f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y2):
    plt.text(a, b+0.1, '%.2f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y3):
    plt.text(a, b-1, '%.2f' % b, ha='center', va= 'bottom',fontsize=10)
#图像其他标签
plt.xlabel(u'氧浓度 %') #X轴标签  
plt.ylabel(u'物质含量 mg/l')  #Y轴标签  
plt.title(u'不同氧浓度冷凝水相关物质产量') #图标题
plt.legend()  #图例
plt.show()  #显示图  
