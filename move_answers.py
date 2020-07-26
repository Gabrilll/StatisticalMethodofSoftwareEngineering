import os
import shutil

users = os.listdir()
exercise = []

for user in users:
    if user.isnumeric():
        cases = os.listdir(user)
        for case in cases:
            if case not in exercise:
                path = user + '/' + case + '/.mooctest/answer.py'
                if os.path.exists(path):
                    aim = 'answers/' + case + '.py'
                    shutil.move(path, aim)
                    exercise.append(case)

print(len(exercise))
