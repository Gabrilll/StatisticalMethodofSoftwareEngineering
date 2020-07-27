import json

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
exc = {}
req = {}

for key in data:
    cases = data[key]['cases']

    for case in cases:
        case_id = case['case_id']
        if case_id not in exc:
            exc[case_id] = {}
            exc[case_id]['sum'] = 0
            exc[case_id]['times'] = 0
            exc[case_id]['average'] = 0
            req[case_id] = {}
            req[case_id]['times'] = 0
            req[case_id]['average'] = 0
        uploads = case['upload_records']
        for upload in uploads:
            exc[case_id]['sum'] += upload['score']
            exc[case_id]['times'] += 1
            exc[case_id]['average'] = exc[case_id]['sum'] / exc[case_id]['times']
            req[case_id]['times'] = exc[case_id]['times']
            req[case_id]['average'] = exc[case_id]['average']

json_str = json.dumps(req)
with open('average.json', 'w') as json_file:
    json_file.write(json_str)

print(len(req))
