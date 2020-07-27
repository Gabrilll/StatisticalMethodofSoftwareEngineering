import matplotlib.pyplot as plt
import json
import numpy as np

f=open('../analysis_of_code/matrix/matrix.json')
data = json.loads(f.read())

m1 = []
m2=[]
m3=[]
m4=[]
m5 = []
for case in data:
    m1.append(data[case]['M1'])
    m2.append(data[case]['M2'])
    m3.append(data[case]['M3'])
    m4.append(data[case]['M4'])
    m5.append(data[case]['M5'])

m1_m = np.mean(m1)
m1_d= np.std(m1)
m2_m= np.mean(m2)
m2_d = np.std(m2)
m3_m = np.mean(m3)
m3_d = np.std(m3)
m4_m = np.mean(m4)
m4_d = np.std(m4)
m5_m = np.mean(m5)
m5_d = np.std(m5)

x = []
y = []
res = {}
for case in data:
    t1 = (data[case]["M1"] - m1_m) / m1_d
    t2 = (data[case]["M2"] - m2_m) / m2_d
    t3 = (data[case]["M3"] - m3_m) / m3_d
    t4 = (data[case]["M4"] - m4_m) / m4_d
    t5 = (data[case]["M5"] - m5_m) / m5_d

    x.append(t1 + t2 + t3 + t4 + t5)
    y.append(data[case]['difficulty_index'])
    res[case]={}
    res[case]['predict_complexity'] = t1 + t2 + t3 + t4 + t5

plt.scatter(x, y, c='green', s=2)
plt.title("predict_complexity")
plt.show()

json_str = json.dumps(res)
with open('trial_complexity.json', 'w') as json_file:
    json_file.write(json_str)

print(len(res))