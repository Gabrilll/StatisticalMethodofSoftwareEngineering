# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:50:25 2020

@author: Ray
"""
path = '../test_data.json'
import numpy as np
import matplotlib.pyplot as plt
# 计算每一套试卷的平均难度
import json
import random
from io import BytesIO
import base64
import os

module_path = os.path.dirname(__file__)

f = open(module_path+"/../test_data.json", encoding='utf-8')
res = f.read()
data = json.loads(res)
questionID = []
types = []
pos = 0
for key in data:
    cases = data[key]["cases"]
    for case in cases:
        if case["case_id"] not in questionID:
            questionID.append(case["case_id"])
            types.append(case["case_type"])
            pos += 1

count = 100
lis = random.sample(questionID, count)

f1 = open(module_path+'/../qRealDiscrim.json', encoding='utf-8')
res1 = f1.read()
data1 = json.loads(res1)

difficulty = 0
discrim = 0
for i in range(0, count):
    for key in data1:
        if key == lis[i]:
            difficulty += data1[key]["qRealDiff"]
            discrim += data1[key]["qRealDiscrim"]

averageDifficulty = 1 - difficulty / count
averageDiscrim = discrim / count

print(averageDifficulty)
print(averageDiscrim)

# 构造数据
feature = list(set(types))
values = [0, 0, 0, 0, 0, 0, 0, 0]
for id in lis:
    isS = False
    for key in data:
        cases = data[key]["cases"]
        for case in cases:
            if case["case_id"] == id:
                for i in range(len(feature)):
                    if (case["case_type"] == feature[i]):
                        values[i] += 1
                        isS = True
                        break
            if (isS):
                break
        if (isS):
            break
print(values)
# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

# 使用ggplot的绘图风格
# plt.style.use('ggplot')

N = len(values)
# 设置雷达图的角度，用于平分切开一个圆面
angles = np.linspace(0, 2 * np.pi, N, endpoint=False)

# 为了使雷达图一圈封闭起来，需要下面的步骤
values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

# 绘图
fig = plt.figure()
# 这里一定要设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values,'o-',linewidth=2)
# 填充颜色
ax.fill(angles, values,'g', alpha=0.25)
# 添加每个特征的标签
ax.set_thetagrids(angles * 180 / np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0, 40)
# 添加标题
plt.title('题目分布图')
# 添加网格线
ax.grid(True)
sio = BytesIO()
plt.savefig(sio, format='png', transparent=True)
img = base64.b64encode(sio.getvalue()).decode()
# 显示图形
plt.show()


def value():
    return "data:image/png;base64,"+img
