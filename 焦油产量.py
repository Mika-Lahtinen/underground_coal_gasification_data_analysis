# -*- coding: utf-8 -*-
"""
Created on Fri May  4 23:30:37 2018

@author: Mikka
"""
#引入模型
import matplotlib.pyplot as plt
import numpy
#引入数据
x = [40,60,80,100]#氧浓度
y1 = [4.88,4.2,1.3,2]#贫煤
y2 = [17.68,16.72,11.6,6.5]#烟煤
y3 = [4.48,3,0.85,0.3]#褐煤
#显示中文
plt.rcParams['font.sans-serif']=['SimHei']
#线条绘制
plt.figure()
plt.plot(x,y1,'r',linewidth=1,marker='.',label=u'贫煤')
plt.plot(x,y2,'g',linewidth=1,marker='^',label=u'烟煤')
plt.plot(x,y3,'b',linewidth=1,marker='o',label=u'褐煤')
#添加数据标签
for a,b in zip(x,y1):
    plt.text(a, b+0.3, '%.2f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y2):
    plt.text(a, b+0.1, '%.2f' % b, ha='center', va= 'bottom',fontsize=10)
for a,b in zip(x,y3):
    plt.text(a, b-1, '%.2f' % b, ha='center', va= 'bottom',fontsize=10)
#图像其他标签
plt.xlabel(u'氧浓度 %') #X轴标签  
plt.ylabel(u'焦油产量 g/Nm3')  #Y轴标签  
plt.title(u'不同氧浓度焦油产量') #图标题
plt.legend()  #图例
plt.show()  #显示图  
