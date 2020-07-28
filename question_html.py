import webbrowser
import json
from analysis_of_questions import plot_score_distribution

GEN_HTML = 'question.html'

f = open(GEN_HTML, 'w')
f_a = open('analysis_of_questions/average.json')
f_d = open('analysis_of_questions/realDifficultyIndex.json')
f_v = open('analysis_of_questions/qRealDiscrim.json')
f_c = open('analysis_of_code/complexity.json')
f_m=open('analysis_of_code/matrix/matrix.json')
res_a = f_a.read()
res_d = f_d.read()
res_v = f_v.read()
res_c = f_c.read()
res_m=f_m.read()
data_a = json.loads(res_a)
data_d = json.loads(res_d)
data_v = json.loads(res_v)
data_c = json.loads(res_c)
data_m=json.loads(res_m)


background='background.jpg'

def show_question(id):
    img = plot_score_distribution.plot(id)
    img2="analysis_of_questions/scoresDigram/"+id+".png"
    message = """
    <html>
    <head>
    <style>
    table, th, td {
        border-collapse: collapse;
    }
    tr{
    border_bottom:1px solid
    }
    th, td {
        padding: 5px;
        text-align: center;
    }
    </style>
    </head>
    <body background=%s>
    <h3>题目分析</h3>
    <table style="border-top:3px #309F73 solid;border-bottom:3px #309F73 solid;" cellpadding="30" rules="rows">
    <caption>题目分析</caption>
    <tr><th>总提交次数</th><th>平均得分</th><th>难度指数</th><th>区分度</th><th>代码复杂度</th></tr>
    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <br><br>
    <h3>代码分析</h3>
    <table style="border-top:3px #309F73 solid;border-bottom:3px #309F73 solid;" cellpadding="10" rules="rows">
    <caption>代码分析矩阵</caption>
    <tr><th>圈复杂度</th><th>平均嵌套块深度</th><th>操作符数量</th><th>不同操作符数量</th><th>方法调用次数</th></tr>
    <tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>
    </table>
    <br><br><br>
    <table><tr>
    <tr><th>提交得分分布</th><th>最终得分分布</th></tr>
    <td><img src=%s border=0 height="400" width="550" ></td>
    <td><img src=%s border=0 height="400" width="550"></td>
    </tr></table>
    </body>
    </html>""" % (background,data_a[id]['times'],
        round(data_a[id]['average'], 2), round(data_d[id]['qRealDiff'] / 100, 2), round(data_v[id]['qRealDiscrim'], 2),
        round(data_c[id]['predict_complexity']/5, 2), data_m[id]["M1"],round(data_m[id]["M2"],2),data_m[id]["M3"],data_m[id]["M4"],data_m[id]["M5"],img,img2)

    f.write(message)
    f.close()
    webbrowser.open(GEN_HTML)

show_question("2087")
