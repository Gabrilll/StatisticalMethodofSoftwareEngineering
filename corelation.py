#计算难度矩阵和实际难度之间的相关性系数
from scipy.stats import pearsonr
import json

pos = 0
questionID = []
realDifficulty=[]
m1=[]
m2=[]
m3=[]
m4=[]
m5=[]

f = open('m1m5.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

for key in data:
    if key not in questionID:
        questionID.append(key)
        m1.append(data[key]["M1"])
        m5.append(data[key]["M5"])
        pos+=1


f1 = open('M2.json', encoding='utf-8')
res1 = f1.read()
data1 = json.loads(res1)
for i in range(0,pos):
    for key in data1:
        if str(key)==str(questionID[i]):
            m2.append(data1[key]["Average Block Depth"])
            break

f3= open('m3m4.json', encoding='utf-8')
res3 = f3.read()
data3 = json.loads(res3)

for i in range(0,pos):
    for key in data3:
        if str(key)==str(questionID[i]):
            m3.append(data3[key]['M3'])
            m4.append(data3[key]['M4'])
            break

f4= open('realDifficultyIndex.json', encoding='utf-8')
res4 = f4.read()
data4 = json.loads(res4)

for i in range(0,pos):
    for key in data4:
        if str(key)==str(questionID[i]):
            realDifficulty.append(data4[key]['qRealDiff'])
            break


print(pearsonr(m1,realDifficulty))
print(pearsonr(m2,realDifficulty))
print(pearsonr(m3,realDifficulty))
print(pearsonr(m4,realDifficulty))
print(pearsonr(m5,realDifficulty))
