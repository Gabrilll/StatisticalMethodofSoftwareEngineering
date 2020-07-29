# 将5个维度的数据整合成csv文件
import csv
import json

f = open('matrix.csv', 'w', newline='')
writer = csv.writer(f)
f_j = open('matrix.json')
data = json.loads(f_j.read())

writer.writerow(['case_id', 'M1', 'M2', 'M3', 'M4', 'M5', 'difficulty_index'])

lines = []

for case in data:
    line = []
    line.append(case)
    line.append(data[case]['M1'])
    line.append(data[case]['M2'])
    line.append(data[case]['M3'])
    line.append(data[case]['M4'])
    line.append(data[case]['M5'])
    line.append(data[case]['difficulty_index'])
    lines.append(line)

writer.writerows(lines)
print(len(lines))
