# 统计M3(操作符数量)和M4(不同操作符数量）
import json
import zipfile

one_char_op = ["+", "-", "*", "/", "|", "&", "<", ">", "=", "%", "~",
               "^", "@", "[", "]"]
two_char_op = ["==", "!=", "<=", ">=", "<<", ">>", "**", "//", ":="]
three_char_op = []
char_op = ['and', 'or', 'not', 'in', 'is', "del"]

j = open('../../../test_data.json', encoding='utf-8')
res = j.read()
data = json.loads(res)
z = zipfile.ZipFile('../../../data_collection/answers.zip')
cases = z.namelist()
print(cases)


def is_operator_2(index, case_code):
    if index + 1 < len(case_code):
        op = case_code[index] + case_code[index + 1]
        if op in two_char_op:
            return True
    return False


def is_operator_3(index, case_code):
    if index + 2 < len(case_code):
        op = case_code[index] + case_code[index + 1] + case_code[index + 2]
        if op in three_char_op:
            return True
    return False


def is_char_operator_2(index, case_code):
    if index + 1 >= len(case_code):
        return False
    if index > 0 and (case_code[index - 1] != ' ' and case_code[index - 1] not in one_char_op):
        return False
    if index + 2 < len(code) and case_code[index + 2] != ' ':
        return False
    if case_code[i] + case_code[i + 1] in char_op:
        return True
    return False


def is_char_operator_3(index, case_code):
    if index + 2 >= len(case_code):
        return False
    if index > 0 and (case_code[index - 1] != ' ' and case_code[index - 1] not in one_char_op):
        return False
    if index + 3 < len(code) and case_code[index + 3] != ' ':
        return False
    if case_code[i] + case_code[i + 1] + case_code[i + 2] in char_op:
        return True
    return False


exc = {}
for case in cases:
    f = z.open(case)
    m3 = []
    m4 = 0
    test = []
    for code in f:
        code = str(code, encoding='utf-8')
        code = code.lstrip()
        code = code.replace("\n", "")
        if code.startswith("#"):
            continue
        i = 0
        while i < len(code):
            if is_operator_3(i, code):
                op = code[i] + code[i + 1] + code[i + 2]
                if op not in m3:
                    m3.append(op)
                m4 += 1
                i += 2
                test.append(op)
            elif is_operator_2(i, code):
                op = code[i] + code[i + 1]
                if op not in m3:
                    m3.append(op)
                m4 += 1
                i += 1
                test.append(op)
            elif code[i] in one_char_op:
                op = code[i]
                if op not in m3:
                    m3.append(op)
                m4 += 1
                test.append(op)
            elif is_char_operator_3(i, code):
                op = code[i] + code[i + 1] + code[i + 2]
                if op not in m3:
                    m3.append(op)
                m4 += 1
                i += 2
                test.append(op)
            elif is_char_operator_2(i, code):
                op = code[i] + code[i + 1]
                if op not in m3:
                    m3.append(op)
                m4 += 1
                i += 1
                test.append(op)
            i += 1
    case_id = case.split('/')[-1][:-3]
    exc[case_id] = {}
    exc[case_id]["M3"] = len(m3)
    exc[case_id]["M4"] = m4

json_str = json.dumps(exc)
with open('operator.json', 'w') as json_file:
    json_file.write(json_str)

print(len(exc))
