import matplotlib.pyplot as plt
import json
import seaborn as sns
import numpy as np
import math

f = open('../test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
score_dis = {}

for key in data:
    cases = data[key]['cases']

    for case in cases:
        case_id = case['case_id']
        if case_id not in score_dis:
            score_dis[case_id] = {}
        uploads = case['upload_records']
        cur_exc = score_dis[case_id]
        for upload in uploads:
            score = upload["score"]
            if score not in cur_exc:
                cur_exc[score] = 0
            cur_exc[score] += 1


def plot_1(exercise_id):
    exc = score_dis[exercise_id]
    x = {}
    y = []
    for score in exc:
        x[math.floor(score + 0.5)] = exc[score]
    ac_x = np.arange(0, 101, 1)
    print(x)
    for temp in ac_x:
        if temp in x:
            y.append(x[temp])
        else:
            y.append(0)
    plt.ylim(0, max(y))
    plt.xlim(0, 100)
    plt.fill_between(ac_x, y, 0, color="green", alpha=0.4)
    plt.plot(ac_x, y)
    print(ac_x, y)
    plt.title("score distribution")
    plt.ylabel('upload_times')
    plt.xlabel('score')
    plt.show()


def plot_2(exercise_id):
    exc = score_dis[exercise_id]
    x = []
    for score in exc:
        times = exc[score]
        for i in range(0, times):
            x.append(score)
    sns.distplot(x, color='g', rug=True, bins=20, kde=False, norm_hist=False, rug_kws={'color': 'g'})
    plt.xlim(0, 100)
    plt.title("score distribution")
    plt.ylabel('upload_times')
    plt.xlabel('score')
    plt.show()


def plot_3(exercise_id):
    exc = score_dis[exercise_id]
    x = []
    for score in exc:
        times = exc[score]
        for i in range(0, times):
            x.append(score)
    sns.distplot(x, color='g', bins=20)
    plt.xlim(0, 100)
    plt.title("score distribution")
    plt.xlabel('score')
    plt.show()


def plot_4(exercise_id):
    exc = score_dis[exercise_id]
    x = []
    for score in exc:
        times = exc[score]
        for i in range(0, times):
            x.append(score)
    sns.distplot(x, hist=False, color='g', kde_kws={"shade": True})
    plt.xlim(0, 100)
    plt.title("score distribution")
    plt.xlabel('score')
    plt.show()


plot_4("2234")
