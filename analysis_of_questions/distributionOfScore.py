# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 最终得分情况
# 颜色深浅表示得到最终得分的总共提交次数，颜色越深表示提交次数越多。

import json
import matplotlib.pyplot as plt
sample=[]
case=[]
group=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
with open('../test_data.json','rb') as f:
   data=json.load(f)
   for item in data:
       sample.append(item)
   for i in range(len(sample)):
       for j in range(len(data[sample[i]]['cases'])):
           item=data[sample[i]]['cases'][j]
           if(data[sample[i]]['cases'][j]['upload_records'])==0:
               data[sample[i]]['cases'][j]['time']=1
           else:
               data[sample[i]]['cases'][j]['time']=len(data[sample[i]]['cases'][j]['upload_records'])
           case.append(item['case_id'])
case=list(set(case))
case.sort()
for item in case:
    list1=[]
    for i in range(len(sample)):
        for item1 in data[sample[i]]['cases']:
            if(item1['case_id']==item):
                list1.append(item1['final_score'])
    while(len(list1)!=0):
        list1=[]
        for j in range(len(sample)):
            for item1 in data[sample[j]]['cases']:
                if(item1['case_id']==item):
                    if(item1['time']>0):
                        list1.append(item1['final_score'])
                        item1['time']-=1
        list1.sort()
        plt.hist(list1,group,color='#6FBD67',alpha=0.35,histtype='bar')
    plt.legend()
    plt.xlabel('score')
    plt.ylabel('Number of people')    
    plt.title(item)
    plt.savefig('scoresDigram/'+item+'.png',transparent=True)
    plt.clf()
