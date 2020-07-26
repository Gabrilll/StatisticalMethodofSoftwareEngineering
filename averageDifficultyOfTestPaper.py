#计算每一套试卷的平均难度

import json
import random

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
questionID = []
pos = 0

for key in data:
    cases = data[key]["cases"]
    for case in cases:
        if case["case_id"] not in questionID:
            questionID.append(case["case_id"])
            pos += 1

count=100
lis=random.sample(questionID,count)
print(lis)

f1 = open('qRealDiscrim.json', encoding='utf-8')
res1 = f1.read()
data1 = json.loads(res1)

difficulty=0
discrim=0
for i in range(0,count):
    for key in data1:
        if key==lis[i]:
            difficulty+=data1[key]["qRealDiff"]
            discrim+=data1[key]["qRealDiscrim"]

averageDifficulty=1-difficulty/count
averageDiscrim=discrim/count

print(averageDifficulty)
print(averageDiscrim)

