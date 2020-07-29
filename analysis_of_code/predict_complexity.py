# 预测代码复杂度
import matplotlib.pyplot as plt
import json

f = open('matrix/matrix.json')
data = json.loads(f.read())

m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
for case in data:
    m1.append(data[case]['M1'])
    m2.append(data[case]['M2'])
    m3.append(data[case]['M3'])
    m4.append(data[case]['M4'])
    m5.append(data[case]['M5'])

m1_max = max(m1)
m1_min = min(m1)
m2_max = max(m2)
m2_min = min(m2)
m3_max = max(m3)
m3_min = min(m3)
m4_max = max(m4)
m4_min = min(m4)
m5_max = max(m5)
m5_min = min(m5)

x = []
y = []
res = {}
for case in data:
    t1 = (data[case]["M1"] - m1_min) / (m1_max - m1_min)
    t2 = (data[case]["M2"] - m2_min) / (m2_max - m2_min)
    t3 = (data[case]["M3"] - m3_min) / (m3_max - m3_min)
    t4 = (data[case]["M4"] - m4_min) / (m4_max - m4_min)
    t5 = (data[case]["M5"] - m5_min) / (m5_max - m5_min)

    x.append(t1 + t2 + t3 + t4 + t5)
    y.append(data[case]['difficulty_index'])
    res[case] = {}
    res[case]['predict_complexity'] = t1 + t2 + t3 + t4 + t5

plt.scatter(x, y, c='green', s=2)
plt.title("predict_complexity")
plt.show()

json_str = json.dumps(res)
with open('complexity.json', 'w') as json_file:
    json_file.write(json_str)

print(len(res))
