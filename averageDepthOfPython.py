#计算所有以python代码为答案的M2
import json
import os
import zipfile

f = open('averageDepth.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
f1 = open("cAnswer.json", encoding="utf-8")
res1 = f1.read()
data1 = json.loads(res1)

cQuestion = []
for key in data1:
    cQuestion.append(int(key["case_id"]))

pos = 0
pythonQuestion = []
depth = []
for key in data:
    if key["case_Id"] not in cQuestion:
        pythonQuestion.append(key["case_Id"])
        pos += 1


#path = "C:\\Users\\asus\\Desktop\\nestedBlock1"
z = zipfile.ZipFile('answers.zip')
for i in range(0, pos):
    #print(pythonQuestion[i])
    # filename = str(pythonQuestion[i]) + ".py"
    # path1 = os.path.join(path, filename)
    path1 = "answers/" +str(pythonQuestion[i] )+ ".py"
    f = z.open(path1)
    tempDepth=0
    count=0
    tempDepth1=[]
    for line in f:
        line = str(line, encoding='utf-8')
        line=line.replace('\t','    ')
        temp = 0
        line1=line.strip()
        if len(line1)==0 or line1.startswith('#'):
            continue
        for i in line:
            if i.isspace():
                temp+=1
            else:
                count+=1
                break
        tempDepth1.append(temp)
    length=len(tempDepth1)
    for i in range(0,length-1):
        if tempDepth1[i]>tempDepth1[i+1]:
            tempDepth+=tempDepth1[i]
    if tempDepth1[length-1]!=0:
        tempDepth+=tempDepth1[length-1]

    depth1=(tempDepth//4)/count
    depth.append(depth1)

lis=[]
for i in range(0,pos):
    dic={"case_Id":pythonQuestion[i],"Average Block Depth":depth[i]}
    lis.append(dic)

print(len(lis))
with open("averageDepthOfPython.json","w") as f:
    json.dump(lis,f)
    print("finished")