#以70分以下的人数占总人数的比例作为题目难度系数

import json
import math

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
questionID = []
realDiffIndex = []
pos = 0

for key in data:
    cases = data[key]["cases"]
    for case in cases:
        if case["case_id"] not in questionID:
            questionID.append(case["case_id"])
            pos += 1
print(pos)

for i in range(0, pos):
    countLessThan70 = 0
    count = 0
    case_id = questionID[i]
    for key in data:
        cases = data[key]["cases"]
        for case in cases:
            if case["case_id"] == case_id:

                for upload in case["upload_records"]:
                    count += 1
                    if upload["score"] <70:
                        countLessThan70 += 1
                """count+=1
                if case["final_score"]!=100:
                    countLessThan70+=1"""
    realDiff =int( round((countLessThan70 / count)*100,0))
    realDiffIndex.append(realDiff)

print(realDiffIndex)
dic = {}
for i in range(0, pos):
    dic1 = {"qRealDiff": realDiffIndex[i]}
    s = str(questionID[i])
    dic[s] = dic1

with open("realDifficultyIndex.json", "w") as f:
    json.dump(dic,f)
    print("finished")