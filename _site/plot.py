# -*- coding: UTF-8 -*-
"""
@Project ：rl-lab 
@File    ：plot.py
@Author  ：Yifu Yuan
@Date    ：2023/9/28
"""
import matplotlib.pyplot as plt
x = ['naive', '+example', '+filter']
y = [88, 92, 98]
plt.figure(figsize=(4, 3))
plt.plot(x, y, marker='o')
plt.ylabel('Annotation Accuracy (%)')
plt.savefig("test.pdf")
plt.show()


# import matplotlib.pyplot as plt
#
# # 横坐标
# x = ['naive', '+ example\nannotations', '+filter']
#
# # 纵坐标，以百分比形式表示
# y = [88, 92, 98]
#
# plt.figure(figsize=(8, 6))
#
# # 画柱状图
# bars = plt.bar(x, y)
#
# # 添加标题和坐标轴标签
# # plt.title('Accuracy Plot')
# plt.ylabel('Annotation Accuracy (%)')
#
# # 显示图形
# plt.show()