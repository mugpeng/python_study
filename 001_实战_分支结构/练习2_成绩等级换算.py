# 练习2：百分制成绩转换为等级制成绩。
'''
要求：如果输入的成绩在90分以上（含90分）输出A；
80分-90分（不含90分）输出B；
70分-80分（不含80分）输出C；
60分-70分（不含70分）输出D；60分以下输出E。
'''

scores = int(input("Please input ur score.\n"))
if scores >= 90:
    grade = "A"
elif scores >= 80:
    grade = "B"
elif scores >= 70:
    grade = "C"
elif scores >= 60:
    grade = "D"
elif scores >= 0:
    grade = "E"
else:
    print('Error, please input a integer.')
print('Ur score is: ', grade)