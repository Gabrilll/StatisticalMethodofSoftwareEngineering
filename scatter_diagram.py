import matplotlib.pyplot as plt
import json

f = open('matrix.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
diff = []

for case in data:
    value = data[case]
    m1.append(value['M1'])
    m2.append(value['M2'])
    m3.append(value['M3'])
    m4.append(value['M4'])
    m5.append(value['M5'])
    diff.append(value['difficulty_index'])

plt.subplot(2, 3, 1)
plt.scatter(m1, diff, alpha=0.5, c='green', s=2)
plt.title("M1 Scatter")

plt.subplot(2, 3, 2)
plt.scatter(m2, diff, alpha=0.5, c='green', s=2)
plt.title("M2 Scatter")

plt.subplot(2, 3, 3)
plt.scatter(m3, diff, alpha=0.5, c='green', s=2)
plt.title("M3 Scatter")

plt.subplot(2, 3, 4)
plt.scatter(m4, diff, alpha=0.5, c='green', s=2)
plt.title("M4 Scatter")

plt.subplot(2, 3, 5)
plt.scatter(m5, diff, alpha=0.5, c='green', s=2)
plt.title("M5 Scatter")
plt.show()
