#获得所有c++代码为答案的M2
import json

f = open('../../../averageDepth.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

f1 = open("../../../cAnswer.json", encoding="utf-8")
res1 = f1.read()
data1 = json.loads(res1)

cQuestion = []
pos=0
for key in data1:
    cQuestion.append(key["case_id"])
    pos+=1
print(cQuestion)
lis=[]
dic={}
print(pos)
for i in range(0,pos):
    questionID=cQuestion[i]
    for key in data:
        if key["case_Id"]==int(questionID):
            dic = {"case_Id": int(cQuestion[i]), "Average Block Depth": key["Average Block Depth"]}
            lis.append(dic)
print(lis)

with open('../../../averageDepthOfC.json', "w") as f:
    json.dump(lis,f)
    print("finished")
