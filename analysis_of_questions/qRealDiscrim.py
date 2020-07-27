
#计算区分度
import json
import math
import numpy as np

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

questionID = []
qRealDiff = []
qRealDiscrim = []
count1 = []
score=[]
pos = 0


#获得所有题号
for key in data:
    cases = data[key]["cases"]
    for case in cases:
        if case["case_id"] not in questionID:
            questionID.append(case["case_id"])
            pos += 1

for i in range(0, pos):
    case_id = questionID[i]
    sum = 0
    count = 0
    qDiff = 0
    for key in data:
        cases = data[key]["cases"]
        for case in cases:
            if case["case_id"] == case_id:
                for upload in case["upload_records"]:
                    sum += upload["score"]
                    count += 1
    qDiff = (sum / count) / 100
    count1.append(count)
    qRealDiff.append(qDiff)

for i in range(0, pos):
    case_id = questionID[i]
    sum = 0
    for key in data:
        cases = data[key]["cases"]
        for case in cases:
            if case["case_id"] == case_id:
                for upload in case["upload_records"]:
                    result = upload["score"] / 100 - qRealDiff[i]
                    sum += result * result
    qDiscrim = math.sqrt(sum / count1[i])
    qRealDiscrim.append(qDiscrim)

dic = {}
for i in range(0, pos):
    dic1 = {"qRealDiff": qRealDiff[i], "qRealDiscrim": qRealDiscrim[i]}
    s = str(questionID[i])
    dic[s] = dic1

print(questionID)
print(qRealDiff)
print(qRealDiscrim)
print(dic)

with open("../qRealDiscrim.json", "w") as f:
    json.dump(dic, f)
    print("加载文件完成")
