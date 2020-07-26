
#找到所有以C++代码为答案的题号
import json
import zipfile

f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
questionID = []
cQuestion=[]
pos=0
for key in data:
    cases = data[key]["cases"]
    for case in cases:
        if case["case_id"] not in questionID:
            questionID.append(case["case_id"])
            pos += 1
print(pos)

z = zipfile.ZipFile('answers.zip')
countC=0
for i in range(0, pos):
    path="answers/"+questionID[i]+".py"
    f=z.open(path)
    for line in f:
        line=str(line,encoding='utf-8')
        line = line.strip()
        if line.startswith("#include"):
            cQuestion.append(questionID[i])
            countC+=1
            break
print(countC)
print(cQuestion)

lis=[]
for i in range(0,countC):
    dic={}
    dic["case_id"]=cQuestion[i]
    lis.append(dic)

print(lis)
with open("cAnswer.json", "w") as f:
     json.dump(lis, f)
     print("加载文件完成")
