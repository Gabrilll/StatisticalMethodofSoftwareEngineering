# 下载数据
import json
import urllib.request, urllib.parse
import os

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
print(data)

for key in data:
    cases = data[key]['cases']
    print(cases)

    for case in cases:
        print(case["case_id"], case["case_type"])
        filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
        print(filename)
        url = os.path.dirname(case["case_zip"])+'/'+urllib.parse.quote(filename)
        lcdir = key+'/'+case["case_id"]
        qdir = lcdir+'/'+'question'
        exist = os.path.exists(qdir)
        if not exist:
            os.makedirs(qdir)
            urllib.request.urlretrieve(url, qdir+'/'+filename.replace('*','×'))
            uploads = case["upload_records"]
            for upload in uploads:
                updir = lcdir+'/'+'uploads'+'/'+str(upload['upload_id'])
                os.makedirs(updir)
                upfn = urllib.parse.unquote(os.path.basename(upload['code_url']))
                urllib.request.urlretrieve(upload['code_url'],updir+'/'+upfn)
