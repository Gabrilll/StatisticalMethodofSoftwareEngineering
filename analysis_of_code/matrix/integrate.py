# 将5个维度的数据整合成json文件
import json

f1 = open('dimensions/m1m5.json')
f2 = open('dimensions/m2.json')
f3 = open('dimensions/operator.json')
f_diff = open('../../analysis_of_questions/realDifficultyIndex.json')
m1m5 = json.loads(f1.read())
m2 = json.loads(f2.read())
m3m4 = json.loads(f3.read())
diff = json.loads(f_diff.read())

res = {}

for case in diff:
    res[case] = {}
    values = res[case]
    values['M1'] = m1m5[case]['M1']
    values['M2'] = m2[case]["Average Block Depth"]
    values['M3'] = m3m4[case]['M3']
    values['M4'] = m3m4[case]['M4']
    values['M5'] = m1m5[case]['M5']
    values['difficulty_index'] = diff[case]['qRealDiff']

json_str = json.dumps(res)
with open('matrix.json', 'w') as json_file:
    json_file.write(json_str)

print(len(res))
