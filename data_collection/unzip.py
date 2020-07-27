import os
import zipfile

users = os.listdir()

for user in users:
    if user.isnumeric():
        cases = os.listdir(user)
        for case in cases:
            zip_src = os.listdir(user + '/' + case + '/question')
            for zip in zip_src:
                if zipfile.is_zipfile(user + '/' + case + '/question/'+zip):
                    fz = zipfile.ZipFile(user + '/' + case + '/question/'+zip)
                    fz.extract('.mooctest/answer.py', user + '/' + case)
