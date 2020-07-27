import matplotlib.pyplot as plt
import json
import seaborn as sns


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


def plot(exercise_id):
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


plot("2234")
