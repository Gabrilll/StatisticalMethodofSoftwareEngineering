import webbrowser
from analysis_of_question_set import averageDifficultyOfTestPaper
from analysis_of_question_set import evaluate_portion_of_classification
GEN_HTML = 'question_set.html'

f = open(GEN_HTML, 'w')

background='background.jpg'
values=averageDifficultyOfTestPaper.values()
img=evaluate_portion_of_classification.value()

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
    <h3>试题分析</h3>
    <table style="border-top:3px #309F73 solid;border-bottom:3px #309F73 solid;" cellpadding="30" rules="rows">
    <caption>试题分析</caption>
    <tr><th>试题难度</th><th>试题区分度</th></tr>
    <tr><td>%s</td><td>%s</td></tr>
    </table>
    <br><br>
    <img src=%s height="400" width="550">
    </body>
    </html>""" % (background,round(values[0],2),round(values[1],2),img)

f.write(message)
f.close()
webbrowser.open(GEN_HTML)