#计算预估难度和实际难度之间的相关性
from scipy.stats import pearsonr
import json

f = open('predict.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

pos = 0
questionID = []
pre=[]
for key in data:
    if key not in questionID:
        questionID.append(key)
        pre.append(data[key])
        pos+=1
print(pre)
f4 = open('realDifficultyIndex.json', encoding='utf-8')
res4 = f4.read()
data4 = json.loads(res4)
realDifficulty=[]
for i in range(0,pos):
        for key in data4:
            if int(key) == int(questionID[i]):
                realDifficulty.append(data4[key]['qRealDiff'])
                break
print(realDifficulty)

print(pearsonr(pre,realDifficulty))