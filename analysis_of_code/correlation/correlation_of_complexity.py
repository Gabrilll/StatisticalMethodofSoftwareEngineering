# 计算预测代码复杂度和难度指数之间的相关系数
from scipy.stats import pearsonr
import json

f = open('../complexity.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
f2 = open('../matrix/matrix.json', encoding='utf_8')
res2 = f2.read()
data2 = json.loads(res2)
x = []
y = []
for case in data2:
    x.append(data[case]['predict_complexity'])
    y.append(data2[case]['difficulty_index'])
print(pearsonr(x, y))
