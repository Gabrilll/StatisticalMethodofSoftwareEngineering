# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import matplotlib.pyplot as plt
sample=[]
case=[]
group=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
with open('../test_data.json', 'rb') as f:
    data = json.load(f)
    for item in data:
        sample.append(item)
    for i in range(len(sample)):
        for item in data[sample[i]]['cases']:
            case.append(item['case_id'])
case=list(set(case))
case.sort()
count=[]
for item in case:
    list1=[]
    for i in range(len(sample)):
        for item1 in data[sample[i]]['cases']:
            if(item1['case_id']==item):
                list1.append(item1['final_score'])
                count.append(len(item1['upload_records']))
while(len(list1)!=0):
    for item in case:
        cur=0
        list1=[]
        for i in range(len(sample)):
            for item1 in data[sample[i]]['cases']:
                if(item1['case_id']==item):
                    if(count[cur]>0):
                        list1.append(item1['final_score'])
                        count[cur]-=1
                    cur+=1
        list1.sort()
        plt.hist(list1,group,color='#97DFF7',alpha=0.35,histtype='bar')
    plt.legend()
    plt.xlabel('score')
    plt.ylabel('Number of people')    
    plt.title(item)
    plt.savefig('scoresDigram/'+item+'.png')
    plt.clf()