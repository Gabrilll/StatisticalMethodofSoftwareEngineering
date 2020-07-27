import json
import urllib.request,urllib.parse
import os
import zipfile
import pandas as pd
import csv
import time
import lizard
from radon.raw import analyze
path = 'test_data.json'
f = open(path,encoding='utf-8')
res = f.read()
data = json.loads(res)
sample=[]
case=[]
with open("m1m5.json",'rb') as f:
    data1 = json.load(f)
f.close()
for item in data:
   sample.append(item)
for i in range(len(sample)):
   for item in data[sample[i]]['cases']:
       case.append(item['case_id'])
case = list(set(case))
case.sort()
cyCpl = []
number = 0
f.close()
z = zipfile.ZipFile('answers.zip')
for item in case:
    isF = False
    for user in data:
        cases = data[user]['cases']
        for oneCase in cases:
            if oneCase["case_id"] == item:
                z.extract('answers/'+item+'.py')
                listA = []
                complexity = 0
                lloc = 0
                try:
                    info = lizard.analyze_file('answers/'+item+'.py')
                    mydict = info.__dict__
                    lloc = len(mydict["function_list"])
                    for i in range(len(mydict["function_list"])):
                        listA.append(info.function_list[i].__dict__)
                except BaseException:
                    lloc = data1[item]['M5']
                    complexity = data1[item]['M1']
                    print("读取错误")
                if(data1[item]['M1']!=0 and complexity==0):
                    complexity=data1[item]['M1']
                listC = []
                f.close()
                if len(listA) == 0:
                    listC.append(0)
                else:
                   for oneItem in listA:
                       listC.append(int(oneItem['cyclomatic_complexity']))
                print(max(listC),end='')
                print(" ",end='')
                print(lloc)
                cyCpl.append([item, max(listC), lloc])
                isF = True
                number+=1
                break
        if isF:
            break
    if(number == 30):
        time.sleep(2)
        number = 0
print(cyCpl)
with open("softwareMatirx.csv", 'a+',newline='') as dstfile:
    writer = csv.writer(dstfile)
    writer.writerows(cyCpl)  # 批量写入
dstfile.close()

